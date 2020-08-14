import discord
from discord.ext import commands
import json

class MacrosCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def macros(self,ctx):
        macrofile = json.loads(open("./spintaxmacros.json","r").read())[0]
        message = ""
        for macro in macrofile:
            message += "**" + macro + "**\r\n"
            
        await ctx.message.channel.send("Macros:\r\n" + message)

# add this cog to the bot
def setup(bot):
    bot.add_cog(MacrosCog(bot))