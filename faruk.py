import discord
from discord.ext import commands
from bot_mantik import gen_pass
import random
import os
print(os.listdir('resimler'))
img_name = os.listdir('resimler')




a = random.randint(1, 2)

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)


@bot.command()
async def link(ctx):
    await ctx.send(f'https://www.youtube.com/watch?v=uZpMmP5EUEI')



@bot.event
async def on_ready():
    print(f'{bot.user} olarak giriş yaptık')

@bot.command()
async def bye(ctx):
    await ctx.send(f'Görüşürüz {bot.user}!')

@bot.command()
async def nasilsin(ctx):
    await ctx.send(f'İyiyim {bot.user}! teşekkürler')

@bot.command()
async def merhaba(ctx):
    await ctx.send(f'Merhaba {bot.user}!')

@bot.command()
async def sen_bir_botsun(ctx):
    await ctx.send(f'salak {bot.user}! sen bir botsun!')

@bot.command()
async def sifre(ctx):
    await ctx.send(gen_pass(8))

@bot.command()
async def joined(ctx, member: discord.Member):
    """Says when a member joined."""
    await ctx.send(f'{member.name} joined {discord.utils.format_dt(member.joined_at)}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Merhaba {bot.user}! Ben bir botum!')

@bot.command()
async def heh(ctx, count_heh = 100):
    await ctx.send("he" * count_heh)



@bot.command()
async def yazi_tura(ctx):
    await ctx.send(f'{bot.user}! yazı mıtura mı?')

@bot.command()
async def tura(ctx):
    if a == 1:
        await ctx.send(f'Evet {bot.user}! Bildin!')
    elif a != 1:
        await ctx.send(f'Hayır {bot.user}! Bilemedin!')
    


@bot.command()
async def yazi(ctx):

    if a == 2:
        await ctx.send(f'Evet {bot.user}! Bildin!')
    elif a != 2:
        await ctx.send(f'Hayır {bot.user}! Bilemedin!')


@bot.event
async def on_member_join(member):
        guild = member.guild
        if guild.system_channel is not None:
            to_send = f'Welcome {member.mention} to {guild.name}!'
            await guild.system_channel.send(to_send)

@bot.command()
async def mem(ctx):
        a = random.randint(1,10)
        # Dosya adını bir değişkenden bu şekilde değiştirebilirsiniz!
        if a == 1 or a == 2:
            with open('resimler/mem1.jpg', 'rb') as f:
                picture = discord.File(f)
            # Daha sonra bu dosyayı bir parametre olarak gönderebiliriz!
            await ctx.send(file=picture)
        if a == 3 or a == 4 or a == 5:
            with open('resimler\mem2.png', 'rb') as f:
                picture = discord.File(f)
            # Daha sonra bu dosyayı bir parametre olarak gönderebiliriz!
            await ctx.send(file=picture)
        if a == 6:
            with open('resimler\mem3.jpg', 'rb') as f:
                picture = discord.File(f)
            # Daha sonra bu dosyayı bir parametre olarak gönderebiliriz!
            await ctx.send(file=picture)
        if a == 7 or a == 8:
            with open('resimler\mem4.png', 'rb') as f:
                picture = discord.File(f)
            # Daha sonra bu dosyayı bir parametre olarak gönderebiliriz!
            await ctx.send(file=picture)
        if a == 9 or a == 10:
            with open('resimler\mem5.png', 'rb') as f:
                picture = discord.File(f)
            # Daha sonra bu dosyayı bir parametre olarak gönderebiliriz!
            await ctx.send(file=picture)





bot.run("MTEzNjY5ODgwOTQ3MzMwNjcyNA.GKbPAJ.T00Mp155o01l4ipSc8J7II-oGHH1b7JVt4MLUg")
