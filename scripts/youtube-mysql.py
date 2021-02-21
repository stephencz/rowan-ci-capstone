import json, sys
import mariadb

with open('youtube-data.json', 'r') as file:

    connection = mariadb.connect(
        user="root",
        password="",
        host="localhost",
        database="capstone"
    )

    data = json.loads(file.read())
    cursor = connection.cursor()

    # Create youtube video table
    cursor.execute("                                \
        CREATE TABLE youtube(                       \
        video_id INT NOT NULL AUTO_INCREMENT,       \
        video_game_name VARCHAR(255) NOT NULL,      \
        video_title VARCHAR(256) NOT NULL,          \
        video_description TEXT NOT NULL,            \
        video_link_id VARCHAR(255) NOT NULL,        \
        PRIMARY KEY (video_id)                      \
        );")

    connection.commit()

    # Insert video data into table
    for video in data:

        video_game_name = video['game-id']
        video_title = video['title']
        video_description = video['description']
        video_link_id = video['video-id']

        query = "INSERT INTO youtube                                              \
                 (video_game_name, video_title, video_description, video_link_id) \
                 value (?, ?, ? ,?)"

        cursor.execute(query, (video_game_name, video_title, video_description, video_link_id))
    
    connection.commit()
