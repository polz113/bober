<?php

class CSV {

    public static function toArray($fileContent, $delimiter = ';', $enclosure = '"', $escape = '\\') {

        $lines = array();
        $fields = array();

        if ($escape == $enclosure) {
            $escape = '\\';
            $fileContent = str_replace(array('\\', $enclosure . $enclosure, "\r\n", "\r"), array('\\\\', $escape . $enclosure, "\\n", "\\n"), $fileContent);
        } else {
            $fileContent = str_replace(array("\r\n", "\r"), array("\\n", "\\n"), $fileContent);
        }

        $nb = strlen($fileContent);
        $field = '';
        $inEnclosure = false;
        $previous = '';

        for ($i = 0; $i < $nb; $i++) {
            $c = $fileContent[$i];
            if ($c === $enclosure) {
                if ($previous !== $escape) {
                    $inEnclosure ^= true;
                } else {
                    $field .= $enclosure;
                }
            } else if ($c === $escape) {
                $next = $fileContent[$i + 1];
                if ($next != $enclosure && $next != $escape) {
                    $field .= $escape;
                }
            } else if ($c === $delimiter) {
                if ($inEnclosure) {
                    $field .= $delimiter;
                } else {
                    //end of the field
                    $fields[] = $field;
                    $field = '';
                }
            } else if ($c === "\n") {
                $fields[] = $field;
                $field = '';
                $lines[] = $fields;
                $fields = array();
            } else {
                $field .= $c;
            }
            $previous = $c;
        }
        //we add the last element
        if (true || $field !== '') {
            $fields[] = $field;
            $lines[] = $fields;
        }
        return $lines;
    }

}

?>