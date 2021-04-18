import discord
from discord.ext import commands
import math
import threading
import requests
import json
import twitchspam.follow as follow
import config.config as config
import logger

class FollowCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    # followbot command
    @commands.command()
    async def followbot(self, ctx, channel, amount=config.defaultfollowamount):
        amount = int(amount)

        logger.log(f"Starting followbot on channel {channel} with amount {amount}")
        followctx = follow.Follow(channel,amount)
        await followctx.start_followbot()
        await ctx.message.channel.send("Follow botting " + channel + "...")
        return

# add this cog to the bot
def setup(bot):
    bot.add_cog(FollowCog(bot))
