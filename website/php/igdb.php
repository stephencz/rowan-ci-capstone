<?php
 
/**
 * Gets data from the games table based on the game id.
 * @param id The id of the game to retrieve from the database.
 */
function get_game($id) {
    $connection = connect();

    $query = "SELECT * FROM games WHERE game_id = $id";
    $result = $connection->query($query);

    if($result->num_rows > 0) {
		close_connection($connection);
        return $result->fetch_assoc();
    }
    else {
        echo "NO RESULT";
    }

    close_connection($connection);
}

/**
 * Gets a piece of data from a game based on its id.
 * @param id The id of the game to get data from.
 * @param key The column name for the exact data to get.
 */
function get_game_data($id, $key) {
    return get_game($id)[$key];
}

function get_game_platforms($id) {
    $connection = connect();

    $platform_ids = [];

    $query = "SELECT * FROM game_platforms WHERE game_id = $id";
    $result = $connection->query($query);

    if($result->num_rows > 0) {
        while($rows = $result->fetch_assoc()) {
            array_push($platform_ids, $rows['platform_id']);
        }

        return get_platform_names($platform_ids);
    }
    else {
        echo "NO RESULT";
    }

    close_connection($connection);
}

function get_platform_names($ids) {
    $names = [];

    foreach($ids as $value) {
        $connection = connect();

        $query = "SELECT platform_name FROM platforms WHERE platform_id = $value";
        $result = $connection->query($query);

        if($result->num_rows > 0) {
            while($rows = $result->fetch_assoc()) {
                array_push($names, $rows['platform_name']);
            }

        }
        else {
            echo "NO RESULT";
        }

        close_connection($connection);
    }

    return $names;
}

function get_game_companies($id) {
    $connection = connect();

    $company_ids = [];

    $query = "SELECT * FROM game_companies WHERE game_id = $id";
    $result = $connection->query($query);

    if($result->num_rows > 0) {
        while($rows = $result->fetch_assoc()) {
            array_push($company_ids, $rows['company_id']);
        }

        return get_company_names($company_ids);
    }
    else {
        echo "NO RESULT";
    }

    close_connection($connection);
}

function get_company_names($ids) {
    $names = [];

    foreach($ids as $value) {
        $connection = connect();

        $query = "SELECT company_name FROM companies WHERE company_id = $value";
        $result = $connection->query($query);

        if($result->num_rows > 0) {
            while($rows = $result->fetch_assoc()) {
                array_push($names, $rows['company_name']);
            }

        }
        else {
            echo "NO RESULT";
        }

        close_connection($connection);
    }

    return $names;
}

/**
 * Renders all the games in the games table in HTML.
 */
function render_game_list() {
    echo '<div class="game-list">';
    for($i = 1; $i <= 50; $i++) {
        
        $game = get_game($i);

        echo '<div class="game-list-item">';
        echo '<div class="game-rank">' . $i . '</div>';
        echo '<div class="game-cover"><img src="' . $game['game_cover_url'] . '"></div>'; 
        echo '<div class="game-title"><a href="game.php?game_id=' . $i . '">' . $game['game_name'] . '</a></div>';
        echo '<div class="game-rating">' . $game['game_rating'] . '</div>';
        echo '</div>';

    }
    echo '</div>';
}

/**
 * Render the games ESRB and PEGI age ratings in HTML.
 * @param id The id of the game to get the age ratings of.
 */
function render_game_age_rating($id) {
    $esrb = get_game_data($id, "game_esrb_rating");
    $pegi = get_game_data($id, "game_pegi_rating");

    switch($pegi) {
        case 1: echo '<div class="game-pegi-3"></div>'; break;
        case 2: echo '<div class="game-pegi-7"></div>'; break;
        case 3: echo '<div class="game-pegi-12"></div>'; break;
        case 4: echo '<div class="game-pegi-16"></div>'; break;
        case 5: echo '<div class="game-pegi-18"></div>'; break;
    }

    switch($esrb) {
        case 6: echo '<div class="game-esrb-rp"></div>'; break;
        case 7: echo '<div class="game-esrb-ec"></div>'; break;
        case 8: echo '<div class="game-esrb-e"></div>'; break;
        case 9: echo '<div class="game-esrb-e10"></div>'; break;
        case 10: echo '<div class="game-esrb-t"></div>'; break;
        case 11: echo '<div class="game-esrb-m"></div>'; break;
        case 12: echo '<div class="game-esrb-ao"></div>'; break;
    }
}

function render_game_age_rating_text_pegi($id) {
    $pegi = get_game_data($id, "game_pegi_rating");

    switch($pegi) {
        case 1: echo 'Age 3'; break;
        case 2: echo 'Age 7'; break;
        case 3: echo 'Age 12'; break;
        case 4: echo 'Age 16'; break;
        case 5: echo 'Age 18'; break;
    }
}

function render_game_age_rating_text_esrb($id) {
    $esrb = get_game_data($id, "game_esrb_rating");

    switch($esrb) {
        case 6: echo 'Rating Pending'; break;
        case 7: echo 'Early Childhood'; break;
        case 8: echo 'Everyone'; break;
        case 9: echo 'Everyone Ten Plus'; break;
        case 10: echo 'Teen'; break;
        case 11: echo 'Mature'; break;
        case 12: echo 'Adults Only'; break;
    }
}

function render_platforms($id) {
    $platforms =  get_game_platforms($id);
    echo '<ul class="game-platforms">';
    foreach($platforms as $value) {
        echo '<li>' . $value . '</li>';
    }
    echo '</ul>';
}

function render_companies($id) {
    $companies = get_game_companies($id);
    echo '<ul class="game-companies">';
    foreach($companies as $value) {
        echo '<li>' . $value . '</li>';
    }
    echo '</ul>';
}
?>