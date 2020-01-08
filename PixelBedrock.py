#!/usr/bin/env python3

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

import os
from datetime import datetime

import discord
from discord.ext import commands

bot = commands.Bot(command_prefix="b!", owner_id=546812331213062144, case_insensitive=False)
line_divide = "\n———————————————————————————————"

pixelbedrock_token = os.environ.get("pixelbedrock_token")

cogs = [
    "Events",
    "Information",
    "Utility",
    "Owner"
]


class PixelBedrock(commands.Bot):
    def __init__(self):
        super().__init__(command_prefix="b!", owner_id=546812331213062144, reconnect=True, case_insensitive=False)

        self.bot = bot
        self.embed_colors = (0x03B9FB, 0x44FE77, 0xFF0101)

        self.load_extension('jishaku')
        self.remove_command('help')

    async def on_ready(self):
        # change_status.start()
        await self.change_presence(activity=discord.Activity(type=0, name=f"play.pixelbe.cf — \U0001F535"))

        if not hasattr(self, 'uptime'):
            self.uptime = datetime.utcnow()

        try:
            for cog in cogs:
                self.load_extension(f"cogs.{cog}")
        except Exception as e:
            print(f"Could not load extension {e}")

        print(f"-------------------PixelBedrock-------------------"
              f"\nBot is online and connected to {self.user}"
              f"\nCreated by TrackRunny#0001 on Discord"
              f"\nConnected to {(len(self.guilds))} Guilds."
              f"\n-------------------------------------------------")


"""
@tasks.loop(seconds=15)
async def change_status():
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=next(status)))
"""


PixelBedrock().run(pixelbedrock_token)