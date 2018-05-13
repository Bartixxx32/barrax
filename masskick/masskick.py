import discord
from discord.ext import commands
from cogs.utils import checks
class Barrax:
    """Barrax cog"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True)
    @checks.is_owner()
    async def masskick(self, ctx):
        """Kicking all users"""
        await self.bot.say("Kicking all users")
        for i in list(ctx.message.server.members):
            await self.bot.kick(i,)
def setup(bot):
    bot.add_cog(Barrax(bot))

