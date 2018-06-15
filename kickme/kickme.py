import discord
from discord.ext import commands

class Barrax:
    """Barrax cog"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True)
    async def kickme(self,ctx):
        """Kick who write this command"""
        user = ctx.message.author.mention
        await self.bot.say("User {} leave from this server :C".format(user))
        await self.bot.kick(ctx.message.author)
def setup(bot):
    bot.add_cog(Barrax(bot))