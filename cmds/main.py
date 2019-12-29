import discord
from discord.ext import commands
from core.classes import Cog_Extension

class Main(Cog_Extension):

    @commands.command()
    async def ping(self, ctx):
        await ctx.send(f'latency is {round(self.bot.latency*1000)} ms')

    @commands.command()
    async def bro(self, ctx):
        await ctx.send('給我去寫功課')

def setup(bot):
    bot.add_cog(Main(bot))
