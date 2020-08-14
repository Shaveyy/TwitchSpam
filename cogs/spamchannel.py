import discord
from discord.ext import commands
import math
import threading
import time
import socket
from scripts.bot import Bot
import random
# Import followbot module
import re
import scripts.follow
import scripts.spintax
# discord.py calls groups of commands cogs
# cogs can also be handlers for different types of events
# and respond to changes in data as they happen

# setup
class SpamCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    def handle_channel_spam(self,channel,accounts,bot_message,nonam=False):
        followers=False
        sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        sock.connect(("irc.chat.twitch.tv" , 6667))
        sock.send("PASS oauth:qotvyqpnozfq9ku729076ofwfkv51x\r\n".encode())
        sock.send("NICK lolsecurity\r\n".encode())
        membership = "CAP REQ :twitch.tv/membership\r\n"
        commands = "CAP REQ :twitch.tv/commands twitch.tv/tags\r\n"
        sock.send(membership.encode())
        sock.send(commands.encode())
        time.sleep(1)
        sock.send("JOIN #{}\r\n".format(channel).encode())
        #print("ROOMSTATE #{}\r\n".format(channel).encode())
        #sock.send("ROOMSTATE #{}\r\n".format(channel).encode())
        try:
            while(1):
                data = sock.recv(1024)
                recvdata = data.decode('utf-8')
                #x = re.findall('^@.*?',recvdata)
                p = re.search("@(.*?);",recvdata)
                if p:
                    follow = recvdata.split(";")[8]
                    if follow != "followers-only=-1":
                        followers = True
                    break
        except: pass
        if(followers):
            scripts.follow.start_following(channel,accounts)

        bots = Bot(channel)
        bots.CreateBots(accounts,"oauthlist.txt","localhost",9050)
        for _ in range(6):
                # Add random number to get around the 1 message limit
                bots.SendMessage(scripts.spintax.spin(bot_message))
                time.sleep(.500)
    # ping command
    @commands.command()
    async def spamchannel(self, ctx,arg1,arg2,arg3):
        channel = arg1
        accounts = int(arg2)
        bot_message = arg3
        if(accounts > 250):
            await ctx.message.author.send("Please refrain from using more then 250 accounts")
            await ctx.message.delete()
            
        t1 = threading.Thread(target=self.handle_channel_spam,args=(channel,accounts,bot_message))
        t1.daemon = True
        t1.start()
        embed = discord.Embed(title="Spamming {0} with {1} accounts...".format(channel,accounts), color=0x00ff00)
        embed.add_field(name="Message", value=bot_message, inline=False)
        embed.add_field(name="Channel", value=channel, inline=False)
        embed.add_field(name="Accounts", value=str(accounts),inline=False)
        ETA = "~"
        ETA += str(.5*accounts + 3)
        ETA += " Seconds"
        embed.add_field(name="ETA", value=ETA,inline=False)
        await ctx.message.channel.send(embed=embed)
        return

# add this cog to the bot
def setup(bot):
    bot.add_cog(SpamCog(bot))