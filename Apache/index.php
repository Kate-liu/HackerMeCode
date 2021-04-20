<?php

if (isset($_FILES['file'])) {
    $name = basename($_POST['name']);
    $ext = pathinfo($name, PATHINFO_EXTENSION);
    if (in_array($ext, ['php', 'php3', 'php4', 'php5', 'phtml', 'pht'])) {
        exit('bad file');
    }
    move_uploaded_file($_FILES['file']['tmp_name'], './' . $name);
}
?>

<form action="index.php" method="post" enctype="multipart/form-data">
    <input type="file" name="file">
    <input type="text" name="name">
    <input type="submit" value="submit">
</form>