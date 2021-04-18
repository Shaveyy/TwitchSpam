import discord
from twitchspam.bot import Bot
import time
import random
import requests
import json
import os
import urllib.request
import threading
import twitchspam.streamkeygen as skey
import subprocess
import socket
import re
import logger
import os
import sys
import twitchspam.follow as follow
import glob
import youtube_dl

def channelbyusername(channel):
    url = "https://api.twitch.tv/kraken/users?login=" + channel
    payload = {}
    headers = {
    'Accept': 'application/vnd.twitchtv.v5+json',
    'Client-Id': 'b31o4btkqth5bzbvr9ub2ovr79umhh'
    }
    response = requests.request("GET",url,headers=headers,data=payload)
    json_data = json.loads(response.text)
    print(response.text)
    return (json_data['users'][0]['_id'])

def test_oauth(oauth):
    if(":" in oauth):
        oauth = oauth.split(":")[1]
    headers = {
        'Accept': 'application/vnd.twitchtv.v5+json',
        'Authorization': 'OAuth ' + oauth,
        'Client-ID': 'gp762nuuoqcoxypju8c569th9wz7q5',
    }

    response = requests.get('https://api.twitch.tv/kraken', headers=headers)
    isvalid = bool(json.loads(response.text)['token']['valid'])
    channelid = channelbyusername("test")

    return isvalid


# gives the GLHF badge to an account of your choice
def GLHF(oauth):
    headers = {
        'authority': 'anykey.org',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'sec-fetch-site': 'none',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-user': '?1',
        'sec-fetch-dest': 'document',
        'accept-language': 'en-US,en;q=0.9',
    }

    params = (
        ('code', oauth), # pass the oauth
        ('scope', 'user_read'),
        ('state', 'XON1DQP7'),
    )


    response = requests.get('https://anykey.org/pledge', headers=headers, params=params)
    return response

def streamthread(stream_key,video_file):
    # TODO make this a bit safer 
    os.system('bash -c "/usr/bin/ffmpeg -re -i \'' + video_file + '\' -vcodec libx264 -profile:v main -preset:v medium -r 30 -g 60 -keyint_min 60 -sc_threshold 0 -b:v 2500k -maxrate 2500k -bufsize 2500k -sws_flags lanczos+accurate_rnd -b:a 96k -ar 48000 -ac 2 -f flv rtmp://live.twitch.tv/app/' + stream_key + '"')
    return

def start_stream(url,filename,stream_key):
    if not os.path.exists('videos'):
        os.makedirs('videos')

    ydl_opts = {
        "outtmpl": f"{sys.path[0]}/videos/{filename}.%(ext)s"
    }
    
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
    #os.system(f"/usr/bin/youtube-dl -f mp4 {url}")
    files = glob.glob(f"{sys.path[0]}/videos/{filename}.*")
    print(files)
    filename = files[0]

    t1 = threading.Thread(target=streamthread,args=(stream_key,filename))
    t1.daemon = True
    t1.start()
