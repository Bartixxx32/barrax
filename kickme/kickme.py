import discord
from discord.ext import commands

class Mycog:
    """My custom cog that does stuff!"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True)
    async def kickme(self, ctx):
        """This does stuff!"""

        #Your code will go here
        
        await self.bot.say("User want to leave from this server :C")
        await self.bot.say(ctx.message.author)
def setup(bot):
    bot.add_cog(Mycog(bot))
