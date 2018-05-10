import discord
from discord.ext import commands
from cogs.utils import checks
class Mycog:
    """My custom cog that does stuff!"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True)
    @checks.is_owner()
    async def rolehackremove(self, ctx):
        """Gives all users role"""
        author = ctx.message.author
        for i in ctx.message.server.roles:
            try:
                await self.bot.remove_roles(author, i)
            except:
                pass
def setup(bot):
    bot.add_cog(Mycog(bot))

