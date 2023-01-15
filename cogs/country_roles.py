from random import randint

import discord
from discord.ext.commands import Cog, slash_command, has_permissions, check_any, is_owner, Context, CommandError, CommandInvokeError
from discord.utils import get

from cogs.countries import COUNTRIES, FLAGS


class CountryRoles(Cog):
    def __init__(self, bot):
        """Initializes the cog's bot"""
        self.bot = bot

    # add country roles to server - ADMINS ONLY
    @slash_command(guild_ids=[1063836013736243301], description='Adds all country roles and sets up react messages')
    @check_any(is_owner(), has_permissions(manage_guild=True))
    # @has_permissions(administrator=True)
    async def start(self, ctx):
        await ctx.respond('Adding roles...')
        try:
            guild = ctx.guild
            guild_roles = await guild.fetch_roles()
            for country in COUNTRIES:
                already_added = any(
                    role.name == country for role in guild_roles)
                if not already_added:
                    await guild.create_role(
                        name=country,
                        hoist=True,
                        colour=discord.Colour(randint(0, 0xffffff))
                    )
            await ctx.respond('Roles added! :slight_smile:')
        except discord.DiscordException:
            await ctx.respond('Couldn\'t add all roles :frowning:')

    # delete country roles from server - ADMINS ONLY
    @slash_command(guild_ids=[1063836013736243301], description='Deletes all previously added country roles')
    @check_any(is_owner(), has_permissions(manage_guild=True))
    # @has_permissions(administrator=True)
    async def reset(self, ctx):
        await ctx.respond('Deleting roles...')
        try:
            guild = ctx.guild
            guild_roles = await guild.fetch_roles()
            added_country_roles = filter(
                lambda x: x.name in COUNTRIES, guild_roles)
            for role in added_country_roles:
                await role.delete()
            await ctx.respond('Roles deleted! :slight_smile:')
        except discord.DiscordException:
            await ctx.respond('Couldn\'t delete all roles :frowning:')

    # add specified country to user
    @slash_command(guild_Ids=[1063836013736243301], description='Gives the user the specified role')
    async def gimme(self, ctx, country):
        guild = ctx.guild
        guild_roles = await guild.fetch_roles()
        user_roles = list(
            filter(lambda x: x.name not in COUNTRIES, ctx.author.roles))
        role = get(guild_roles, name=country)
        if country in COUNTRIES and role is not None:
            user_roles.append(role)
            await ctx.author.edit(roles=user_roles)
            await ctx.respond('Role updated! :slight_smile:')
        elif country in FLAGS:
            user_roles.append(get(guild_roles, name=FLAGS[country]))
            await ctx.author.edit(roles=user_roles)
            await ctx.respond('Role updated! :slight_smile:')
        else:
            await ctx.respond('Couldn\'t assign role :frowning:')

    # cog error handling
    async def cog_command_error(self, ctx: Context, error: CommandError):
        if isinstance(error, CommandInvokeError):
            await ctx.send('Sorry, an error has occured. Please try again.')