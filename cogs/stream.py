import discord
from discord.ext import commands
import math
import scripts.utils as util
import scripts.streamkeygen as skey
import threading

class StreamCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # ping command
    @commands.command()
    async def stream(self, ctx,arg1,arg2 = None,arg3 = None):
        title = "gameplay of artifact"
        game = "Artifact"
        url = arg1

        if arg2 and arg3:
            game = arg2
            title = arg3
            
        filename = ""
        if arg1:
            await ctx.message.channel.send("Encoding video...")
            import uuid
            filename = str(uuid.uuid4())
            stream_key,display_name = skey.GenStreamKey(title,game)
            t1 = threading.Thread(target=util.start_stream,args=(url,filename,stream_key))
            t1.daemon = True
            t1.start()
        embed = discord.Embed(title="Stream starting...", color=0x00ff00)
        embed.add_field(name="Channel",value=display_name,inline=False)
        await ctx.message.channel.send(embed=embed)

# add this cog to the bot
def setup(bot):
    bot.add_cog(StreamCog(bot))