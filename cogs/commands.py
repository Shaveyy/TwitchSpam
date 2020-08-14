import discord
from discord.ext import commands
import math
import json

class CommandsCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def macros(self,ctx):
        macrofile = json.loads(open("./spintaxmacros.json","r").read())[0]
        message = []
        for macro in macrofile:
            message.append("**" + macro + "**\r\n")

        await ctx.message.channel.send("Macros:\r\n" + message)
        
    # ping command
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
Donates an OAuth token to your's truly :)
**!spamreport {channel} {amount}**
Spam reports an account
        """)

# add this cog to the bot
def setup(bot):
    bot.add_cog(CommandsCog(bot))