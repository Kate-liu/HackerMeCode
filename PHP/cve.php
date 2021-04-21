<?php
header('Content-Type: text/html; charset=utf-8');

class Person
{

    public $name;
    public $age;

    public function __construct($name, $age)
    {
        $this->name = $name;
        $this->age = $age;
    }

    public function __destruct()
    {
        // TODO: Implement __destruct() method.
        $fp = fopen("/var/www/html/escape.php", "w");
        fputs($fp, $this->name);
        fputs($fp, $this->age);
        fclose($fp);
    }

}

$s1 = 'O:6:"Person":2:{s:4:"name";s:3:"tom";s:3:"age";s:25:"<script>alert(1)</script>";}';
$s2 = 'O:6:"Person":2:{s:4:"name";s:3:"tom";s:3:"age";s:18:"<%php phpinfo();%>";}';
$p = unserialize($s2);

unset($p);
include(__dir__ . '/escape.php');

?>
