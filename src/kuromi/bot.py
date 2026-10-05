import os
import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("TOKEN")

intents = discord.Intents.all()
bot = discord.Bot(intents=intents)

@bot.event
async def on_ready() -> None:
    print(f"Logged in as {bot.user}")

cogs_path = os.path.join(
    os.path.dirname(__file__),
    "cogs",
)
cog_files = os.listdir(cogs_path)

for file in cog_files:
    if file.endswith(".py"):
        cog = file[:-3]
        bot.load_extension(f"kuromi.cogs.{cog}")
        print(f"Loaded cog: {cog}")

def main() -> None:
    bot.run(TOKEN)

if __name__ == "__main__":
    main()