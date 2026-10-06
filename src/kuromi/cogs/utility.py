import time
import discord
from discord.ext import commands

class Utility(commands.Cog):
    def __init__(
        self,
        bot: discord.Bot,
    ) -> None:
        self.bot = bot
        self.start_time = time.monotonic()

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

    @discord.slash_command(
        name="uptime",
        description="Check the bot's uptime",
    )
    async def uptime(
        self,
        ctx: discord.ApplicationContext,
    ) -> None:
        uptime = int(time.monotonic() - self.start_time)
        days, remainder = divmod(uptime, 86_400)
        hours, remainder = divmod(remainder, 3_600)
        minutes, seconds = divmod(remainder, 60)
        message = "Up! "
        if days > 0:
            message += f"{days}d "
        if hours > 0:
            message += f"{hours}h "
        if minutes > 0:
            message += f"{minutes}m "
        message += f"{seconds}s"
        await ctx.respond(message)

def setup(bot: discord.Bot) -> None:
    bot.add_cog(Utility(bot))