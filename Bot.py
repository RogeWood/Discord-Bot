import discord
from discord.ext import commands

bot = commands.Bot(command_prefix = '#')

@bot.event
async def on_ready():
    print(">> Bot is online <<")
    

@bot.event
async def on_member_join(member):
    print(F'{member} join!')

@bot.event
async def on_member_remove(member):
    print(F'{member} leave!')

bot.run("NjU3ODk5NzEzNTAwMDIwNzM5.Xf9FTA.KVdSIUaK7WhfPbivw9TVUWiAC7A")
