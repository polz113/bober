<?php

class Svg2Pdf {

    public static function Convert($svg, $replace = array()) {
        if (count($replace) > 0) {
            $svg = strtr($svg, $replace);
        }
        $tmp_file = tempnam(sys_get_temp_dir(), 'svg2pdf');
        file_put_contents($tmp_file . '.svg', $svg);
        $inkscape = trim(shell_exec('/usr/bin/which inkscape'));
        shell_exec($inkscape . ' -z -f ' . $tmp_file . '.svg -A ' . $tmp_file . '.pdf');
        if (file_exists($tmp_file . '.pdf')) {
            $pdf = file_get_contents($tmp_file . '.pdf');
            // cleanup
            @unlink($tmp_file);
            @unlink($tmp_file . '.svg');
            @unlink($tmp_file . '.pdf');
            $log = 'Svg2Pdf :: Convert :: PDF file size: ' . strlen($pdf);
            if (defined('THREAD') && defined('THREAD_TYPE')) {
                print date('d.m.Y H:i:s') . ' :: ' . THREAD_TYPE . ' Thread :: ' . str_pad(THREAD, 3, '0', STR_PAD_LEFT) . ' :: ' . $log . "\n";
            }
            return $pdf;
        } else {
            return null;
        }
    }

    public static function BatchConvert($svg, $data = array(), $background = false) {
        $count = count($data);
        if ($count == 0) {
            return null;
        }
        $workerJobSet = new WorkerJobSet($background, false);
        for ($i = 0; $i < $count; ++$i) {
            $workerJobSet->addTask('Svg2Pdf', "Convert", array($svg, $data[$i]));
        }
        // svg 2 pdf jobs
        $svg_to_pdf_jobs = array();
        // optimize fetch from database, not to load everying if we need only id
        $criteria = new CDbCriteria();
        $criteria->select = 't.id'; 
        $criteria->condition = 't.job_set_id = '.$workerJobSet->getJobSetId();
        $JobList = Job::model()->findAll($criteria);
        // $JobList = Job::model()->findAll('job_set_id=:job_set_id', array(':job_set_id' => $workerJobSet->getJobSetId()));
        foreach ($JobList as $Job) {
            $svg_to_pdf_jobs[] = $Job->id;
        }
        if (!$background) {
            $result = $workerJobSet->run();
            if ($result != null) {
                $workerJobSetMerge = new WorkerJobSet($background, false);
                $workerJobSetMerge->addTask('Svg2Pdf', 'MergePDF', array($svg_to_pdf_jobs));
                $resultPDF = $workerJobSetMerge->run();
                // clean up database
                $jobSet = JobSet::model()->find('id=:id', array(':id' => $workerJobSet->getJobSetId()));
                if ($jobSet != null) {
                    $jobSet->delete();
                }
                $jobSetMerge = JobSet::model()->find('id=:id', array(':id' => $workerJobSetMerge->getJobSetId()));
                if ($jobSetMerge != null) {
                    $jobSetMerge->delete();
                }
                if (isset($resultPDF[0])) {
                    return $resultPDF[0];
                } else {
                    return null;
                }
            } else {
                return null;
            }
        } else {
            $job_id = $workerJobSet->addTask('Svg2Pdf', 'MergePDF', array($svg_to_pdf_jobs));
            $result = $workerJobSet->run();
            $workerJobSet->setFinalJobResultId($job_id);
            return $workerJobSet->getJobSetId();
        }
    }

    public static function MergePDF($svg_to_pdf_jobs) {
        $log = "Svg2Pdf :: MergePDF :: MergePDF pdf jobs: " . implode(', ', $svg_to_pdf_jobs);
        if (defined('THREAD') && defined('THREAD_TYPE')) {
            print date('d.m.Y H:i:s') . ' :: ' . THREAD_TYPE . ' Thread :: ' . str_pad(THREAD, 3, '0', STR_PAD_LEFT) . ' :: ' . $log . "\n";
        }
        // počakat moramo, da so vsi svg 2 pdf narjeni, preden jih gremo mergat
        for ($i = 0; $i < 2; ++$i) {
            do {
                $job_check = Job::model()->find('id in (:ids) and (finished=:finished or result IS NULL)', array(':ids' => implode(', ', $svg_to_pdf_jobs), ':finished' => 0));
                if ($job_check != null) {
                    $log = 'Svg2Pdf :: MergePDF :: Need to wait to all SVG 2 PDF jobs are finished...';
                    if (defined('THREAD') && defined('THREAD_TYPE')) {
                        print date('d.m.Y H:i:s') . ' :: ' . THREAD_TYPE . ' Thread :: ' . str_pad(THREAD, 3, '0', STR_PAD_LEFT) . ' :: ' . $log . "\n";
                    }
                    sleep(1);
                }
            } while ($job_check != null);
        }

        $pdf_list = array();
        foreach ($svg_to_pdf_jobs as $job_id) {
            $job = Job::model()->find('id=:id', array(':id' => $job_id));
            if ($job == null) {
                $log = 'Svg2Pdf :: MergePDF :: Job with ID: ' . $job_id . ' not found!!!';
                if (defined('THREAD') && defined('THREAD_TYPE')) {
                    print date('d.m.Y H:i:s') . ' :: ' . THREAD_TYPE . ' Thread :: ' . str_pad(THREAD, 3, '0', STR_PAD_LEFT) . ' :: ' . $log . "\n";
                }
                $job = new Job();
                continue;
            }
            if (strlen($job->result) == 0) {
                $log = 'Svg2Pdf :: MergePDF :: Found one empty PDF, retry function MergePDF...';
                if (defined('THREAD') && defined('THREAD_TYPE')) {
                    print date('d.m.Y H:i:s') . ' :: ' . THREAD_TYPE . ' Thread :: ' . str_pad(THREAD, 3, '0', STR_PAD_LEFT) . ' :: ' . $log . "\n";
                }
                sleep(1);
                return self::MergePDF($svg_to_pdf_jobs);
            }
            $log = 'Svg2Pdf :: MergePDF :: Found Job ID: ' . $job->id . ', PDF size: ' . strlen($job->result);
            if (defined('THREAD') && defined('THREAD_TYPE')) {
                print date('d.m.Y H:i:s') . ' :: ' . THREAD_TYPE . ' Thread :: ' . str_pad(THREAD, 3, '0', STR_PAD_LEFT) . ' :: ' . $log . "\n";
            }
            $pdf_list[] = unserialize(base64_decode($job->result));
        }
        $log = 'Svg2Pdf :: MergePDF :: PDF to merge: ' . count($pdf_list);
        if (defined('THREAD') && defined('THREAD_TYPE')) {
            print date('d.m.Y H:i:s') . ' :: ' . THREAD_TYPE . ' Thread :: ' . str_pad(THREAD, 3, '0', STR_PAD_LEFT) . ' :: ' . $log . "\n";
        }
        $list = array();

        $gs = trim(shell_exec('/usr/bin/which gs'));
        $cmd = $gs . ' -q -dNOPAUSE -dBATCH -sDEVICE=pdfwrite -sOutputFile=';
        $counter = 0;
        do {
            $new_pdf_list = array();

            $output_file = tempnam(sys_get_temp_dir(), 'pdfmerge');
            $list[] = $output_file;
            $list[] = $output_file . '.pdf';
            $cmd_to_exec = $cmd . $output_file . '.pdf ';
            $new_pdf_list[] = $output_file . '.pdf';
            for ($i = 0; $i < count($pdf_list); ++$i) {
                if ($i < 10) {
                    $tmp_file = tempnam(sys_get_temp_dir(), 'pdfformerge');
                    file_put_contents($tmp_file . '.pdf', $pdf_list[$i]);
                    $cmd_to_exec .= $tmp_file . '.pdf ';
                    $list[] = $tmp_file;
                    $list[] = $tmp_file . '.pdf';
                } else {
                    $new_pdf_list[] = $pdf_list[$i];
                }
            }
            $result = shell_exec($cmd_to_exec);
            $counter++;
            $log = 'Svg2Pdf :: MergePDF :: Anti too long command handler, merging blocks of 10 pdfs, cylce number: ' . $counter;
            if (defined('THREAD') && defined('THREAD_TYPE')) {
                print date('d.m.Y H:i:s') . ' :: ' . THREAD_TYPE . ' Thread :: ' . str_pad(THREAD, 3, '0', STR_PAD_LEFT) . ' :: ' . $log . "\n";
            }
            $new_pdf_list[0] = file_get_contents($output_file . '.pdf');
            $pdf_list = $new_pdf_list;
        } while (count($pdf_list) > 1);

        for ($i = 0; $i < count($list); ++$i) {
            @unlink($list[$i]);
        }
        return $pdf_list[0];
    }

}

?>