import discord
from discord.ext import commands
import math
import twitchspam.utils as util
import twitchspam.streamkeygen as skey
import config.config as config
from twitchspam.sql import SQLCon

class GenKeyCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # ping command
    @commands.command()
    async def genkey(self, ctx,arg1="Innit",arg2="Old School Runescape"):
        title = arg1
        game = arg2
        
        stream_key,display_name = skey.GenStreamKey(title,game)
        
        embed = discord.Embed(title="Your Channel", color=0x00ff00)
        embed.add_field(name="Stream Key", value=stream_key, inline=False)
        embed.add_field(name="Channel name", value=display_name, inline=False)
        await ctx.message.author.send(embed=embed)
        await ctx.message.channel.send("You have been DMed your key.")
        return

# add this cog to the bot
def setup(bot):
    bot.add_cog(GenKeyCog(bot))
