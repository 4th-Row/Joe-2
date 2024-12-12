import asyncio
import os

import discord
from discord.ext import commands

class Joe(commands.Bot):
    def __init__(self):
        intents = discord.Intents.default()
        intents.message_content = True
        super().__init__(
            command_prefix='j!',
            intents=intents,
            case_insensitive=True,
            activity=discord.Activity(type=discord.ActivityType.watching, name='you code'),
            status=discord.Status.online
            )
        print(f"Created bot with prefix {self.command_prefix}.")

bot = Joe()

async def main():

    # Load cogs
    for filename in os.listdir("modules"):
        if filename[-3:] == ".py" and filename != "__init__.py" and filename != "testing.py":
            try:
                await bot.load_extension(f"modules.{filename[:-3]}")
            except Exception as e:
                print(f"Couldn't load module \"{filename}\": {e}")

    @bot.event
    async def on_ready():
        print(f'Logged into Discord as {bot.user}')

    @bot.command()
    async def test(ctx: commands.Context):
        await ctx.send('ok')

    DISCORD_TOKEN = os.getenv('DISCORD_TOKEN')
    print('Starting bot')
    async with bot:
        await bot.start(DISCORD_TOKEN)

if __name__ == '__main__':
    asyncio.run(main())