import discord
from discord.ext import commands

bot = commands.Bot(command_prefix="!")

@bot.command()
async def add(ctx, a: int, b: int):
    await ctx.send(a+b)

@bot.command()
async def subtract(ctx, a: int, b: int):
    await ctx.send(a-b)

@bot.command()
async def multiply(ctx, a: int, b: int):
    await ctx.send(a*b)

@bot.command()
async def divide(ctx, a: int, b: int):
    if b == 0:
        await ctx.send("Error: Division by zero is undefined.")
    else:
        await ctx.send(a/b)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

bot.run('your-token-here')
