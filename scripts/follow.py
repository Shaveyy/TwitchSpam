import requests
import threading
import json
import config.config as config

def channelbyusername(channel):
    url = "https://api.twitch.tv/kraken/users?login=" + channel
    payload = {}
    headers = {
    'Accept': 'application/vnd.twitchtv.v5+json',
    'Client-Id': 'kimne78kx3ncx6brgo4mv6wki5h1ko'
    }
    response = requests.request("GET",url,headers=headers,data=payload)
    json_data = json.loads(response.text)
    return (json_data['users'][0]['_id'])

def followchannel(f,channel_id,i):
    token = f[i].split(":")[1]
    headers = {
        'Connection': 'keep-alive',
        'Authorization': 'OAuth ' + token,
        'Accept-Language': 'en-US',
        'Client-Id': 'kimne78kx3ncx6brgo4mv6wki5h1ko',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36',
        'X-Device-Id': 'b542c99d713d05b2',
        'Content-Type': 'text/plain;charset=UTF-8',
        'Accept': '*/*',
        'Origin': 'https://www.twitch.tv',
        'Sec-Fetch-Site': 'same-site',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Dest': 'empty',
        'Referer': 'https://www.twitch.tv/abracadabra',
    }

    data = '[{"operationName":"FollowButton_FollowUser","variables":{"input":{"disableNotifications":false,"targetID":"' + channel_id + '"}},"extensions":{"persistedQuery":{"version":1,"sha256Hash":"3efee1acda90efdff9fef6e6b4a29213be3ee490781c5b54469717b6131ffdfe"}}}]'

    requests.post('https://gql.twitch.tv/gql', headers=headers, data=data)
    
def start_following(channel,amount):
    f = open(config.oauthsfile).read().split("\n")
    if(not f):
        print("File could not open")
    chan_id = channelbyusername(channel)
    for i in range(amount):
        # Added threading to make it faster
        if(i > len(f)):
            return
        
        x = threading.Thread(target=followchannel, args=(f,chan_id,i))
        x.start()