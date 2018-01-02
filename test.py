import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import time


Client = discord.Client()  
client = commands.Bot(command_prefix = "?") 


@client.event 
async def on_ready():
    print("Bot is online and connected to Discord") 

@client.event
async def on_message(message):
    if message.content == "?cookie":
        await client.send_message(message.channel, ":cookie:")

@client.event
async def on_message(message):
    if message.content.startswith('?progress'):
        embed = discord.Embed(title="PROGRESS", description="This bot is 0.37% complete", color=0x00ff00)
        await client.send_message(message.channel, embed=embed)


@client.event
async def on_message(message):
    if message.content.startswith('?greet'):
        await client.send_message(message.channel, 'Say hello')
        msg = await client.wait_for_message(author=message.author, content='hello')
        await client.send_message(message.channel, 'Hello.')


@client.event
async def on_ready():
    await client.change_presence(game=discord.Game(name='WIP | Prefix - ?'))



    
        


        

        
    
client.run("Mzk3Njk0NjM0NzA2NDY4ODY0.DSz_wQ.wSd8D6TkHv8WLrq4c4SmzYBMZ9Q")
