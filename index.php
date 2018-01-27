<?php 
$rr=exec('python wer.py');
echo "This is the first application\n";
echo $rr;
$ew=shell_exec('python face.py');
echo "\nThis is the first application\n";
echo "\n$ew";
?>
