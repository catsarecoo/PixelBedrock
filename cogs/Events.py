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
from discord.ext import commands

from logging_files.events_logging import logger


class Events(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_member_join(self, member):
        welcome_messages = [
            f"**{member}** just joined the server - glhf!",
            f"**{member}** just joined. Everyone, look busy!",
            f"**{member}** just joined. Can I get a heal?",
            f"**{member}** joined your party.",
            f"**{member}** joined. You must construct additional pylons.",
            f"Ermagherd. **{member}** is here.",
            f"Welcome, **{member}**  Stay awhile and listen.",
            f"Welcome, **{member}**  We were expecting you ( ͡° ͜ʖ ͡°)",
            f"Welcome, **{member}**  We hope you brought pizza.",
            f"Welcome **{member}**  Leave your weapons by the door.",
            f"A wild **{member}** appeared.",
            f"Swoooosh. **{member}** just landed.",
            f"Brace yourselves. **{member}** just joined the server.",
            f"**{member}** just joined. Hide your bananas.",
            f"**{member}** just arrived. Seems OP - please nerf.",
            f"**{member}** just slid into the server.",
            f"A **{member}** has spawned in the server.",
            f"Big **{member}** showed up!",
            f"Where’s **{member}**  In the server!",
            f"**{member}** hopped into the server. Kangaroo!!",
            f"**{member}** just showed up. Hold my beer.",
            f"Challenger approaching - **{member}** has appeared!",
            f"It's a bird! It's a plane! Nevermind, it's just **{member}** ",
            f"It's **{member}**  Praise the sun! \\\\[T]/",
            f"Never gonna give **{member}** up. Never gonna let **{member}** down.",
            f"Ha! **{member}** has joined! You activated my trap card!",
            f"Cheers, love! **{member}** s here!",
            f"Hey! Listen! **{member}** has joined!",
            f"We've been expecting you **{member}**",
            f"It's dangerous to go alone, take **{member}**",
            f"**{member}** has joined the server! It's super effective!",
            f"Cheers, love! **{member}** is here!",
            f"**{member}** is here, as the prophecy foretold.",
            f"**{member}** has arrived. Party's over.",
            f"Ready player **{member}**",
            f"**{member}** is here to kick butt and chew bubblegum. And **{member}** is all out of gum.",
            f"Hello. Is it **{member}** you're looking for?",
            f"**{member}** has joined. Stay a while and listen!",
            f"Roses are red, violets are blue, **{member}** joined this server with you",
        ]

        members = self.bot.get_guild(657160854273261578)
        welcome_channel = self.bot.get_channel(657161568248791041)

        embed = discord.Embed(
            colour=random.choice(self.bot.embed_colors),
            title=f"★ A new member has joined the server!",
            description=f"⇁ {random.choice(welcome_messages)}",
        )

        await welcome_channel.send(embed=embed)

        logger.info(f"Events | Member Join: {member}")


def setup(bot):
    bot.add_cog(Events(bot))