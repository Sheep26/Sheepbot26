import time
import discord
import json
import random
from discord import app_commands
from discord.ext import commands
import datetime
import string
import yt_dlp
import asyncio
bot = commands.Bot(command_prefix=".", intents = discord.Intents.all())
activity = ""
startTime = time.time()
songs = []
blockedWords = []
dogwaterWords = []
email = ["gmail.com", "hotmail.com", "outlook.com", "oatlocker.com", "yahoo.co.nz", "oatlocker.com", "deeznuts.com", "gmail.com", "yahoo.co.nz", "outlook.com", "gmail.com"]
token: str

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

with open('config.json') as  f:
    data1 = json.load(f)
for data in data1['token']:
    token = data
for data in data1['Activity']:
    activity = data
for data in data1['dogwater']:
    dogwaterWords.append(data)
for data in data1["blocked-words"]:
    blockedWords.append(data)

@bot.tree.command(name='dogwater', description = "Ur dogwater kid")
async def dogwater(interaction: discord.Interaction, user: discord.User):
    await interaction.response.send_message(f"{(str (random.choice(dogwaterWords))).format(name = user.name)}")

@bot.tree.command(name='dmme', description = "Dms you")
async def dmme(interaction: discord.Interaction, what: str):
    user = bot.get_user(interaction.user.id)
    await user.send(what)
    await interaction.response.send_message(f"Done", ephemeral=True)

@bot.tree.command(name='heck', description = "Heck")
async def heck(interaction: discord.Interaction, user: discord.User):
    letters: str = ""
    for x in range(10):
        letters = letters + random.choice(string.ascii_lowercase + string.ascii_uppercase + string.digits)
    email1 = random.choice(email)
    heck_embed=discord.Embed(title=f"Hecked {user.name}", color=discord.Color.blue())
    heck_embed.add_field(name='Email', value=f"{user.name}{letters[0]}{letters[1]}{letters[2]}{letters[3]}@{email1}", inline=True)
    heck_embed.add_field(name='Password', value=f"{letters}", inline=True)
    await interaction.response.send_message(embed=heck_embed)

@bot.tree.command(name='rat', description = "Responds with rat?")
async def rat(interaction: discord.Interaction):
    await interaction.response.send_message("Rat?")
    
@bot.tree.command(name='ping', description = "Check the bots ping")
async def ping(interaction: discord.Interaction):
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
async def play(interaction: discord.Interaction, song: str):
    try :
        await interaction.response.defer(thinking = True)
        guild = interaction.guild
        voice_channel = guild.voice_client
        try:
            filename = await YTDLSource.from_url(song, loop=bot.loop)
        except:
            await interaction.followup.send('Failed to download music')
        try:
            voice_channel.play(discord.FFmpegPCMAudio(source=filename))
            music_name: str = filename
            music_name = music_name.replace("-", " ")
            music_name = music_name.replace("_", " ")
            music_name = music_name.replace(".webm", "")
            music_embed=discord.Embed(title='**Now playing:** {}'.format(music_name), color=discord.Color.blue())
            await interaction.followup.send(embed=music_embed)
        except:
            await interaction.followup.send('Failed to play music')
    except:
        await interaction.followup.send("The bot is not connected to a voice channel.")

@bot.tree.command(name='leave', description = "Leaves vc")
async def leave(interaction: discord.Interaction):
    guild = interaction.guild
    vc = guild.voice_client

    if vc:
        vc.cleanup()
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
        
@bot.tree.command(name='uptime', description = "Gets the bots uptime")
async def uptime(interaction: discord.Interaction):
    await interaction.response.send_message("The bots uptime is {}".format(get_uptime()))
        
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
async def on_message(message):
    if message.author == bot.user:
        return
    if message.content == "ok":
        await message.channel.send("ok")

@bot.event
async def on_ready():
    if not activity == None:
        activity = discord.Game(name=activity)
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

def main():
    if token == None or token == "":
        print("No token, please provide a bot token")
        return
    bot.run(token)

if __name__ == "__main__":
    main()