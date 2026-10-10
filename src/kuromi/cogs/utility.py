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
        name="avatar",
        description="Display a user's global avatar",
    )
    @discord.option(
        "user",
        discord.User,
        description="The user whose avatar to display",
    )
    async def avatar(
        self,
        ctx: discord.ApplicationContext,
        user: discord.User,
    ) -> None:
        avatar = user.avatar
        if avatar is None:
            avatar = user.display_avatar
        avatar_url = avatar.url
        await ctx.respond(avatar_url)

    @discord.slash_command(
        name="member-count",
        description="Check the server's member count",
        guild_only=True,
    )
    async def member_count(
        self,
        ctx: discord.ApplicationContext,
    ) -> None:
        members = ctx.guild.members
        member_count = len(members)
        bot_count = 0
        for member in members:
            if member.bot:
                bot_count += 1
        user_count = member_count - bot_count
        message = "Counting...\n"
        message += str(member_count)
        if member_count != 1:
            message += " members\n"
        else:
            message += " member\n"
        message += str(user_count)
        if user_count != 1:
            message += " users\n"
        else:
            message += " user\n"
        message += str(bot_count)
        if bot_count != 1:
            message += " bots"
        else:
            message += " bot"
        await ctx.respond(message)

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
        name="server-avatar",
        description="Display a member's server avatar",
        guild_only=True,
    )
    @discord.option(
        "member",
        discord.Member,
        description="The member whose avatar to display",
    )
    async def server_avatar(
        self,
        ctx: discord.ApplicationContext,
        member: discord.Member,
    ) -> None:
        avatar = member.guild_avatar
        if avatar is None:
            avatar = member.display_avatar
        avatar_url = avatar.url
        await ctx.respond(avatar_url)

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