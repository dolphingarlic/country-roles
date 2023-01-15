import os
import logging
from dotenv import load_dotenv

from discord import Game, Intents
from discord.ext.commands import Bot

from cogs.bot_info import BotInfo
from cogs.country_roles import CountryRoles

# environment variables for test server
load_dotenv()
DISCORD_TOKEN = os.getenv('DISCORD_TOKEN')

# dev logging
logging.basicConfig(level=logging.DEBUG)

intents = Intents.default()

bot = Bot(
    intents = intents,
    help_command=None,
    activity=Game(name=f'with roles | /help')
)
bot.add_cog(BotInfo(bot))
bot.add_cog(CountryRoles(bot))

# bot startup and confirmation
@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!') 
bot.run(DISCORD_TOKEN)
