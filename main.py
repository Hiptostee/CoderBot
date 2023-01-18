import discord
import os
import json
import random
from discord.ext import commands
from code import codify, decodify
from keep_alive import keep_alive
from discord_ui import UI, SelectMenu, SelectOption

from asyncio import TimeoutError
intents = discord.Intents.default()
intents.members = True
intents.presences = True

client = commands.Bot(command_prefix = "!", intents = intents)

@client.event
async def on_ready():
  print("Bot is Online")

@client.command()
async def code(ctx, *,  self):
  await ctx.channel.send(codify(str(self.lower())))
  
@client.command()
async def decode(ctx, *, self):
  await ctx.channel.send(decodify(str(self.lower())))
  
@client.command()
async def DM(ctx, user: discord.Member, *, message=None):
  message = codify(message)
  await user.send(message)
  await user.send(f"Sent from {ctx.message.author}")
  await ctx.message.delete()
@client.command()
async def pushups(ctx):
  
  
    rando = random.randint(1,100)
    if rando % 10 ==0:
      isGiveAway = "Yes"
    else:
      isGiveAway = "No"
    await ctx.channel.send("PUSHUPS: " +  str(random.randint(1, 25)))
    await ctx.channel.send("GIVE AWAY?: " + isGiveAway )
  
    
  
# @client.command()
# async def checklist(ctx):
#   with open("check.json", "r") as file:
#     data = json.load(file)
#     if ctx.author.id in data.keys():
#       return
#     else:
#       with open("check.json", "w") as file:
#           dict_key = ctx.author.id
#           dict_value = "My checklist!"
#           data[dict_key] = dict_value
#           json.dump(data, file)

# @client.command()
# async def checklist_view(ctx):
#   with open("check.json", "r") as file:
#     data = json.load(file)
#     pretty = json.dumps(data, indent=4, sort_keys=True)
#     await ctx.channel.send(pretty)
    
# @client.command()
# async def add_item(ctx, *self):
#   await ctx.channel.send("")
#   list = []
#   #await ctx.channel.send("To tell me the thing you would like to add to your checklist, please type the item and then the date like: item = clean the dishes, date = 10/4/22")
#   for i in range(0, len(self)):
#     list.append(self[i])
#   new_task = " ".join(list)
#   print(' '.join(new_task.split("item =")).split("time ="))


# @client.command()
# async def buttons():
#   msg = await message.channel.send("you", components=[SelectMenu(options=[
#       SelectOption("my_value", label="test", description="this is a test"),
#       SelectOption("my_other_value", emoji="🤗", description="this is a test too")
#   ], max_values=2)])
#   try:
#       sel = await msg.wait_for("select", client, by=message.author, timeout=20)
#       await sel.respond("you selected `" + str([x.content for x in sel.selected_options]) + "`")
#   except TimeoutError:
#       await msg.delete()






    
keep_alive()
client.run(os.getenv("TOKEN"))

