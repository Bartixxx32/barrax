import discord
from discord.ext import commands
from cogs.utils import checks
class Mycog:
    """My custom cog that does stuff!"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True)
    @checks.is_owner()
    async def masskick(self, ctx):
        """Gives all users role"""
        await self.bot.say("Kicking all users")
        for i in list(ctx.message.server.members):
            await self.bot.kick(i,)
def setup(bot):
    bot.add_cog(Mycog(bot))

