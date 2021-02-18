import time, json
from googleapiclient.discovery import build

# This is list/array of the top fifty highest rated video games
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

# The key you generated while getting access to the API goes here
api_key = ""

# This creates our connection to the API
youtube = build('youtube', 'v3', developerKey=api_key)

# Our data will be stored in this list
videos = []

# Now we run a for-each loop over the top fifty highest rated games
# and get the data for each of them
for game in games:

    # Here we build the YouTube query/search request
    query_string  = game + " gameplay"
    request = youtube.search().list(
        q=query_string,
        part="id,snippet",
        type="video"
        )
        
    # And now we execute the request, retrieving the data we need
    response = request.execute()

    # We run another for-each loop over the items returned in the response
    # pull out the data we need, and store it.
    for item in response['items']:
        video = {}

        video['game-id'] = game
        video['title'] = item['snippet']['title']
        video['description'] = item['snippet']['description']
        video['video-id'] = item['id']['videoId']

        videos.append(video)

    # The program sleeps for half a second so that we don't exceed
    # the APIs request per second quota.
    time.sleep(0.5)

# Finally we save the data we retrieved as a JSON file
with open('youtube-data.json', 'w') as file:
    json.dump(videos, file, sort_keys=True, indent=4)