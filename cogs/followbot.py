import discord
from discord.ext import commands
import math
import threading
import requests
import json
import scripts.follow as follow


class FollowCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    # ping command
    @commands.command()
    async def followbot(self, ctx,arg1,arg2):
        channel = arg1
        amount = int(arg2)
        if(amount == None):
            amount = 10
            
        follow.start_following(channel,amount)
        await ctx.message.channel.send("Follow botting " + channel + "...")
        return

# add this cog to the bot
def setup(bot):
    bot.add_cog(FollowCog(bot))