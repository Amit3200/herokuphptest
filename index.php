<?php 
$rr=exec('python wer.py');
echo "This is the first application\n";
echo $rr;
exec('python FaceRecognition1.py');
echo "This is the first application\n";
?>
