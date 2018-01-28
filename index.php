<?php 
echo "This is the first application";
$r=exec("python wer.py");
echo '<br>';
$k=exec("python face.py");
$p=exec("python Speech.py");
echo $p;
echo ">";
echo $r;
?>
