import discord
import random
import time

# ayricaliklar (intents) de�i�keni botun ayr�cal�klar�n� depolayacak
intents = discord.Intents.default()
# Mesajlar� okuma ayr�cal���n� etkinle�tirelim
intents.message_content = True
# client (istemci) de�i�keniyle bir bot olu�tural�m ve ayr�cal�klar� ona aktaral�m
while True:
    a  =   random.randint (1,2)
    time.sleep(0.1)


    from bot_mantik import gen_pass

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
        if message.content.startswith('hello'):
            await message.channel.send("Hi!")
        elif message.content.startswith('bye'):
            await message.channel.send("Ke�ke oyun gelsen")
        elif message.content.startswith('nasilsin'):
            await message.channel.send("iyiyim ya sen?")
        elif message.content.startswith('merhaba'):
            await message.channel.send("merhaba")
        elif message.content.startswith('sen bir botsun'):
            await message.channel.send("bu do�ru")
        elif message.content.startswith('sifre'):
            await message.channel.send(gen_pass(8))
        elif message.content.startswith('iyiyim te�ekk�rler'):
            await message.channel.send('rica ederim') 
        
        
        elif message.content.startswith('yazi tura'):
            random_result = random.randint(1, 2)
            await message.channel.send('yazi mi? tura mi?')
        elif message.content.startswith('tura'):
            if a == 1:
                await message.channel.send('bildin')
            elif a != 1:
                await message.channel.send('bilemedin')
        
        
        elif message.content.startswith('yazi'):
            if a == 2:
                await message.channel.send('bildin')
            elif a != 2:
                await message.channel.send('bilemedin')



    
        """else:
            await message.channel.send(message.content)"""

    client.run("MTEzNjY5ODgwOTQ3MzMwNjcyNA.GPE-zf.DJyty2LLgIXBPRKdkqOLGlx1tP2n6oeTmexQPU")