<?php
    $name = 'roger3';
    echo 'hello '.  $name;
    echo '<br>';
    echo "hello $name."; echo '<br>';
    print('test'); echo '<br>';

    $name = 'andy';
    var_dump($name); echo '<br>'; // int(5)
    $name = 'mary';
    echo "hello $name." . PHP_EOL; // 通用各系統的換行
    $x = 5;
    var_dump($x); echo '<br>'; // int(5)
    $x = true;
    var_dump($x);echo '<br>';
    $x = false;
    var_dump($x);echo '<br>----------<br>';
    $cars = array("Volvo","BMW","Toyota");
    var_dump($cars); echo '<br>';
    $arr = array('a', 4, true); // 陣列為指標可 存放不同類型
    var_dump($arr); echo '<br>----------<br>';
    $x = "Hello world!";
    $x = null;
    var_dump($x); echo '<br>----------<br>';
    $x = "Hello world!";
    echo substr($x, 6, 5); echo '<br>';    // world
    echo substr($x, 6) ; echo '<br>';      // world!
    echo substr($x, -5, 3); echo '<br>';   //  orl

    echo '<br>----------<br>';
    $members = array("Peter"=>"35", "Ben"=>"37", "Joe"=>"43");
    foreach ($members as $x => $y) {
        echo "$x : $y <br>";
    }

?>