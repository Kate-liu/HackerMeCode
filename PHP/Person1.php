<?php

class Person1
{
    public $name;
    public $age;

    public function __construct($name, $age)
    {
        echo "构造函数调用，对象正在创建\n";
        $this->name = $name;
        $this->age = $age;
    }

    public function __toString()
    {
        // TODO: Implement __toString() method.
        return "my name is " . $this->name . ", I am " . $this->age . " years old \n";
    }

    public function __destruct()
    {
        echo "析构函数调用，对象被销毁了\n";
    }

}

$tom = new Person1('tom', '12');
echo $tom;

?>
