import requests
import json
import threading
import config.config as config
import twitchspam.utils as utils

def reportchannel(channel_id,i):
    f = open("oauthlist.txt", "r").read().split("\n")
    clientid = f[i].split(":")[0]
    token = f[i].split(":")[2]
    headers = {
        'Connection': 'keep-alive',
        'Authorization': 'OAuth ' + token,
        'Accept-Language': 'en-US',
        'Client-Id': clientid,
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36',
        'X-Device-Id': 'b542c99d713d05b2',
        'Content-Type': 'text/plain;charset=UTF-8',
        'Accept': '*/*',
        'Origin': 'https://www.twitch.tv',
        'Sec-Fetch-Site': 'same-site',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Dest': 'empty',
        'Referer': 'https://www.twitch.tv/souljaboy',
    }

    data = '[{"operationName":"ReportUserModal_ReportUser","variables":{"input":{"description":"moderating\\n\\ndescription: He is allowing people to be racist in the chat","reason":"other","content":"USER_REPORT","contentID":"","extra":"","targetID":"'+ channel_id + '","wizardPath":["moderating"]}},"extensions":{"persistedQuery":{"version":1,"sha256Hash":"dd2b8f6a76ee54aff685c91537fd75814ffdc732a74d3ae4b8f2474deabf26fc"}}}]'

    response = requests.post('https://gql.twitch.tv/gql', headers=headers, data=data)
    print(response.text)

def start_reporting(channel,amount):
    # Hacky
    global files
    files = open(config.oauthsfile).read().split("\n")
    chan_id = utils.channelbyusername(channel)
    for i in range(amount): #len(files)
        if i > len(files):
            return
            
        x = threading.Thread(target=reportchannel, args=(chan_id,i))
        x.start()
