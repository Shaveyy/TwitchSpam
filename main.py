import discord
from discord.ext import commands
import asyncio
# configuration files
import configparser
import sys, traceback
import glob
import config.config as config
# startup stuff for debugging
print('using discordpy version', discord.__version__)

# the command prefix should be something unique, many bots already use !, ., and / for their prefixes
# you can do any string, 'hey you stupid bot ' would totally work
client = commands.Bot(command_prefix='!', description='a')

# this is where extensions are added by default
default_extensions = [
]


if __name__ == '__main__':
    # Automatically make cog list
    for _file in glob.glob("cogs/*.py"):
        default_extensions.append('cogs.' + _file.split("/")[-1].split(".")[0])
        
    for extension in default_extensions:
        try:
            client.load_extension(extension)
        except Exception as e:
            print('Failed to load extension ' + extension, file=sys.stderr)
            traceback.print_exc()


@client.event
async def on_ready():
    # print some stuff when the bot goes online
    print('Logged in ' + str(client.user.name) + ' - ' +
          str(client.user.id) + '\n' + 'Version ' + str(discord.__version__))
    # a good way to let users know how to use the bot is by providing them with a help method
    # only way this can do them any good is by letting them know what the help command is
    await client.change_presence(activity=discord.Game('Try !commands'))

# now actually connect the bot
client.run(config.token) #"NzM1OTExODAwNjM3NDg5MzA1.XxnMWw.unlzbthL0Jxtacfq1WgPBf3nVGI"
