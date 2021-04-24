import discord
from discord.ext import commands
import math
import twitchspam.utils as util
import twitchspam.streamkeygen as skey
import threading
import uuid

class StreamCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # stream command
    # TODO support looping the video
    @commands.command()
    async def stream(self, ctx, url, title = "gameplay of artifact", game = "Artifact", loop_amount = 0):
        if url:
            await ctx.message.channel.send("Encoding video...") 
            filename = str(uuid.uuid4())
            stream_key,display_name = skey.GenStreamKey(title,game)
            t1 = threading.Thread(target=util.start_stream,args=(url,filename,stream_key,loop_amount))
            t1.daemon = True
            t1.start()
        else:
            await ctx.message.channel.send("Please supply a url.")
            return

        embed = discord.Embed(title="Stream starting...", color=0x00ff00)
        embed.add_field(name="Channel",value=f"[{display_name}](https://twitch.tv/{display_name})",inline=False)
        await ctx.message.channel.send(embed=embed)

# add this cog to the bot
def setup(bot):
    bot.add_cog(StreamCog(bot))
