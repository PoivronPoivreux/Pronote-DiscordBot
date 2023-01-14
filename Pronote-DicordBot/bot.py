import discord
import subprocess

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$e'):
        channel = client.get_channel(Ton ID Du Cannal De Texte)
        with open("loading.gif", "rb") as f:
            file = discord.File(f)
        loading_message = await channel.send(file=file)

        subprocess.run(["python", "options.py"])

        await loading_message.delete()

        with open("emploi.png", "rb") as f:
            file = discord.File(f)
            await channel.send(file=file)

    if message.content.startswith('$purge'):
        channel = client.get_channel(Ton ID Du Cannal De Texte (le même que le précédent))
        await channel.purge(limit=500)


client.run('Ton Token De Bot')