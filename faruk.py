import discord
from discord.ext import commands
from bot_mantik import gen_pass
import random
a = random.randint(1, 2)

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)


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
    await ctx.send(f'Evet {bot.user}! Ben bir botum!')

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
async def heh(ctx, count_heh = 5):
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











@bot.command()
async def sen_bir_botsun(ctx):
    await ctx.send(f'Evet {bot.user}! Ben bir botum!')


bot.run("Token")
