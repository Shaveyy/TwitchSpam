import random
import json
import requests

def GenStreamKey(title,game):
    oauth = open("accounts.txt").read().split("\n")
    _oauth = random.choice(oauth).split(":")[1]

    headers = {
        'Accept': 'application/vnd.twitchtv.v5+json',
        'Client-ID': 'kimne78kx3ncx6brgo4mv6wki5h1ko',
        'Authorization': 'OAuth ' + _oauth,
    }

    response = requests.get('https://api.twitch.tv/kraken/channel', headers=headers)
    _json = json.loads(response.text)
    #print(json.loads(response.text))
    print(json.loads(response.text)['stream_key'])
    print(json.loads(response.text)['display_name'])
    stream_key = json.loads(response.text)['stream_key']
    display_name = json.loads(response.text)['display_name']
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

    response = requests.put('https://api.twitch.tv/kraken/channels/' + _json['_id'], headers=headers, data=data)
    return stream_key,display_name