import discord
from discord.ext import commands

class Barrax:
    """Barrax cog"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True)
    async def kickme(self, ctx):
        """Kick who write this command"""
        
        await self.bot.say("User want to leave from this server :C")
        await self.bot.say(ctx.message.author)
def setup(bot):
    bot.add_cog(Barrax(bot))
