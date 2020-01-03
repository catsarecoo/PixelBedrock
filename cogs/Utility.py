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

import datetime
import random

import discord
from discord.ext import commands
from mcstatus import MinecraftServer

from logging_files.utility_logging import logger
from utils.default import uptime
from utils.motd_format import motd_format


class Utility(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self.bot_start_time = datetime.datetime.now()

    @commands.command()
    async def uptime(self, ctx):
        embed = discord.Embed(
            color=random.choice(self.bot.embed_colors),
            title="★ Uptime",
            description=uptime(datetime.datetime.now() - self.bot_start_time)
        )

        await ctx.send(embed=embed)

        logger.info(f"Sent Uptime: {ctx.author}")

    @commands.command()
    async def server(self, ctx, server="play.pixelbe.cf", port=19132):
        try:
            srv = MinecraftServer(f"{server}", int(port))
            motd = srv.query()
            players_string = ', '.join(str(p) for p in motd.players.names)
            plugins_string = ', '.join(str(l) for l in motd.software.plugins)

            embed = discord.Embed(
                color=random.choice(self.bot.embed_colors),
                title="★ PixelBe Server Status"
            )
            embed.add_field(name="⇁ IP Address", inline=True, value=f"```{server}```")
            embed.add_field(name="⇁ Server Port", inline=True, value=f"```{port}```")
            embed.add_field(name="⇁ Amount Of Players", inline=True,
                            value=f"```{len(motd.players.names)}/{motd.players.max}```")
            embed.add_field(name="⇁ Main Map", inline=True, value=f"```{motd.map}```")
            embed.add_field(name="⇁ Server Software", inline=True, value=f"```{motd.software.brand}```")
            embed.add_field(name="⇁ Supported Version(s)", inline=False, value=f"```{motd.software.version}```")
            embed.add_field(name="⇁ MOTD", inline=False, value=f"```{motd_format(motd.motd, ['Â', '§', 'b', 'r', '8', 'le'], '')}```")

            if not len(motd.players.names):
                embed.add_field(name="⇁ Player Names", inline=False,
                                value="```No Players Online!```")
            elif len(players_string) > 1024:
                players_string = players_string[:1018]
                players_string, _, _ = players_string.rpartition(', ')
                players_string = '```' + players_string + ' ...```'
                embed.add_field(name="⇁ Player Names", inline=False,
                                value=players_string)
            else:
                embed.add_field(name="⇁ Player Names", inline=False,
                                value='```' + '' + ', '.join(motd.players.names) + ', '[:-0] + '```')
            if not len(plugins_string):
                embed.add_field(name="⇁ Server Plugins", inline=False, value="```No Plugin Information!```")
            elif len(plugins_string) > 1024:
                plugins_string = plugins_string[:1018]
                plugins_string, _, _ = plugins_string.rpartition(', ')
                plugins_string = '```' + plugins_string + ' ...```'
                embed.add_field(name="⇁ Server Plugins", inline=False, value=plugins_string)
            else:
                embed.add_field(name="⇁ Server Plugins", inline=False,
                                value='```' + '' + ', '.join(motd.software.plugins) + ', '[:-0] + '```')

            await ctx.send(embed=embed)

            logger.info(f"Utility | Sent Server: {ctx.author}")

        except Exception:
            embed_error = discord.Embed(
                color=random.choice(self.bot.embed_colors),
                title="★ Server Timeout",
                description="⇁ PixelBe is offline!"
            )
            await ctx.send(embed=embed_error)

    @commands.command()
    @commands.cooldown(rate=1, per=3600, type=commands.BucketType.user)
    async def suggest(self, ctx, *, suggestion):
        channel = self.bot.get_channel(662183000187863053)
        picture = ctx.author.avatar_url_as(size=1024, format=None, static_format="png")

        embed = discord.Embed(
            color=random.choice(self.bot.embed_colors),
            title=f"★ New Suggestion From: {ctx.author}",
            description=f"⇁ Suggestion: `{suggestion}`"
        )
        embed.set_thumbnail(url=picture)

        embed2 = discord.Embed(
            color=random.choice(self.bot.embed_colors),
            title="★ Suggestion Successfully Sent",
            description="⇁ **Thank you** for your suggestion! Please check <#662183000187863053> to view it."
        )

        await ctx.send(embed=embed2)
        message = await channel.send(embed=embed)

        await message.add_reaction("👍")
        await message.add_reaction("👎")

        logger.info(f"Utility | Sent Suggestion: {ctx.author} | Suggestion: {suggestion}")

    @suggest.error
    async def suggest_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            embed = discord.Embed(
                color=random.choice(self.bot.embed_colors),
                title="★ Required Argument Missing",
                description="⇁ Please follow the format: `e!suggest <suggestion>`"
            )

            await ctx.send(embed=embed)
            ctx.command.reset_cooldown(ctx)
        elif isinstance(error, commands.CommandOnCooldown):
            embed = discord.Embed(
                color=random.choice(self.bot.embed_colors),
                title="★ Cool Down Limit Reached",
                description="⇁ You can only send a suggestion every hour."
            )

            await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(Utility(bot))
