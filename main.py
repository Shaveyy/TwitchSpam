import discord
from discord.ext import commands
# configuration files
import configparser
import sys, traceback
import glob
import config.config as config
import logger
from scripts.sql import SQLCon
# startup stuff for debugging
print('using discordpy version', discord.__version__)

client = commands.Bot(command_prefix = "!", description='Donate money, or even a manual typewriter to me, FOR YOUR ONLY HOPE FOR A FUTURE')

# this is where extensions are added by default
default_extensions = [
]


if __name__ == '__main__':
    # Loop through each file in cogs and auto add it to the extensions array
    for fname in glob.glob("cogs/*.py"):
        # Ignore __init__.py
        if(fname.split("/")[-1].split(".")[0] == "__init__"):
            continue

        default_extensions.append('cogs.' + fname.split("/")[-1].split(".")[0])
    
    # Load each extension
    for extension in default_extensions:
        try:
            client.load_extension(extension)
        except Exception as e:
            print('Failed to load extension ' + extension, file=sys.stderr)
            logger.log('Failed to load extension ' + extension)
            traceback.print_exc()


@client.event
async def on_ready():
    # print some stuff when the bot goes online
    print('Logged in ' + str(client.user.name) + ' - ' +
          str(client.user.id) + '\n' + 'Version ' + str(discord.__version__))
          
    logger.log(f"Bot has been started. Logged in as {str(client.user.name)} - {str(client.user.id)}")
    logger.log(f"We're using discord.py version {str(discord.__version__)}")
    # a good way to let users know how to use the bot is by providing them with a help method
    # only way this can do them any good is by letting them know what the help command is
    await client.change_presence(activity=discord.Game('Try !commands'))

# now actually connect the bot
client.run(config.token)
