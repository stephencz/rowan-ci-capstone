"""
This script retrieve data from the IGDB API for use in 
my Rowan University Capstone Project.
@author Stephen Czekalski
@date 2/8/2021
"""

import json, requests

# The base url for the IGDB api
BASE_API = "https://api.igdb.com/v4"

# The client id for my IGDB application.
CLIENT_ID = ""

# The client secret for my IGDB application.
CLIENT_SECRET = ""

# The type of token I want.
GRANT_TYPE = "client_credentials"

"""
Gets a IGDB token for use with IGDB API.
@param client_id The client id of the IGDB application.
@param client_Secert The client secret for the GIDB application.
@param grant_type The type of token I want
"""
def get_igdb_token(client_id, client_secret, grant_type):
    url = "https://id.twitch.tv/oauth2/token?"
    url += "client_id=" + client_id
    url += "&client_secret=" + client_secret
    url += "&grant_type=" + grant_type

    req = requests.post(url)
    return json.loads(req.text)

"""
Makes an API request and retrieves the reponse.
@param token Our access token retrived using get_igdb_token(...)
@param end_point The API end_point to request data from
@param fields The fields we want from the data.
"""
def get_igdb_data(token, end_point, fields):
    bearer = 'Bearer ' + str(token['access_token'])
    return requests.post(BASE_API + end_point, headers={'Client-ID': CLIENT_ID, 'Authorization': bearer, 'Accept': 'application/json'}, data=fields)

"""
Gets the important data for games with a high total rating and a high rating count.
@param token Our access token retrieved using get_igdb_token(...)
"""
def get_best_in_genre(token):
    games = get_igdb_data(token, "/games", 'fields name,slug,summary,genres.name,involved_companies.company.name,involved_companies.company.websites.url, \
                                            age_ratings.category,age_ratings.rating,platforms.name,release_dates.date,total_rating,total_rating_count, \
                                            cover.url,cover.height,cover.width; \
                                            where total_rating < 100 & total_rating > 80 & rating_count > 100; \
                                            sort rating desc; limit 500;')
    return games

def run():

    # Ask the user if they want to retrieve fresh data from the API.
    if input('Would you like to retrieve fresh IGDB Data? (Y/N)') == 'Y':
        token = get_igdb_token(CLIENT_ID, CLIENT_SECRET, GRANT_TYPE)
        best = get_best_in_genre(token)

        with open('igdb-data.json', 'w') as file:
            file.write(best.text)

    # Restructures and reformats JSON data from API into a more usable structure.
    with open('igdb-data.json', 'r') as file:   
        data = json.loads(file.read())
        formatted_data = []

        with open('formatted-data.json', 'w') as formattedFile:
            for value in data:
                tree = {}
                tree['igbd-id'] = value['id']
                tree['name'] = value['name']
                tree['slug'] = value['slug']
                tree['summary'] = value['summary']
                tree['cover'] = value['cover']['url']
                tree['release_date'] = value['release_dates'][0]['date']
                tree['total_rating'] = value['total_rating']
                tree['total_rating_count'] = value['total_rating_count']
                
                tree['platforms'] = []
                for platform in value['platforms']:
                    tree['platforms'].append(platform['name'])

                if "age_ratings" in value:
                    for rating in value['age_ratings']:
                        if rating['category'] == 1:
                            tree['esrb-rating'] = rating['rating']
                        else:
                            tree['pegi-rating'] = rating['rating']

                tree['companies'] = []
                for company in value['involved_companies']:
                    tree['companies'].append(company['company']['name'])

                formatted_data.append(tree)

            # Sort reformatted data by each game's total rating and save.
            sorted_data = sorted(formatted_data, key=lambda k: k['total_rating'], reverse=True)
            json.dump(sorted_data, formattedFile, sort_keys=True, indent=4)


    with open('formatted-data.json', 'r') as formattedFile:
        data = json.loads(formattedFile.read())
        trimmed_data = []
        with open('final-igdb-data.json', 'w') as trimmedFile:
            for i in range(50):
                trimmed_data.append(data[i])
                print(data[i]['name'])

            json.dump(trimmed_data, trimmedFile, sort_keys=True, indent=4)

            
if __name__ == "__main__":
    run()