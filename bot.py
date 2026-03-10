import discord
import os

TARGET_USER_ID = 875803669830971482  # replace with the user ID

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
        await message.reply("https://cdn.discordapp.com/attachments/1349551267906850929/1480287940440625162/am3jvo.gif?ex=69b1c413&is=69b07293&hm=a1ff5e041941b78ea4e78bf243083860b07fdec362cad6762714092df64c032c&")

TOKEN = os.getenv("DISCORD_TOKEN")

client.run(TOKEN)
