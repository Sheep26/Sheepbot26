import time
import discord
import json
import random
from discord import app_commands
from discord.ext import commands
from os import system, name
import datetime
import subprocess
bot = commands.Bot(command_prefix=".", intents = discord.Intents.all())
gamename = ""
startTime = 0
sus1 = ["is sus", "was ejected", "is so sus that he got sent out to space", "is the sussiest person alive"]
insults = ["is trash", "sucks", "is stupid", "is the dumbest person alive", "is the fattest person alive", "bro your so dogwater noone would ever want you on there team", "is even more trash than the trash i took out last night", "was a accident", "had a brick drop on their head when they were born", "is a chicken", "is fat"]
dog1 = [
    "is dogwater",
    "bro your so dogwater noone would ever want you on there team",
    "is trash att every game in existance", "is trash", "fell into dogwater",
    "is even more trash than the trash i took out last night",
  "is dogwater",
  "drank dogwater"
]
dog = 0
email = ["gmail.com", "hotmail.com", "outlook.com", "oatlocker.com", "yahoo.co.nz", "oatlocker.com", "deeznuts.com", "gmail.com", "yahoo.co.nz", "outlook.com", "gmail.com"]
number = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
letter = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "f", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "A", "b", "C", "E", "F", "G", "H", "I", "F", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
#, ephemeral=True
def clear():
    if name == 'nt':
        system('cls')
    else:
        system('clear')
with open('config.json') as  f:
    data1 = json.load(f)
for data in data1['token']:
    token = data
for data in data1['insults']:
    insults.append(data)
for data in data1['gameName']:
    gamename = data

@bot.tree.command(name='dogwater')
@app_commands.describe(who = "who is dogwater")
async def dogwater(interaction: discord.Interaction, who: str):
    global dog
    dog = random.choice(dog1)
    await interaction.response.send_message(f"{who} {dog}")

@bot.tree.command(name="insult")
@app_commands.describe(who = "who")
async def insult(interaction: discord.Interaction, who: str):
    global insults
    ins = random.choice(insults)
    await interaction.response.send_message(f"{who} {ins}")

@bot.tree.command(name='sus')
@app_commands.describe(who = "who is sus")
async def sus(interaction: discord.Interaction, who: str):
    global sus1
    sus2 = random.choice(sus1)
    await interaction.response.send_message(f"{who} {sus2}")
    
@bot.tree.command(name='embed')
async def embed(interaction: discord.Interaction):
    test_embed=discord.Embed(title="random Embed", url="https://google.com ",description="random description" , color=discord.Color.blue())
    test_embed.add_field(name='random field', value="random value", inline=True)
    await interaction.response.send_message(embed=test_embed)

@bot.tree.command(name='heck')
@app_commands.describe(who = "who")
async def heck(interaction: discord.Interaction, who: str):
    letters = random.choice(letter)
    letters = letters + random.choice(letter)
    letters = letters + random.choice(letter)
    letters = letters + random.choice(letter)
    letters = letters + random.choice(letter)
    letters = letters + random.choice(letter)
    letters = letters + random.choice(letter)
    letters = letters + random.choice(letter)
    letters = letters + random.choice(letter)
    letters = letters + random.choice(letter)
    letters = letters + random.choice(letter)
    letters = letters + random.choice(letter) 
    number = random.choice(letter)
    number = number + random.choice(letter)
    number = number + random.choice(letter)
    email1 = random.choice(email)
    heck_embed=discord.Embed(title=f"Hecked {who}", color=discord.Color.red())
    heck_embed.add_field(name='Email', value=f"{who}{number}@{email1}", inline=True)
    heck_embed.add_field(name='Password', value=f"{letters}", inline=True)
    await interaction.response.send_message(embed=heck_embed)

@bot.tree.command(name='rat')
async def rat(interaction: discord.Interaction):
    await interaction.response.send_message("https://www.youtube.com/watch?v=vdVnnMOTe3Q")

@bot.event
async def on_ready():
    activity = discord.Game(name=gamename)
    await bot.change_presence(status=discord.Status.online, activity=activity)
    try:
        synced = await bot.tree.sync()
        print(f'Synced {len(synced)} commands')
    except Exception as e:
        print(e)
    
def get_uptime():
    return str(datetime.timedelta(seconds=int(round(time.time()-startTime))))

def logout():
    bot.close()
    print("Logging out bot")

startTime = time.time()

if __name__ == '__main__':
    subprocess.Popen("server.py", shell=True)
    bot.run(token)