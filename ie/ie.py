import discord
import asyncio
from discord.ext import commands
from cogs.utils import checks
class InternetExplorer:
    """Internet explorer"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @checks.is_owner()
    async def ie(self, ie):
        """Internet explorer"""
        await asyncio.sleep(25)
        await self.bot.say(ie)
def setup(bot):
    bot.add_cog(InternetExplorer(bot))

