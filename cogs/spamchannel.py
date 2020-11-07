import discord
from discord.ext import commands
import math
import threading
import time
import socket
from twitchspam.bot import Bot
import random
# Import followbot module
import re
import twitchspam.follow
import config.config as config
import logger
import asyncio
import copy

# discord.py calls groups of commands cogs
# cogs can also be handlers for different types of events
# and respond to changes in data as they happen

# setup
class SpamCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.output = ""

    async def update_output(self,output,message,embed):
        self.output += output + "\n"
        updatedEmbed = copy.deepcopy(embed)
        updatedEmbed.add_field(name="Output",value=f"```{self.output}```")
        await message.edit(embed=updatedEmbed)
        

    async def handle_channel_spam(self,channel,accounts,bot_message,message,embed):
        """
        Seperate function for threading the channel spam.
        TODO clean this up a bit
        """
        # Check followers only mode
        followers=False
        sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        sock.connect(("irc.chat.twitch.tv" , 6667))
        sock.send("PASS oauth:3joa4tvfl6dyb527bthp1fmncgnsi6\r\n".encode())
        sock.send("NICK lolsecurity\r\n".encode())
        # Request member perms to get the mode of the channel
        membership = "CAP REQ :twitch.tv/membership\r\n"
        commands = "CAP REQ :twitch.tv/commands twitch.tv/tags\r\n"
        sock.send(membership.encode())
        sock.send(commands.encode())
        await asyncio.sleep(1)
        # Join the channel of choice
        sock.send("JOIN #{}\r\n".format(channel).encode())
        # Infinite loop until we find the followers only mode.
        # Probably quit after 30 seconds of not finding it since this could be really wasteful threading wise
        try:
            while(1):
                data = sock.recv(1024)
                recvdata = data.decode('utf-8')
                p = re.search("@(.*?);",recvdata)
                if p:
                    follow = recvdata.split(";")[8]
                    if follow.split("=")[1] != "-1":
                        followers = True
                    break
        except: pass
        # Follow if follower only mode is on
        if(followers):
            await self.update_output("Detected followers only mode. Followbotting...",message,embed)
            twitchspam.follow.start_following(channel,accounts)
        
        await self.update_output("Creating bots...",message,embed)
        # Create bots
        bots = Bot(channel)
        bots.CreateBots(accounts,config.oauthsfile,"localhost",9050)
        # Send bot messages 3 times,
        # Add to config soon
        await self.update_output("Bots have connected...\n Sending messages",message,embed)
        for _ in range(3):
                # Add random number to get around the 1 message limit
                bots.SendMessage(bot_message)
                time.sleep(1.25)

        await self.update_output("Finished sending bots",message,embed)
        self.output = ""
        
    # ping command
    @commands.command()
    async def spamchannel(self, ctx,arg1,arg2,arg3):
        logger.log(f"Bot started by {str(ctx.message.author)} on channel {arg1} with {arg2} accounts\r\nmessage: {arg3}")
        # Get channel, accounts, and bot_message
        channel = arg1
        accounts = int(arg2)
        bot_message = arg3
        # TODO add to config
        if(accounts > 250):
            logger.log(f"User {str(ctx.message.author)} tried using more then 250 accounts!")
            await ctx.message.author.send("Please refrain from using more then **250** accounts")
            await ctx.message.delete()

        embed = discord.Embed(title="Spamming {0} with {1} accounts...".format(channel,accounts), description="[Consider Donating](https://ko-fi.com/shaveyy)", color=0x00ff00)
        embed.add_field(name="Message", value=bot_message, inline=False)
        embed.add_field(name="Channel", value=channel, inline=False)
        embed.add_field(name="Accounts", value=str(accounts),inline=False)
        ETA = "~"
        ETA += str(.5 * accounts + 3)
        ETA += " Seconds"
        embed.add_field(name="ETA", value=ETA,inline=False)
        message = await ctx.message.channel.send(embed=embed)
        await self.handle_channel_spam(channel,accounts,bot_message,message,embed)

        return

# add this cog to the bot
def setup(bot):
    bot.add_cog(SpamCog(bot))
