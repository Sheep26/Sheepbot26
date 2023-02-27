import time
import discord
import json
import random
from discord import app_commands
from discord.ext import commands
from os import system, name
import datetime
import subprocess
import yt_dlp
import asyncio
bot = commands.Bot(command_prefix=".", intents = discord.Intents.all())
gamename = ""
server = False
startTime = 0
sus1 = ["is sus", "was ejected", "is so sus that he got sent out to space", "is the sussiest person alive"]
insults = ["is trash", "sucks", "is stupid", "is the dumbest person alive", "is the fattest person alive", "bro your so dogwater noone would ever want you on there team", "is even more trash than the trash i took out last night", "was a accident", "had a brick drop on their head when they were born", "is a chicken", "is fat"]
songs = []
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

yt_dlp.utils.bug_reports_message = lambda: ''

ytdl_format_options = {
    'format': 'bestaudio/best',
    'restrictfilenames': True,
    'noplaylist': True,
    'nocheckcertificate': True,
    'ignoreerrors': False,
    'logtostderr': False,
    'quiet': False,
    'no_warnings': True,
    'default_search': 'auto',
    'source_address': '0.0.0.0' # bind to ipv4 since ipv6 addresses cause issues sometimes
}

ffmpeg_options = {
    'options': '-vn'
}

ytdl = yt_dlp.YoutubeDL(ytdl_format_options)

class YTDLSource(discord.PCMVolumeTransformer):
    def __init__(self, source, *, data, volume=0.5):
        super().__init__(source, volume)
        self.data = data
        self.title = data.get('title')
        self.url = ""

    @classmethod
    async def from_url(cls, url, *, loop=None, stream=False):
        loop = loop or asyncio.get_event_loop()
        data = await loop.run_in_executor(None, lambda: ytdl.extract_info(url, download=not stream))
        if 'entries' in data:
                # take first item from a playlist
            data = data['entries'][0]
        filename = data['title'] if stream else ytdl.prepare_filename(data)
        return filename

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
for data in data1['WebServer']:
    server = data

@bot.tree.command(name='dogwater', description = "Ur dogwater kid")
@app_commands.describe(who = "who is dogwater")
async def dogwater(interaction: discord.Interaction, who: str):
    global dog
    dog = random.choice(dog1)
    await interaction.response.send_message(f"{who} {dog}")

@bot.tree.command(name="insult", description = "Insults people")
@app_commands.describe(who = "who")
async def insult(interaction: discord.Interaction, who: str):
    global insults
    ins = random.choice(insults)
    await interaction.response.send_message(f"{who} {ins}")

@bot.tree.command(name='sus', description = "Amongus")
@app_commands.describe(who = "who is sus")
async def sus(interaction: discord.Interaction, who: str):
    global sus1
    sus2 = random.choice(sus1)
    await interaction.response.send_message(f"{who} {sus2}")
    
"""@bot.tree.command(name='embed', description = "Random embed")
async def embed(interaction: discord.Interaction):
    test_embed=discord.Embed(title="random Embed", url="https://google.com ",description="random description" , color=discord.Color.blue())
    test_embed.add_field(name='random field', value="random value", inline=True)
    await interaction.response.send_message(embed=test_embed)"""

@bot.tree.command(name='heck', description = "Heck")
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
    heck_embed=discord.Embed(title=f"Hecked {who}", color=discord.Color.blue())
    heck_embed.add_field(name='Email', value=f"{who}{number}@{email1}", inline=True)
    heck_embed.add_field(name='Password', value=f"{letters}", inline=True)
    await interaction.response.send_message(embed=heck_embed)

@bot.tree.command(name='rat', description = "Responds with rat?")
async def rat(interaction: discord.Interaction):
    await interaction.response.send_message("Rat?")
    
@bot.tree.command(name='ping', description = "Check the bots ping")
async def rat(interaction: discord.Interaction):
     await interaction.response.send_message(f"The bots ping is {round(bot.latency * 1000)}ms")
    
@bot.tree.command(name='join', description = "Joins vc")
async def join(interaction: discord.Interaction):
    if interaction.user.voice is not None:
        vc = interaction.user.voice.channel
        voice = await vc.connect()
        await interaction.response.send_message("Joining voice channel")
    else:
        await interaction.response.defer(ephemeral=True)
        await interaction.followup.send("You are not in a voice channel.")
        return

@bot.tree.command(name='play', description = "Plays music")
@app_commands.describe(song = "song")
async def play(interaction: discord.Interaction, song: str):
    try :
        await interaction.response.defer(thinking = True)
        guild = interaction.guild
        voice_channel = guild.voice_client
        
        try:
            filename = await YTDLSource.from_url(song, loop=bot.loop)
        except:
            await interaction.followup.send('Failed to download music')
            return
        try:
            voice_channel.play(discord.FFmpegPCMAudio(executable="ffmpeg.exe", source=filename))
            music_name: str = filename
            music_name = music_name.replace("-", " ")
            music_name = music_name.replace("_", " ")
            music_name = music_name.replace(".webm", "")
            music_embed=discord.Embed(title='**Now playing:** {}'.format(music_name), color=discord.Color.blue())
            await interaction.followup.send(embed=music_embed)
        except:
            await interaction.followup.send('Failed to play music')
            return
    except:
        await interaction.response.send_message("The bot is not connected to a voice channel.")

@bot.tree.command(name='leave', description = "Leaves vc")
async def leave(interaction: discord.Interaction):
    guild = interaction.guild
    vc = guild.voice_client

    if vc:
        await vc.disconnect()
        await interaction.response.send_message('Leaving voice channel')
    else:
        await interaction.response.send_message("The bot isn't in the voice channel")
        
@bot.tree.command(name='pause', description = "Pauses music")
async def pause(interaction: discord.Interaction):
    guild = interaction.guild
    voice_channel = guild.voice_client
    try :
        await interaction.response.send_message("Paused the music.")
        voice_channel.pause()
    except:
        await interaction.response.send_message("The bot is not playing anything at the moment.")
        
@bot.tree.command(name='resume', description = "Resumes music")
async def resume(interaction: discord.Interaction):
    guild = interaction.guild
    voice_channel = guild.voice_client
    try:
        await interaction.response.send_message("Resumed the music.")
        await voice_channel.resume()
    except:
        await interaction.response.send_message("The bot is not playing anything at the moment.")
        
@bot.tree.command(name='stop_music', description = "Stops music")
async def stop_music(interaction: discord.Interaction):
    guild = interaction.guild
    voice_channel = guild.voice_client
    if voice_channel.is_playing():
        await interaction.response.send_message("Stopping the music.")
        voice_channel.stop()
    else:
        await interaction.response.send_message("The bot is not playing anything at the moment.")

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

def get_uptime_sec():
    return (round(time.time()-startTime))

def logout():
    bot.close()
    print("Logging out bot")

startTime = time.time()

if __name__ == '__main__':
    if server == True:
        subprocess.Popen("server.py", shell=True)
    bot.run(token)
