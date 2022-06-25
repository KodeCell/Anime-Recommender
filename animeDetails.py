import requests

def get_anime_data(anime_id):
    response = requests.get(f'https://api.jikan.moe/v4/anime/{anime_id}/full')
    data = response.json()
    mal_link = data['data']['url']
    posters = data['data']['images']['webp']['image_url']
    type = data['data']['type']
    episodes = data['data']['episodes']
    status = data['data']['status']
    new =  data['data']['genres']
    genres = [data['name'] for data in new]
    summary = data['data']['synopsis']


    return posters,type,episodes,status,",".join(genres),mal_link,summary