# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# PixelBedrock - Official Discord bot for PixelBE                           #
# Copyright (C) 2019-2020 TrackRunny                                        #
#                                                                           #
# This program is free software: you can redistribute it and/or modify      #
# it under the terms of the GNU General Public License as published by      #
# the Free Software Foundation, either version 3 of the License, or         #
# (at your option) any later version.                                       #
#                                                                           #
# This program is distributed in the hope that it will be useful,           #
# but WITHOUT ANY WARRANTY; without even the implied warranty of            #
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the             #
# GNU General Public License for more details.                              #
#                                                                           #
# You should have received a copy of the GNU General Public License         #
# along with this program. If not, see <https://www.gnu.org/licenses/>.     #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

import random

import discord
import psutil
from discord.ext import commands

from logging_files.information_logging import logger


class Information(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def about(self, ctx):
        cpu = str(psutil.cpu_percent())
        ram = str(psutil.virtual_memory()[3] / 1000000000)
        ram_round = ram[:3]
        disk = str(psutil.disk_usage('/')[1] / 1000000000)
        disk_round = disk[:4]
        boot_time = str(psutil.boot_time() / 100000000)
        boot_time_round = boot_time[:4]

        source_code = "[**Open source**](https://github.com/TrackRunny/PixelBedrock)"
        picture = ctx.guild.icon_url_as(size=1024, format=None, static_format="png")
        emoji = "<:github:662426678907240468>"

        stats = f"```" \
                f"• CPU: {cpu}%" \
                f"\n• RAM: {ram_round} / 3 GIGABYTES" \
                f"\n• DISK: {disk_round} / 40 GIGABYTES" \
                f"\n• BOOT TIME: {boot_time_round} SECONDS" \
                f"\n• OPERATING SYSTEM: UBUNTU SERVER 18.04 LTS     " \
                f"```"

        bot_info = f"```" \
                   f"• LIBRARY VERSION: DISCORD.PY VERSION 1.2.5" \
                   f"\n• PYTHON VERSION: 3.7.5     " \
                   f"```"

        embed = discord.Embed(
            color=random.choice(self.bot.embed_colors),
            title="★ PixelBedrock",
            description=f"\n• Official Discord bot for the PixelBE MCBE server."
                        f"\n• View **all commands** with `b!commands`"
                        f"\n• {source_code} {emoji}"
        )
        embed.set_thumbnail(url=picture)
        embed.add_field(name="⇁ Hardware Stats", inline=False, value=stats)
        embed.add_field(name="⇁ Bot Stats", inline=False, value=bot_info)
        embed.set_footer(text="• Developed by TrackRunny#0001", icon_url="https://i.imgur.com/TiUqRH8.gif")

        await ctx.send(embed=embed)

        logger.info(f"information | Sent Help: {ctx.author}")

    @commands.command(aliases=["commands", "cmds"])
    async def help(self, ctx):
        picture = ctx.guild.icon_url_as(size=1024, format=None, static_format="png")
        embed = discord.Embed(
            color=random.choice(self.bot.embed_colors),
            title="★ All Bot Commands",
        )
        embed.set_thumbnail(url=picture)

        information = "`b!commands`, `b!about`, `b!vote`"
        utility = "`b!uptime`, `b!server`, `b!suggest`, `b!newsletter`"

        embed.add_field(name="⇁ Information Commands", inline=False, value=information)
        embed.add_field(name="⇁ Utility Commands", inline=False, value=utility)

        await ctx.send(embed=embed)

        logger.info(f"Information | Sent Commands: {ctx.author}")

    @commands.command()
    async def vote(self, ctx):
        vote_link = "[**here**](http://bit.ly/pixelbeVote)"
        embed = discord.Embed(
            color=random.choice(self.bot.embed_colors),
            title="★ Vote For PixelBE",
            description=f"⇁ Please vote {vote_link}, you can vote every 24 hours."
        )

        await ctx.send(embed=embed)

        logger.info(f"Information | Sent Vote: {ctx.author}")


def setup(bot):
    bot.add_cog(Information(bot))
