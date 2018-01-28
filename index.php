<?php 
echo "This is the first application";
$r=exec("python wer.py");
echo '<br>';
$k=exec("python Speech2.py");
echo $k;
echo ">";
echo $r;
?>
