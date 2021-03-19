<!<!DOCTYPE html>
<html>
<head>

    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">

    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-BmbxuPwQa2lc/FVzBcNJ7UAyJxM6wuqIj61tLrc4wSX0szH/Ev+nYRRuWlolflfl" crossorigin="anonymous">
    <link href="css/styles.css" rel="stylesheet">
	<link href="css/youtube.css" rel="stylesheet">
	<link href="css/reddit.css" rel="stylesheet">
	<link href="css/bing.css" rel="stylesheet">

    <?php
    ini_set('display_errors', 1);
    ini_set('display_startup_errors', 1);
    error_reporting(E_ALL);?>

    <?php require('php/connect.php'); ?>
    <?php require('php/igdb.php'); ?>
	<?php require('php/youtube.php'); ?>
	<?php require('php/reddit.php'); ?>
	<?php require('php/bing.php'); ?>

    <title><?php echo get_game_data($_GET["game_id"], "game_name"); ?> - Top 50 Games</title>

</head>
<body>

    <div class="container">
        <?php include('includes/header.html'); ?>

        <div class="game-info-wrapper">
            <div class="row">

                <div class="col-md-8 offset-md-1">
                    <div class="game-info-body">
                        <div class="game-title">
                            <h1>
                                <span style="font-weight: 700;">#<?php echo $_GET["game_id"]; ?></span>
                                <?php echo get_game_data($_GET["game_id"], "game_name"); ?>
                            </h1>
                        </div>
                        <div class="game-summary"><?php echo get_game_data($_GET["game_id"], "game_summary"); ?></div>

                        <div class="row" style="margin-bottom: 2rem; border-bottom: 1px solid #e3e3e3;">
                            <div class="col-md-4" >

                                <div style="margin-bottom: 1rem;">
                                    <span class="label">Release Date: </span>
                                    <div class="game-date"><?php echo date('F j, Y', get_game_data($_GET["game_id"], "game_release")); ?></div>
                                </div>

                                <div style="margin-bottom: 1rem;">
                                    <span class="label">Platforms:</span>
                                    <?php render_platforms($_GET["game_id"]); ?>
                                </div>

                            </div>

                            <div class="col-md-4">
                                <div style="margin-bottom: 1rem;">
                                    <span class="label">Companies:</span>
                                    <?php render_companies($_GET["game_id"]); ?>
                                </div>
                            </div>

                            <div class="col-md-4">
                                <div style="margin-bottom: 1rem;">
                                    <span class="label">Average Rating:</span>
                                    <div class="game-average-rating"><?php echo get_game_data($_GET["game_id"], "game_rating"); ?></div>
                                </div>

                                <div style="margin-bottom: 1rem;">
                                    <span class="label">Total Rating:</span>
                                    <div class="game-total-rating"><?php echo get_game_data($_GET["game_id"], "game_rating_count"); ?></div>
                                </div>

                                <div style="margin-bottom: 1rem;">
                                    <span class="label">PEGI Rating:</span>
                                    <div class="game-total-rating"><?php echo render_game_age_rating_text_pegi($_GET["game_id"]); ?></div>
                                </div>

                                <div style="margin-bottom: 1rem;">
                                    <span class="label">ESRB Rating:</span>
                                    <div class="game-total-rating"><?php echo render_game_age_rating_text_esrb($_GET["game_id"]); ?></div>
                                </div>
                            </div>
                        </div>
						
						<div class="row">
							<div class="col-md-12">
								<div class="reddit-title">Reddit:</div>
								<?php render_posts($_GET["game_id"]); ?>
							</div>
						</div>
						
						<div style="margin-top: 2rem; margin-bottom: 2rem; border-bottom: 1px solid #e3e3e3;"></div>
	
						
						<div class="row">
							<div class="col-md-12">
								<?php render_videos($_GET["game_id"]); ?>
							</div>
						</div>
						
						
						<div style="margin-top: 2rem; margin-bottom: 2rem; border-bottom: 1px solid #e3e3e3;"></div>
						<div class="row">
							<div class="col-md-12">
							
								<?php render_bing_images($_GET["game_id"]); ?>
							</div>
						</div>
						
						<div style="margin-top: 2rem; margin-bottom: 2rem; border-bottom: 1px solid #e3e3e3;"></div>
						
			
                    </div>
                </div>

                <div class="col-md-2">
                    <div class="game-info-side">
                        <div class="game-cover"><img src="<?php echo get_game_data($_GET["game_id"], "game_cover_url"); ?>"></div>
                        <?php render_game_age_rating($_GET["game_id"]); ?>
                    </div>
                </div>
                
            </div>
        </div>

        <?php include('includes/games_footer.html'); ?>

    </div>

    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta2/dist/js/bootstrap.bundle.min.js" integrity="sha384-b5kHyXgcpbZJO/tY9Ul7kGkf1S0CWuKcCD38l8YkeH8z8QjE0GmW1gYU5S9FOnJ0" crossorigin="anonymous"></script>

</body>
</html>