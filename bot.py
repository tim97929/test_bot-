import discord
from discord.ext import commands
bot = commands.Bot(command_prefix='[')

@bot.event
async def on_ready():
   print(">>bot is online<<")

bot.run('ODg5NzU1OTY0MjI2NTQ3NzUy.YUl30A.qfa3svRkRM0DJEOg0eoyhnkkZRc')