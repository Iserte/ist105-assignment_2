<?php
$a = $_GET['a'] ?? 1;
$b = $_GET['b'] ?? 1;
$c = $_GET['c'] ?? 1;

$command = escapeshellcmd("python3 /var/www/html/calculate.py $a $b $c");
$output = shell_exec($command);

echo $output;
?>