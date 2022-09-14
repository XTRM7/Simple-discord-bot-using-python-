import discord
from PIL import Image

key="Your Token Code"


intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)
 


@client.event
async def on_connect():
    print("BOT ONLINE")

@client.event
async def on_message(message):
    
    if message.content.startswith("&sen"):
      await message.channel.send("Procchur match ache amar", file=discord.File('sagarsen.jpg'))
    if message.content.startswith("&hyper"):
      await message.channel.send("Kiit jbo")
    if message.content.startswith("&sayantan"):
      await message.channel.send("Sayantan Stupid", file=discord.File('sayantan.jpg'))
    if message.content.startswith("&reisr"):
      await message.channel.send("Procchur exam ase")
    if message.content.startswith("&mercy"):
      await message.channel.send("baje na boke biye ta kor", file=discord.File('souravdas.png'))
    if message.content.startswith("&dark"):
      await message.channel.send("Tower er chele", file=discord.File('tower.jpg'))
    if message.content.startswith("&ace"):
      await message.channel.send("Grilled chicken with gache jol")
    if message.content.startswith("&bricktop"):
      await message.channel.send("Just awesome", file=discord.File('devstrike.gif'))
    if message.content.startswith("&sniper"):
      await message.channel.send('Best Best', file=discord.File('busted.png'))
    if message.content.startswith("&albedo"):
      await message.channel.send('Best Best')

      
      


client.run(key)
