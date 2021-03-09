import json, sys, math
import mariadb

with open('../json/bing-data.json', 'r') as file:

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
        CREATE TABLE images(                        \
        image_id INT NOT NULL AUTO_INCREMENT,       \
        image_game_name VARCHAR(255) NOT NULL,      \
        image_url VARCHAR(256) NOT NULL,            \
        PRIMARY KEY (image_id)                      \
        );")

    # Create mapping table
    cursor.execute("                                        \
        CREATE TABLE game_images(                           \
        game_image_id INT NOT NULL AUTO_INCREMENT,          \
        game_id INT NOT NULL REFERENCES games(game_id),     \
        image_id INT NOT NULL REFERENCES images(image_id),  \
        PRIMARY KEY (game_image_id)                         \
        );")

    connection.commit()

    # Insert video data into table
    for image in data:

        image_game_name = image['name']
        image_urls = image['topFiveImages']

        for url in image_urls:

            query = "INSERT INTO images          \
                    (image_game_name, image_url) \
                    value (?, ?)"

            cursor.execute(query, (image_game_name, url))
    
    connection.commit()

    # Insert data into mapping table
    counter = 1
    for game in data:
        for image in game['topFiveImages']:
            query = "INSERT INTO game_images (game_id, image_id) value (?, ?)"
            cursor.execute(query, (int(math.ceil(counter / 5)), counter))

            counter = counter + 1    

    connection.commit()
