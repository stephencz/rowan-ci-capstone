import json, sys
import mariadb

def run():
    # Open our JSON data file and load data into a python dictionary
    with open('igdb-data.json', 'r', encoding="utf-8",) as file:
        data = json.loads(file.read())
            
        # Create our connection to our database
        try:
            connection = mariadb.connect(
                user="root",
                password="",
                host="localhost",
                database="capstone"
            )

        except mariadb.Error as e:
            print(e)
            sys.exit(1)

        # Get cursor
        cursor = connection.cursor()

        # Create the five tables needed to store the data
        if input("Would you like to create the tables? (Y/N) ") == "Y":
            create_games_table(cursor)
            create_platforms_table(cursor)
            create_game_platforms_table(cursor)
            create_companies_table(cursor)
            create_game_companies_table(cursor)
            connection.commit()

        # Insert data into tables
        insert_game_data(cursor, data)
        insert_platform_data(cursor, data)
        insert_company_data(cursor, data)
        connection.commit()

        # Map game_platform and game_companies tables with respective primary keys
        map_game_platforms_tables(cursor, data)
        map_game_companies_tables(cursor, data)

        connection.commit()

        connection.close()

"""
Creates a MySQL table to game information in such as game name, summary,
release date, etc.
@param cusor The MariaDB cursor.
"""
def create_games_table(cursor):
    cursor.execute("                                \
        CREATE TABLE games(                         \
        game_id INT NOT NULL AUTO_INCREMENT,        \
        game_name VARCHAR(256) NOT NULL,            \
        game_summary TEXT NOT NULL,                 \
        game_release INT(11) NOT NULL,              \
        game_rating FLOAT NOT NULL,                 \
        game_rating_count INT NOT NULL,             \
        game_esrb_rating INT NOT NULL,              \
        game_pegi_rating INT NOT NULL,              \
        game_cover_url TEXT NOT NULL,               \
        PRIMARY KEY (game_id)                       \
        );")

"""
Creates a MySQL table with information about the various game platforms.
@param cusor The MariaDB cursor.
"""
def create_platforms_table(cursor):
    cursor.execute("                                \
        CREATE TABLE platforms(                     \
        platform_id INT NOT NULL AUTO_INCREMENT,    \
        platform_name VARCHAR(256) NOT NULL,        \
        PRIMARY KEY(platform_id)                    \
        );")

"""
Creates a MySQL table with information of game companies/publishers/developers.
@param cusor The MariaDB cursor.
"""
def create_companies_table(cursor):
    cursor.execute("                                \
        CREATE TABLE companies(                     \
        company_id INT NOT NULL AUTO_INCREMENT,     \
        company_name VARCHAR(256) NOT NULL,         \
        PRIMARY KEY(company_id)                    \
        );")

"""
Creates a MySQL table to mapping games to their available platforms.
@param cusor The MariaDB cursor.
"""
def create_game_platforms_table(cursor):
    cursor.execute("                                                \
        CREATE TABLE game_platforms(                                \
        game_platform_id INT NOT NULL AUTO_INCREMENT,               \
        game_id INT NOT NULL REFERENCES games(game_id),             \
        platform_id INT NOT NULL REFERENCES platforms(platform_id), \
        PRIMARY KEY(game_platform_id)                               \
        );")                                                        

"""
Creates a MySQL table to mapping games to their companies/publishers/developers
@param cusor The MariaDB cursor.
"""
def create_game_companies_table(cursor):
    cursor.execute("                                                \
        CREATE TABLE game_companies(                                \
        game_company_id INT NOT NULL AUTO_INCREMENT,                \
        game_id INT NOT NULL REFERENCES games(game_id),             \
        company_id INT NOT NULL REFERENCES companies(company_id),   \
        PRIMARY KEY(game_company_id)                                \
        );")

"""
Inserts game data, such as its name, summary, and ratings, into the games table.
@param cursor The MariaDB cursor.
@param data The JSON data we are inserting.
"""
def insert_game_data(cursor, data):
    for game in data:

        game_name = str(game['name']).strip()
        game_summary = str(game['summary']).strip()
        game_release = str(game['release_date']).strip()
        game_rating = str(game['total_rating']).strip()
        game_rating_count = str(game['total_rating_count']).strip()
        game_cover_url = str(game['cover']).strip()

        if 'esrb-rating' in game:
            game_esrb_rating = str(game['esrb-rating']).strip()
        else:
            game_esrb_rating = str(0)

        if 'pegi-rating' in game:
            game_pegi_rating = str(game['pegi-rating']).strip()
        else:
            game_pegi_rating = str(0)

        query = 'INSERT INTO games (game_name, game_summary, game_release, game_rating,  \
                game_rating_count, game_esrb_rating, game_pegi_rating, game_cover_url)   \
                value (?, ?, ?, ?, ?, ?, ?, ?);'
        cursor.execute(query, (game_name, game_summary, game_release, game_rating, game_rating_count, game_esrb_rating, game_pegi_rating, game_cover_url))                                                                   
            
"""
Inserts the gaming platforms data into the platforms table.
@param cursor The MariaDB cursor.
@param data The JSON data we are inserting.
""" 
def insert_platform_data(cursor, data):
    platforms = []
    for game in data:
        for platform in game['platforms']:
            platforms.append(platform)    

    unique_platforms = set(platforms)
    for platform in unique_platforms:
        query = 'INSERT INTO platforms (platform_name) value ("' + platform + '");'
        cursor.execute(query)

"""
Inserts the game developement companies into the companies table.
@param cursor The MariaDB cursor.
@param data The JSON data we are inserting.
"""
def insert_company_data(cursor, data):
    companies = []
    for game in data:
        for company in game['companies']:
            companies.append(company)

    unique_companies = set(companies)
    for company in unique_companies:
        query = 'INSERT INTO companies (company_name) value ("' + company + '");'
        cursor.execute(query)

"""
Maps games to the platforms they can run on for easy lookup in the game_platforms table.
@param cursor The MariaDB cursor.
@param data The JSON data we are inserting.
"""
def map_game_platforms_tables(cursor, data):
    for i in range(0, 50):
        platform_ids = []
        for platform in data[i]['platforms']:
            cursor.execute('SELECT platform_id FROM platforms WHERE platform_name = "' + platform + '";')
            for (platform_id) in cursor:
                platform_ids.append(platform_id[0])
    
        for platform_id in platform_ids:
            cursor.execute('INSERT INTO game_platforms (game_id, platform_id) VALUE (?, ?)', (i + 1, platform_id))

"""
Maps games to their developers for easy lookup in the game_companies table.
@param cursor The MariaDB cursor.
@param data The JSON data we are inserting.
"""
def map_game_companies_tables(cursor, data):
    for i in range(0, 50):
        company_ids = []
        for company in data[i]['companies']:
            cursor.execute('SELECT company_id FROM companies WHERE company_name = "' + company + '";')
            for (company_id) in cursor:
                company_ids.append(company_id[0])

        for company_id in company_ids:
            cursor.execute('INSERT INTO game_companies (game_id, company_id) VALUE (?, ?)', (i + 1, company_id))

if __name__ == "__main__":
    run()