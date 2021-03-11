<?php

function get_game_images($id) {
    $connection = connect();

    $query = "SELECT * FROM game_images WHERE game_id = $id";
    $result = $connection->query($query);

    $image_ids = [];

    if($result->num_rows > 0) {
        while($rows = $result->fetch_assoc()) {
            array_push($image_ids, $rows['image_id']);
        }

        return get_image_data($image_ids);
    }
    else {
        echo "NO RESULT";
    }

    close_connection($connection);
}

function get_image_data($ids) {
    $images = [];

    foreach($ids as $value) {
        $connection = connect();

        $query = "SELECT * FROM images WHERE image_id = $value";
        $result = $connection->query($query);

        if($result->num_rows > 0) {
            while($rows = $result->fetch_assoc()) {
                array_push($images, $rows);
            }
        }
        else {
            echo "NO RESULT";
        }

        close_connection($connection);
    }

    return $images;
}

function render_bing_images($id) {
    $images = get_game_images($id);
    foreach($images as $value) {
        echo '<img class="game-bing-image" src="' . $value['image_url'] . '">';
    }
}

?>