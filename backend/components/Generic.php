<?php

class Generic {

    public static function isSuperAdmin() {
        $cache_key = 'isUserSuperuser#' . Yii::app()->user->id;
        $cached = Yii::app()->cache->get($cache_key);
        if ($cached == null) {
            $user = User::model()->find('id=:id', array(':id' => Yii::app()->user->id));
            $superuser = $user != null ? $user->superuser : 0;
            $cached = $superuser == 1;
            Yii::app()->cache->set($cache_key, $cached, 600);
        }
        return $cached;
    }

    public static function getUserRole() {
        $cache_key = 'userRole#' . Yii::app()->user->id;
        $cached = Yii::app()->cache->get($cache_key);
        if ($cached == null) {
            $user = User::model()->with('profile')->find('id=:id', array(':id' => Yii::app()->user->id));
            $cached = $user != null ? $user->profile->user_role : 0;
            Yii::app()->cache->set($cache_key, $cached, 600);
        }
        return $cached;
    }

    public static function isCoordinator() {
        $cache_key = 'userIsCoordinator#' . Yii::app()->user->id;
        $cached = Yii::app()->cache->get($cache_key);
        if ($cached == null) {
            $cached = false;
            $schoolMentor = SchoolMentor::model()->find('user_id=:user_id and coordinator=:coordinator', array(':user_id' => Yii::app()->user->id, ':coordinator' => 1));
            if ($schoolMentor != null) {
                $cached = true;
            }
            Yii::app()->cache->set($cache_key, $cached, 600);
        }
        return $cached;
    }

    public static function orderBy(&$ary, $clause, $ascending = true, $numeric = true) {
        setlocale(LC_ALL, 'sl_SI.UTF-8');
        $clause = str_ireplace('order by', '', $clause);
        $clause = preg_replace('/\s+/', ' ', $clause);
        $keys = explode(',', $clause);
        $dirMap = array('desc' => 1, 'asc' => -1);
        $def = $ascending ? -1 : 1;

        $keyAry = array();
        $dirAry = array();
        foreach ($keys as $key) {
            $key = explode(' ', trim($key));
            $keyAry[] = trim($key[0]);
            if (isset($key[1])) {
                $dir = strtolower(trim($key[1]));
                $dirAry[] = $dirMap[$dir] ? $dirMap[$dir] : $def;
            } else {
                $dirAry[] = $def;
            }
        }

        $fnBody = '';
        for ($i = count($keyAry) - 1; $i >= 0; $i--) {
            $k = $keyAry[$i];
            $t = $dirAry[$i];
            $f = -1 * $t;
            $aStr = '$a[\'' . $k . '\']';
            $bStr = '$b[\'' . $k . '\']';
            if (strpos($k, '(') !== false) {
                $aStr = '$a->' . $k;
                $bStr = '$b->' . $k;
            }
            if ($numeric) {
                if ($fnBody == '') {
                    $fnBody .= "if({$aStr} == {$bStr}) { return 0; }\n";
                    $fnBody .= "return ({$aStr} < {$bStr}) ? {$t} : {$f};\n";
                } else {
                    $fnBody = "if({$aStr} == {$bStr}) {\n" . $fnBody;
                    $fnBody .= "}\n";
                    $fnBody .= "return ({$aStr} < {$bStr}) ? {$t} : {$f};\n";
                }
            } else {
                if ($fnBody == '') {
                    $fnBody .= "if({$aStr} == {$bStr}) { return 0; }\n";
                    $fnBody .= "return (strcoll({$aStr}, {$bStr}) < 0) ? {$t} : {$f};\n";
                } else {
                    $fnBody = "if({$aStr} == {$bStr}) {\n" . $fnBody;
                    $fnBody .= "}\n";
                    $fnBody .= "return (strcoll({$aStr}, {$bStr}) < 0) ? {$t} : {$f};\n";
                }
            }
        }

        if ($fnBody) {
            $sortFn = create_function('$a,$b', $fnBody);
            if (is_array($ary)) {
                usort($ary, $sortFn);
            }
        }
    }

}
