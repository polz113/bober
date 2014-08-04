<?php
 
/**
 * DefaultDateTimeParser converts a date/time string to an array
 *
 * The following pattern characters are recognized:
 * <pre>
 * Pattern |      Description
 * ----------------------------------------------------
 * d       | Day of month 1 to 31, no padding
 * dd      | Day of month 01 to 31, zero leading
 * M       | Month digit 1 to 12, no padding
 * MM      | Month digit 01 to 12, zero leading
 * yy      | 2 year digit, e.g., 96, 05
 * yyyy    | 4 year digit, e.g., 2005
 * h       | Hour in 0 to 23, no padding
 * hh      | Hour in 00 to 23, zero leading
 * H       | Hour in 0 to 23, no padding
 * HH      | Hour in 00 to 23, zero leading
 * m       | Minutes in 0 to 59, no padding
 * mm      | Minutes in 00 to 59, zero leading
 * s       | Seconds in 0 to 59, no padding
 * ss      | Seconds in 00 to 59, zero leading
 * a       | AM or PM, case-insensitive (since version 1.1.5)
 * ----------------------------------------------------
 * </pre>
 *
 *
 * Modified version of http://www.yiiframework.com/doc/api/1.1/CDateTimeParser
 *
 * This version will accept a pattern and default the time values for any missing pattern
 * It returns a string rather than a timestamp in case its the wrong timezone
 * Also uses the LocalTime class to get the time for now() in the users timezone
 * For example, DefaultDateTimeParser::parse('31/12/2011','dd/MM/yyyy',array('hour'=>0,'minute'=>0,'day'=>0);
 * Will return '2011-12-2011 0:0:0'
 */
class DefaultDateTimeParser
{
 
    public static function parse($value,$pattern='MM/dd/yyyy',$defaults=array())
    {
        $tokens=self::tokenize($pattern);
        $i=0;
        $n=strlen($value);
        foreach($tokens as $token)
        {
            switch($token)
            {
                case 'yyyy':
                {
                    if(($year=self::parseInteger($value,$i,4,4))!==null)
                        $i+=4;
                    break;
                }
                case 'yy':
                {
                    if(($year=self::parseInteger($value,$i,1,2))!==null)
                        $i+=strlen($year);
                    break;
                }
                case 'MM':
                {
                    if(($month=self::parseInteger($value,$i,2,2))!==null)
                        $i+=2;
                    break;
                }
                case 'M':
                {
                    if(($month=self::parseInteger($value,$i,1,2))!==null)
                        $i+=strlen($month);
                    break;
                }
                case 'dd':
                {
                    if(($day=self::parseInteger($value,$i,2,2))!==null)
                        $i+=2;
                    break;
                }
                case 'd':
                {
                    if(($day=self::parseInteger($value,$i,1,2))!==null)
                        $i+=strlen($day);
                    break;
                }
                case 'h':
                case 'H':
                {
                    if(($hour=self::parseInteger($value,$i,1,2))!==null)
                        $i+=strlen($hour);
                    break;
                }
                case 'hh':
                case 'HH':
                {
                    if(($hour=self::parseInteger($value,$i,2,2))!==null)
                        $i+=2;
                    break;
                }
                case 'm':
                {
                    if(($minute=self::parseInteger($value,$i,1,2))!==null)
                        $i+=strlen($minute);
                    break;
                }
                case 'mm':
                {
                    if(($minute=self::parseInteger($value,$i,2,2))!==null)
                        $i+=2;
                    break;
                }
                case 's':
                {
                    if(($second=self::parseInteger($value,$i,1,2))!==null)
                        $i+=strlen($second);
                    break;
                }
                case 'ss':
                {
                    if(($second=self::parseInteger($value,$i,2,2))!==null)
                        $i+=2;
                    break;
                }
                case 'a':
                {
                    // If this value isn't present then ignore it
                    if(($ampm=self::parseAmPm($value,$i))===null)
                        break;
 
                    if(isset($hour))
                    {
                        if($hour==12 && $ampm==='am')
                            $hour=0;
                        else if($hour<12 && $ampm==='pm')
                            $hour+=12;
                    }
                    $i+=2;
                    break;
                }
                default:
                {
                    // If the separator pattern doesn't exist in the value, then ignore it
                    // eg: a space
                    if (strpos($value, $token)===false)
                            break;
 
                    $tn=strlen($token);
                    if($i>=$n || substr($value,$i,$tn)!==$token)
                        return false;
                    $i+=$tn;
                    break;
                }
            }
        }
        if($i<$n) // somethings gone wrong
            return false;
 
        // Defaults to the date/time for the local timezone
        // If you don't want to use Yii::app()-localtime->localNow() then simply replace with the php date() function
        // Yii::app()->localtime-> = LocalTime::
        if(!isset($year))
            $year=isset($defaults['year']) ? $defaults['year'] : Yii::app()->localtime->localNow('Y'); // date('Y');
        if(!isset($month))
            $month=isset($defaults['month']) ? $defaults['month'] : Yii::app()->localtime->localNow('n'); // date('n');
        if(!isset($day))
            $day=isset($defaults['day']) ? $defaults['day'] : Yii::app()->localtime->localNow('j'); // date('j');
        if(!isset($hour))
            $hour=isset($defaults['hour']) ? $defaults['hour'] : Yii::app()->localtime->localNow('H'); // date('H');
        if(!isset($minute))
            $minute=isset($defaults['minute']) ? $defaults['minute'] : Yii::app()->localtime->localNow('i'); // date('i');
        if(!isset($second))
            $second=isset($defaults['second']) ? $defaults['second'] : Yii::app()->localtime->localNow('s'); // date('s');
 
        $year=(int)$year;
        $month=(int)$month;
        $day=(int)$day;
        $hour=(int)$hour;
        $minute=(int)$minute;
        $second=(int)$second;
 
 
        if(CTimestamp::isValidDate($year,$month,$day) && CTimestamp::isValidTime($hour,$minute,$second))
        {
            // Return a time string rather than a timestamp because the timestamp might be the wrong timezone?
            return $year.'-'.$month.'-'.$day.' '.$hour.':'.$minute.':'.$second;
        }
        else
            return false;
    }
 
    /*
     * @param string $pattern the pattern that the date string is following
     */
    private static function tokenize($pattern)
    {
        if(!($n=strlen($pattern)))
            return array();
        $tokens=array();
        for($c0=$pattern[0],$start=0,$i=1;$i<$n;++$i)
        {
            if(($c=$pattern[$i])!==$c0)
            {
                $tokens[]=substr($pattern,$start,$i-$start);
                $c0=$c;
                $start=$i;
            }
        }
        $tokens[]=substr($pattern,$start,$n-$start);
        return $tokens;
    }
 
    /*
     * @param string $value the date string to be parsed
     * @param integer $offset starting offset
     * @param integer $minLength minimum length
     * @param integer $maxLength maximum length
     */
    protected static function parseInteger($value,$offset,$minLength,$maxLength)
    {
        for($len=$maxLength;$len>=$minLength;--$len)
        {
            $v=substr($value,$offset,$len);
            if(ctype_digit($v) && strlen($v)>=$minLength)
                return $v;
        }
        // Changed by Russell England to null rather than false
        return null;
    }
 
    /*
     * @param string $value the date string to be parsed
     * @param integer $offset starting offset
     */
    protected static function parseAmPm($value, $offset)
    {
        $v=strtolower(substr($value,$offset,2));
        return $v==='am' || $v==='pm' ? $v : false;
    }
}
?>