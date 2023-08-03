
import discord

# ayricaliklar (intents) değişkeni botun ayrıcalıklarını depolayacak
intents = discord.Intents.default()
# Mesajları okuma ayrıcalığını etkinleştirelim
intents.message_content = True
# client (istemci) değişkeniyle bir bot oluşturalım ve ayrıcalıkları ona aktaralım
client = discord.Client(intents=intents)
from bot_mantık import gen_pass

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')


@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('hello'):
        await message.channel.send("Hi!")
    elif message.content.startswith('bye'):
        await message.channel.send("Keşke oyun gelsen")
    elif message.content.startswith('nasılsın'):
        await message.channel.send("iyi")
    elif message.content.startswith('merhaba'):
        await message.channel.send("merhaba")
    elif message.content.startswith('sen bir botsun'):
        await message.channel.send("bu doğru")
    elif message.content.startswith('şifre'):
        await message.channel.send(gen_pass[10])
    else:
        await message.channel.send(message.content)

client.run("MTEzNjY5ODgwOTQ3MzMwNjcyNA.GXmSgR.ir46A6xxdr5Arfs3V1L5o6wLfXyBgSD43CBL9w")