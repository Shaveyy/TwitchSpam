import requests
import threading
import json
import config.config as config
import logger
import twitchspam.utils as utils

def followchannel(f,channel_id,i):
    clientid = f[i].split(":")[0]
    token = f[i].split(":")[2]
    headers = {
        'Connection': 'keep-alive',
        'Authorization': 'OAuth ' + token,
        'Accept-Language': 'en-US',
        'Client-Id': clientid,
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

def followchannel_test(oauth,channel_id):
    token = oauth
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

    response = requests.post('https://gql.twitch.tv/gql', headers=headers, data=data)
    print(response.text)
    errors = json.loads(response.text).get("error")
    return json is None

def start_following(channel,amount):
    f = open(config.oauthsfile).read().split("\n")
    if(not f):
        print("File could not be opened")
        logger.log("File could not be opened")
        return
    chan_id = utils.channelbyusername(channel)
    for i in range(amount):
        # Added threading to make it faster
        if(i >= len(f)):
            return

        x = threading.Thread(target=followchannel, args=(f,chan_id,i))
        x.start()
