<?php

class Person3
{

    public $name;
    public $age;

    public function __construct($name, $age)
    {
        $this->name = $name;
        $this->age = $age;
    }

}

$tom = new Person3('tom', '12');
var_dump(serialize($tom));

?>
