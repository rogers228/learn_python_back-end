
## 字串相加
```php
<?php
    echo 'hello '.  $name; // 字串相加
    echo '<br>';  // 換行
    echo "hello $name."; echo '<br>'; // 使用雙引號 在字串中直接寫變數
?>
```

## 字串擷取
```php
    $x = "Hello world!";
    echo substr($x, 6, 5); echo '<br>';    // world
    echo substr($x, 6) ; echo '<br>';      // world!
    echo substr($x, -5, 3); echo '<br>';   //  orl
```