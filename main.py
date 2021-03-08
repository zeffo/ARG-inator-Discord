import discord
from discord.ext import commands
import os
from dotenv import load_dotenv
load_dotenv()
token = os.getenv('TOKEN')
client = commands.Bot(command_prefix='>',intents=discord.Intents.all(),help_command=None)


@client.event
async def on_ready():
    print('Bot is ready')
    while True:
        statuses = [discord.Activity(type=discord.ActivityType.watching, name="The Imitation Game"),
                    discord.Activity(type=discord.ActivityType.listening, name="lofi hip-hop beats to relax and crack code 24/7"),
                    discord.Game(name=">d")]
        await client.change_presence(activity=random.choice(statuses))
        await asyncio.sleep(5)


extensions = ["cipherdecode",'cipherencode','otherciphertools']

if __name__ == "__main__":
    for ext in extensions:
        client.load_extension(ext)

client.run(token)
