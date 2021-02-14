import discord
from discord.ext import commands


class Talk(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def hi(self, ctx):
        await ctx.send("hi")

    @commands.command()
    async def repeat(self, ctx, *, message: str):
        await ctx.send(message)


def setup(bot) -> None:
    bot.add_cog(Talk(bot))
