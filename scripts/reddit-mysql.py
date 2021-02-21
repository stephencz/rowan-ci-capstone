import json, sys
import mariadb

with open('reddit-data.json', 'r') as file:

    connection = mariadb.connect(
        user="root",
        password="",
        host="localhost",
        database="capstone"
    )

    data = json.loads(file.read())
    cursor = connection.cursor()

    cursor.execute("                                \
        CREATE TABLE reddit(                        \
        post_id INT NOT NULL AUTO_INCREMENT,        \
        post_game VARCHAR(255) NOT NULL,            \
        post_author VARCHAR(256) NOT NULL,          \
        post_title VARCHAR(256) NOT NULL,           \
        post_permalink VARCHAR(255) NOT NULL,       \
        post_score INT(11) NOT NULL,                \
        PRIMARY KEY (post_id)                       \
        );")

    connection.commit()

    for post in data:

        post_game = post['game-name']
        post_author = post['author']
        post_title = post['title']
        post_permalink = post['permalink']
        post_score = post['score']

        query = "INSERT INTO reddit                                               \
                 (post_game, post_author, post_title, post_permalink, post_score) \
                 value (?, ?, ? , ?, ?)"

        cursor.execute(query, (post_game, post_author, post_title, post_permalink, post_score))
    
    connection.commit()
