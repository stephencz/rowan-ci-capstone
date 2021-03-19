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
    <?php require('php/youtube.php'); ?>

    <?php render_videos(1); ?>

</body>
</html>