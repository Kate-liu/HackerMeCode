<?php

class Person4
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

$s = 'O:7:"Person4":2:{s:4:"name";s:3:"tom";s:3:"age";s:2:"12";}';
$p = unserialize($s);

echo $p->name;
echo "\n";
echo $p->age;
echo "\n";

?>
