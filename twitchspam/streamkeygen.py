import random
import json
import requests
import config.config as config

def GenStreamKey(title,game):
    oauth = open(config.streamoauthsfile).read().split("\n")
    _token = random.choice(oauth).split(":")[0]
    _oauth = random.choice(oauth).split(":")[2]
    
    headers = {
        'Authorization': 'OAuth ' + _oauth,
    }

    response = requests.get('https://id.twitch.tv/oauth2/validate', headers=headers)
    
    user_id = json.loads(response.text)['user_id']
    display_name = json.loads(response.text)['login'] 

    headers = {
        'Client-ID': 'kimne78kx3ncx6brgo4mv6wki5h1ko',
        'Authorization': 'Bearer ' + _oauth,
    }

    response = requests.get('https://api.twitch.tv/helix/streams/key?broadcaster_id=' + user_id, headers=headers)

    print(response.text)
    print(json.loads(response.text)['data'][0]['stream_key'])
    stream_key = json.loads(response.text)['data'][0]['stream_key']
    headers = {
        'Client-ID': 'uo6dggojyb8d6soh92zknwmi5ej1q2',
        'Accept': 'application/vnd.twitchtv.v5+json',
        'Authorization': 'OAuth ' + _oauth,
    }

    data = {
        'channel[status]': title,
        'channel[game]': game,
        'channel[channel_feed_enabled]': 'false'
    }

    response = requests.put('https://api.twitch.tv/kraken/channels/' + user_id, headers=headers, data=data)
    return stream_key,display_name
