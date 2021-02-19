import json
import praw

games = [
    "Super Mario World",
    "The Legend of Zelda: A Link to the Past",
    "Super Metroid",
    "God of War",
    "The Last of Us Remastered",
    "Final Fantasy VI",
    "Persona 4 Golden",
    "The Legend of Zelda: Breath of the Wild",
    "Metal Gear Solid 3: Subsistence",
    "Super Mario World 2: Yoshi's Island",
    "Super Smash Bros. Melee",
    "The Last of Us Part II",
    "Mass Effect 2",
    "Metroid Prime",
    "Persona 5",
    "The Witcher 3: Wild Hunt",
    "Unreal Tournament",
    "Red Dead Redemption 2",
    "Grand Theft Auto V",
    "Super Mario Galaxy",
    "Super Mario Odyssey",
    "Hades",
    "The Last of Us",
    "Super Mario Galaxy 2",
    "Sid Meier's Civilization",
    "Uncharted 4: A Thief's End",
    "Disco Elysium",
    "Chrono Trigger",
    "Uncharted 2: Among Thieves",
    "Undertale",
    "Star Wars: Knights of the Old Republic",
    "The Legend of Zelda: Ocarina of Time",
    "Portal 2",
    "The Elder Scrolls V: Skyrim",
    "Return of the Obra Dinn",
    "EarthBound",
    "Castlevania: Symphony of the Night",
    "Grand Theft Auto: San Andreas",
    "Paper Mario: The Thousand-Year Door",
    "Hollow Knight",
    "Bloodborne",
    "Oddworld: Abe's Oddysee",
    "The Binding of Isaac: Rebirth",
    "Metroid: Zero Mission",
    "God of War III",
    "The Legend of Zelda: Twilight Princess",
    "Silent Hill 2",
    "Bayonetta 2",
    "Ghost of Tsushima",
    "Day of the Tentacle"
]

reddit = praw.Reddit(client_id="",
                     client_secret="",
                     password="",
                     user_agent="",
                     username="")

reddit_posts = []

for game in games:

    posts = reddit.subreddit("gaming").search(game, sort="top", limit=5)

    for post in posts:
        data = {}

        data['game-name'] = game
        data['title'] = post.title
        data['author'] = post.author.name
        data['score'] = post.score
        data['permalink'] = post.permalink

        reddit_posts.append(data)

with open('reddit-data.json', 'w') as file:
    json.dump(reddit_posts, file, sort_keys=True, indent=4)
