import discord
from discord.ext import commands

class MiscCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @commands.command()
    async def poll(self, ctx,arg):
        embed = discord.Embed(title="Poll started by " + ctx.message.author.name,description=arg, color=0x00ff00)
        msg = await ctx.message.channel.send(arg)
        await ctx.message.delete()
        await msg.add_reaction('⬆️')
        await msg.add_reaction('⬇️')
        
# add this cog to the bot
def setup(bot):
    bot.add_cog(MiscCog(bot))