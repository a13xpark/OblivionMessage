import discord
import os

TARGET_USER_ID = 525129432927698944  # replace with the user ID

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f"Logged in as {client.user}")

@client.event
async def on_message(message):

    if message.author.bot:
        return

    if message.author.id == TARGET_USER_ID:
        await message.reply("yoo beebs hush up")

TOKEN = os.getenv("DISCORD_TOKEN")

client.run(TOKEN)
