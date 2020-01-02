"""
PixelBedrock - Official Discord bot for PixelBe
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

from logging_files.information_logging import logger


class Information(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=["help", "cmds"])
    async def commands(self, ctx):
        picture = ctx.guild.icon_url_as(size=1024, format=None, static_format="png")
        embed = discord.Embed(
            color=random.choice(self.bot.embed_colors),
            title="★ All Bot Commands",
        )
        embed.set_thumbnail(url=picture)

        information = "`b!commands`"
        utility = "`b!uptime`, `b!server`, `b!suggest`"

        embed.add_field(name="⇁ Information Commands", inline=False, value=information)
        embed.add_field(name="⇁ Utility Commands", inline=False, value=utility)

        await ctx.send(embed=embed)

        logger.info(f"Information | Sent Commands: {ctx.author}")


def setup(bot):
    bot.add_cog(Information(bot))