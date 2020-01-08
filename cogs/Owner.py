"""
PixelBedrock - Official Discord bot for PixelBE
Copyright (C) 2020 TrackRunny

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program. If not, see <https://www.gnu.org/licenses/>.
"""

import random

import discord
from discord.ext import commands

from logging_files.owner_logging import logger


class Owner(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.is_owner()
    async def activity(self, ctx, number, *, activity):
        # Type 0 = Playing a game, Type 1 = Live on Twitch, Type 2 = Listening, Type 3 = Watching
        await self.bot.change_presence(activity=discord.Activity(type=number, name=activity))

        embed = discord.Embed(
            color=random.choice(self.bot.embed_colors),
            title="★ Activity Updated",
            description=f"⇁ Activity updated to: `{activity}`"
        )

        await ctx.send(embed=embed)

        logger.info(f"Owner | Sent Activity: {ctx.author} | Activity: {number} | Status: {activity}")

    @commands.command()
    @commands.is_owner()
    async def shutdown(self, ctx):
        embed = discord.Embed(
            color=random.choice(self.bot.embed_colors),
            title="★ Shutdown",
            description="⇁ Shutting down now..."
        )

        await ctx.send(embed=embed)
        await self.bot.logout()

        logger.info(f"Owner | Sent Shutdown: {ctx.author}")


def setup(bot):
    bot.add_cog(Owner(bot))
