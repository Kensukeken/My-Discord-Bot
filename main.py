```py
import discord
from discord.ext import commands
import random

# Description for the bot
description = '''Hello! I'm here to help you with various commands.
Check out the utility commands and have fun!'''

# Set up bot with custom command prefix 'k!'
intents = discord.Intents.default()
intents.members = True
bot = commands.Bot(command_prefix='k!', description=description, intents=intents)



# Event triggered when the bot is ready
@bot.event
async def on_ready():
    print(f'Logged in as {bot.user} (ID: {bot.user.id})')
    print('------')


@bot.command()
async def add(ctx, *args):
    """Adds two numbers together.

    Usage: k!add <left> <right>
    Example: k!add 5 10
    """
    if len(args) != 2:
        await ctx.send("Usage: k!add <left> <right>")
        return

    try:
        left = int(args[0])
        right = int(args[1])
    except ValueError:
        await ctx.send("Invalid input. Please provide two integer values.")
        return

    result = left + right
    await ctx.send(f"The result of {left} + {right} is {result}")
  
# Command: Rolls a dice in NdN format
@bot.command()
async def roll(ctx, dice: str):
    """Rolls a dice in NdN format."""
    try:
        rolls, limit = map(int, dice.split('d'))
    except Exception:
        await ctx.send('Format has to be in NdN!')
        return

    result = ', '.join(str(random.randint(1, limit)) for r in range(rolls))
    await ctx.send(result)

# Provide custom help for the roll command
bot.get_command('roll').help = "Rolls a dice in NdN format.\n\nExample: k!roll 2d6"


# Command: Chooses between multiple choices
@bot.command(description='For when you wanna settle the score some other way')
async def choose(ctx, *, choices: str):
    """Chooses between multiple choices."""
    choice_list = choices.split(" or ")
    await ctx.send(random.choice(choice_list))


# Command: Repeats a message multiple times
@bot.command()
async def repeat(ctx, times: int, *, content='repeating...'):
    """Repeats a message multiple times."""
    for i in range(times):
        await ctx.send(content)

# Music Command: Play a song in a voice channel
@bot.command()
async def play(ctx, song=None):
    """Play a song in a voice channel."""
    if song is None:
        await ctx.send("Please provide a song name.")
    else:
        await ctx.send(f'Now playing: {song}')
      
# Event triggered when a user enters a voice channel
@bot.event
async def on_voice_state_update(member, before, after):
    # Placeholder: Implement voice state update logic here
    # For example, announce when a user joins a voice channel
    pass

# Replace 'YOUR_ACTUAL_BOT_TOKEN' with your bot's actual token
bot.run('your_token')
```
