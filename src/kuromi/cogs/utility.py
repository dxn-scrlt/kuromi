import discord
from discord.ext import commands

class Utility(commands.Cog):
    def __init__(
        self,
        bot: discord.Bot,
    ) -> None:
        self.bot = bot

    @discord.slash_command(
        name="ping",
        description="Check the bot's ping",
    )
    async def ping(
        self,
        ctx: discord.ApplicationContext,
    ) -> None:
        latency = round(self.bot.latency * 1_000)
        await ctx.respond(f"Pong! {latency}ms")

def setup(bot: discord.Bot) -> None:
    bot.add_cog(Utility(bot))