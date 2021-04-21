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

    public function __wakeup()
    {
        echo "wakeup 被调用\n";
    }

}

$s = 'O:6:"Person":2:{s:4:"name";s:3:"tom";s:3:"age";s:25:"<script>alert(1)</script>";}';
$p = unserialize($s);

echo $p->name;
echo "\n";
echo $p->age;
echo "\n";

?>
