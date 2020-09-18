from random import randint

import discord
from discord.ext.commands import Cog, command, has_permissions
from discord.utils import get

from cogs.countries import COUNTRIES, FLAGS


class CountryRoles(Cog):
    def __init__(self, bot):
        """Initializes the cog's bot"""
        self.bot = bot

    @command(description='Adds all country roles and sets up react messages')
    @has_permissions(administrator=True)
    async def start(self, ctx):
        await ctx.send('Adding roles...')
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
            await ctx.send('Roles added! :slight_smile:')
        except Exception as e:
            print(e)
            await ctx.send('Couldn\'t add all roles :frowning:')

    @command(description='Deletes all previously added country roles')
    @has_permissions(administrator=True)
    async def reset(self, ctx):
        await ctx.send('Deleting roles...')
        try:
            guild = ctx.guild
            guild_roles = await guild.fetch_roles()
            added_country_roles = filter(
                lambda x: x.name in COUNTRIES, guild_roles)
            for role in added_country_roles:
                await role.delete()
            await ctx.send('Roles deleted! :slight_smile:')
        except Exception as e:
            print(e)
            await ctx.send('Couldn\'t delete all roles :frowning:')

    @command(description='Gives the user the specified role')
    async def gimme(self, ctx, country):
        try:
            guild = ctx.guild
            guild_roles = await guild.fetch_roles()
            user_roles = list(
                filter(lambda x: x.name not in COUNTRIES, ctx.message.author.roles))

            role = get(guild_roles, name=country)
            if country in COUNTRIES and role is not None:
                user_roles.append(role)
            elif country in FLAGS:
                user_roles.append(get(guild_roles, name=FLAGS[country]))
            else:
                return

            await ctx.message.author.edit(roles=user_roles)
            await ctx.send('Role updated! :slight_smile:')
        except Exception as e:
            print(e)
            await ctx.send('Couldn\'t assign role :frowning:')
