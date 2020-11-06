import discord
from discord.ext import commands
import math
import twitchspam.utils as util
import twitchspam.streamkeygen as skey
import threading
import twitchspam.spamreport as report

class SpamReportCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # ping command
    @commands.command()
    async def spamreport(self, ctx,arg1,arg2):
        channel = arg1
        amount = arg2
        report.start_reporting(channel,int(amount))
        await ctx.message.channel.send("Spam reporting em {}".format(channel))
# add this cog to the bot
def setup(bot):
    bot.add_cog(SpamReportCog(bot))