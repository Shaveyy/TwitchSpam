import discord
from scripts.bot import Bot
import time
import random
import requests
import json
import os
import urllib.request
import threading
import scripts.streamkeygen as skey
import subprocess
import socket
import re

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
    return isvalid

def encode_video(filename):
    import os
    os.system("/usr/bin/ffmpeg -i {0} -c:v libx264 -crf 19 -preset veryfast {1}.flv".format(filename,filename))
    os.system("/usr/bin/rm -rf {0}".format(filename))

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

def streamthread(stream_key,video_file=""):
    if(len(video_file) > 0):
        print(video_file)
        subprocess.call(['./stream', stream_key,video_file])    
        return

    subprocess.call(['./stream', stream_key,"video0.flv"])
    return

def start_stream(url,filename,stream_key):
    if "youtube" in url or "bitchute" in url:
        os.system("youtube-dl {0} -o {1}".format(url,filename))
        import glob
        files = glob.glob(filename + ".*")
        filename = files[0]
    else:
        urllib.request.urlretrieve(url, filename)
    encode_video(filename)
    filename += ".flv"
    t1 = threading.Thread(target=streamthread,args=(stream_key,filename))
    t1.daemon = True
    t1.start()