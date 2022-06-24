import discord
from discord.ext import commands
import json, os
from dotenv import load_dotenv
with open('setting.json', 'r', encoding='utf8') as settingFile:
    settingData = json.load(settingFile)

# load env
load_dotenv()

bot = commands.Bot(command_prefix = 'yo!')

@bot.event
async def on_ready():
    print(">> Bot is online <<")

@bot.event
async def on_member_join(member):
    channel = bot.get_chennel(int(settingData['Testing_channel']))
    await channel.send(F'{member} join!')

@bot.event
async def on_member_remove(member):
    channel = bot.get_chennel(int(settingData['Testing_channel']))
    await channel.send(F'{member} leave!')

@bot.command()
async def load(ctx, extension):
    bot.load_extension(f'cmds.{extension}')
    await ctx.send(f'Loaded {extension} done.')

@bot.command()
async def unload(ctx, extension):
    bot.unload_extension(f'cmds.{extension}')
    await ctx.send(f'Un - Loaded {extension} done.')

@bot.command()
async def reload(ctx, extension):
    bot.reload_extension(f'cmds.{extension}')
    await ctx.send(f'Re - Loaded {extension} done.')



for Filename in os.listdir('./cmds'):
    if Filename.endswith('.py'):
        bot.load_extension(f'cmds.{Filename[:-3]}')

if __name__ == "__main__":
    bot.run(os.getenv("TOKEN"))
