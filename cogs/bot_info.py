from datetime import datetime

import discord
from discord.ext.commands import Cog, slash_command, Context, CommandError, CommandInvokeError


class BotInfo(Cog):
    def __init__(self, bot):
        """Sets the cog's bot. Also sets a custom prefix for commands if defined in .env"""
        self.bot = bot
        self.start_time = datetime.now()
        self.prefix = '/'

    @slash_command(description='Sends information about the bot')
    async def about(self, ctx):
        info = await self.bot.application_info()
        embed = discord.Embed(
            title=f'{info.name}',
            description=f'{info.description}',
            colour=0x1aaae5,
        ).add_field(
            name='Guild Count',
            value=len(self.bot.guilds),
            inline=True
        ).add_field(
            name='User Count',
            value=len(self.bot.users),
            inline=True
        ).add_field(
            name='Uptime',
            value=f'{datetime.now() - self.start_time}',
            inline=True
        ).add_field(
            name='Latency',
            value=f'{round(self.bot.latency * 1000, 2)}ms',
            inline=True
        ).set_footer(text=f'Made by {info.owner}')
        await ctx.respond(embed=embed)

    #TODO update to reflect 'countries' and 'nearme'
    @slash_command(description='Sends a help message')
    async def help(self, ctx):
        embed = discord.Embed(
            title='Help',
            description='Country Roles manages roles.',
            colour=0x41c03f
        ).add_field(
            name=f'`{self.prefix}start`',
            value='Sets up country roles in this server. **Only admins can run this command**',
            inline=True
        ).add_field(
            name=f'`{self.prefix}reset`',
            value='Removes all country roles in this server. **Only admins can run this command**',
            inline=True
        ).add_field(
            name=f'`{self.prefix}country`',
            value='Gives you the role specified by `<country>`. This can either be the name or the flag emoji',
            inline=True
        ).add_field(
            name=f'`{self.prefix}countries`',
            value='Lists all the countries accepted by this bot',
            inline=True
        ).add_field(
            name=f'`{self.prefix}nearme`',
            value='All server members in your country, sent as a DM',
            inline=True
        ).add_field(
            name=f'`{self.prefix}about`',
            value='About Country Roles',
            inline=True
        ).add_field(
            name=f'`{self.prefix}invite`',
            value='Bot invite link',
            inline=True
        ).add_field(
            name=f'`{self.prefix}help`',
            value='Shows this message',
            inline=True
        ).add_field(
            name=f'`{self.prefix}ping`',
            value='Check the bot\'s latency',
            inline=True
        ).add_field(
            name=f'`{self.prefix}source`',
            value='Links to the bot\'s GitHub repo',
            inline=True
        )
        await ctx.respond(embed=embed)

    @slash_command(description='Sends a bot invite link')
    async def invite(self, ctx):
        await ctx.respond('Add your own bot invite link here')

    @slash_command(description='Checks latency')
    async def ping(self, ctx):
        await ctx.respond(f'Pong; {round(self.bot.latency * 1000, 2)}ms')

    @slash_command(description='Sends the link to the bot\'s GitHub repo')
    async def source(self, ctx):
        await ctx.respond('https://github.com/TheRealOwenRees/country-roles')

    @Cog.listener()
    async def on_guild_join(self, guild):
        """Sends a nice message when added to a new server"""
        embed = discord.Embed(
            title='Thanks for adding me to your server! :heart:',
            description=f'To get started, simply type `{self.prefix}start` as an admin, '
                        + f'or type `{self.prefix}help` for a list of commands',
            colour=0x2ac99e
        ).add_field(
            name='Have fun!',
            value=':zap:',
            inline=False
        )
        await guild.system_channel.send(embed=embed)

    # cog error handling
    async def cog_command_error(self, ctx: Context, error: CommandError):
        if isinstance(error, CommandInvokeError):
            await ctx.send('Sorry, an error has occured. Please try again.')
