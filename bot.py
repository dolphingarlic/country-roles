import asyncio
import os
import logging

from discord import Activity, ActivityType
from discord.ext.commands import Bot, when_mentioned_or

from cogs.country_roles import CountryRoles
from cogs.bot_info import BotInfo

async def main():
    logging.basicConfig(level=logging.INFO)
    prefix = os.environ.get('BOT_PREFIX', 'r!')
    bot = Bot(
        command_prefix=when_mentioned_or(prefix),
        help_command=None,
        activity=Activity(type=ActivityType.playing, name=f'with roles | {prefix}help'),
    )
    bot.add_cog(CountryRoles(bot))
    bot.add_cog(BotInfo(bot))
    await bot.start(os.environ['DISCORD_TOKEN'])


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(main())
    except KeyboardInterrupt:
        loop.close()
