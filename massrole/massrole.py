import discord
from discord.ext import commands
from cogs.utils import checks
class Barrax:
    """Barrax cog"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True)
    @checks.is_owner()
    async def massrole(self, ctx, role : discord.Role):
        """Gives all users role"""
        await self.bot.say("Gives all users given role")
        for i in list(ctx.message.server.members):
            await self.bot.add_roles(i, role)
def setup(bot):
    bot.add_cog(Barrax(bot))

