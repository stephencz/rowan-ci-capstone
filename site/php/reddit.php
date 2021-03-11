<?php

function get_game_posts($id) {
    $connection = connect();

    $query = "SELECT * FROM game_posts WHERE game_id = $id";
    $result = $connection->query($query);

    $post_ids = [];

    if($result->num_rows > 0) {
        while($rows = $result->fetch_assoc()) {
            array_push($post_ids, $rows['post_id']);
        }

        return get_post_data($post_ids);
    }
    else {
        echo "NO RESULT";
    }

    close_connection($connection);
}

function get_post_data($ids) {
    $posts = [];

    foreach($ids as $value) {
        $connection = connect();

        $query = "SELECT * FROM reddit WHERE post_id = $value";
        $result = $connection->query($query);

        if($result->num_rows > 0) {
            while($rows = $result->fetch_assoc()) {
                array_push($posts, $rows);
            }
        }
        else {
            echo "NO RESULT";
        }

        close_connection($connection);
    }

    return $posts;
}

function render_posts($id) {
    $post_links = get_game_posts($id);
	echo '<ul class="game-reddit-list">';
    foreach($post_links as $value) {
        echo '<li>https://www.reddit.com' . $value['post_permalink'] . '</li>';
    }
	echo '</ul>';
}

?>