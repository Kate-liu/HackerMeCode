<?php

class Person2
{

    function speak()
    {
        echo "hello world!\n";
    }

    function __call($funcName, $args)
    {
        echo "你调用的" . $funcName . "方法，参数为：\n";
        print_r($args);
        echo "不存在\n";
    }

}

$per = new Person2();
$per->talk("我是新来的");
$per->say("hello I'm tom", '12');
$per->speak();


?>
