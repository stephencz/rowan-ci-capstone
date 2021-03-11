import json, sys
import mariadb


with open('gameResults.json', 'r') as file:
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
        CREATE TABLE bing(                       \
        image_id INT NOT NULL AUTO_INCREMENT,       \
        image_name VARCHAR(255) NOT NULL,      \
        image_total INT NOT NULL,          \
        image_link VARCHAR(255) NOT NULL,        \
        PRIMARY KEY (image_id)                      \
        );")

    connection.commit()

    # Insert video data into table
    for image in data:
        image_name = image['name']
        image_total = image['totalImages']
        image_links = image['topFiveImages']

        for link in image_links:
            query = "INSERT INTO bing                          \
                    (image_name, image_total, image_link) \
                    value (?, ?, ?)"

            cursor.execute(query, (image_name, image_total, link))

    connection.commit()