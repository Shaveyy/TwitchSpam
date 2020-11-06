import discord
from discord.ext import commands
import math
import twitchspam.utils as util
import threading
from twitchspam.sql import SQLCon
import re
import config.config as config

class DonateCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # ping command
    @commands.command()
    async def donateoauth(self, ctx,arg1):
        oauth = arg1 # check to see if oauth is valid
        pattern = r"oauth:[0-9-a-z]{30}"
        if not re.match(pattern,oauth):
            await ctx.message.author.send("Please input a valid oauth token")
            await ctx.message.delete()
            return
        if not util.test_oauth(oauth):
            await ctx.message.author.send("Please input a valid oauth token")
            await ctx.message.delete()
            return

        oauths = open(config.oauthsfile,"r").read().split("\n")
        for token in oauths:
            if(token == oauth):
                await ctx.message.author.send("OAuth is a duplicate")
                await ctx.message.delete()
                return
        
        file = open(config.oauthsfile,"a+")
        file.write(oauth + "\r\n")
        file.close()

        num_of_oauths = len(oauths)
        sql = SQLCon()
        userdonated = sql.UpdateUser(ctx.message.author.name,ctx.message.author.id)
        embed = discord.Embed(title="Donated OAuth", color=0x00ff00)
        embed.add_field(name="User",value=ctx.message.author.name,inline=False)
        embed.add_field(name="OAuth's donated by this user",value=userdonated,inline=False)
        embed.add_field(name="OAuth's pooled together",value=num_of_oauths,inline=False)
        await ctx.message.channel.send(embed=embed)
        await ctx.message.delete()
        return
# add this cog to the bot
def setup(bot):
    bot.add_cog(DonateCog(bot))