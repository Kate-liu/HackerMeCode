<?php
// 从用户目录中删除指定的文件
$username = $_POST['user_submitted_name'];
$userfile = $_POST['user_submitted_filename'];
$homedir = "/home/$username";

unlink("$homedir/$userfile");
echo "The file has been deleted!";

?>

