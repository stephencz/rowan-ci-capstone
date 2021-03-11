<?php

function get_game_videos($id) {
    $connection = connect();

    $query = "SELECT * FROM game_videos WHERE game_id = $id";
    $result = $connection->query($query);

    $video_ids = [];

    if($result->num_rows > 0) {
        while($rows = $result->fetch_assoc()) {
            array_push($video_ids, $rows['video_id']);
        }

        return get_video_links($video_ids);
    }
    else {
        echo "NO RESULT";
    }

    close_connection($connection);
}

function get_video_links($ids) {
    $links = [];

    foreach($ids as $value) {
        $connection = connect();

        $query = "SELECT * FROM youtube WHERE video_id = $value";
        $result = $connection->query($query);

        if($result->num_rows > 0) {
            while($rows = $result->fetch_assoc()) {
                array_push($links, 'https://www.youtube.com/embed/' . $rows['video_link_id']);
            }
        }
        else {
            echo "NO RESULT";
        }

        close_connection($connection);
    }

    return $links;
}

function render_videos($id) {
    $video_links = get_game_videos($id);

	echo '<div class="row">';
	echo '<div class="col-lg-12">';
	echo '<iframe width="100%" height="515" src="' . $video_links[0] . '" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>';
	echo '</div>';
	echo '</div>';
	
	echo '<div class="row">';
	echo '<div class="col-xl-6">';
	echo '<iframe width="100%" height="315" src="' . $video_links[1] . '" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>';
	echo '</div>';
	
	echo '<div class="col-xl-6">';
	echo '<iframe width="100%" height="315" src="' . $video_links[2] . '" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>';
	echo '</div>';
	echo '</div>';
	
	echo '<div class="row">';
	echo '<div class="col-xl-6">';
	echo '<iframe width="100%" height="315" src="' . $video_links[3] . '" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>';
	echo '</div>';
	
	echo '<div class="col-xl-6">';
	echo '<iframe width="100%" height="315" src="' . $video_links[4] . '" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>';
	echo '</div>';
	echo '</div>';
}

?>