import discord
from discord.ext import commands
import math
from twitchspam.sql import SQLCon

class MiscCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # Add user to the DB on message
    # Mainly for tracking usage
    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author == self.bot.user:
            return
            
    # list commands command
    # TODO make this automatically generate
    @commands.command()
    async def commands(self, ctx):
        await ctx.message.channel.send("""The commands are:
**!stream {URL} {Optional: Game} {Optional: Title}**
Starts a stream for you to clip :)
You can add a URL to the command and it'll download it!
**!spamchannel {channel} {number of accounts} "{message}" (in quotes)**
Spams a channel with your desired message
**!genkey**
Gives you a stream key
**!followbot {channel} {amount}**
Followbot a user (this is a WIP)
**!donateoauth {oauth}**
Donates an OAuth token
**!spamreport {channel} {amount}**
Spam reports an account
        """)

# add this cog to the bot
def setup(bot):
    bot.add_cog(MiscCog(bot))