<!DOCTYPE html>
<html>
<head>
</head>
<body>

    <?php
    ini_set('display_errors', 1);
    ini_set('display_startup_errors', 1);
    error_reporting(E_ALL);?>

    <?php require('php/connect.php'); ?>
    <?php require('php/reddit.php'); ?>

    <?php render_posts(1); ?>

</body>
</html>