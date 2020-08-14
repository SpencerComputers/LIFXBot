from discord.ext import commands
import discord, requests, json

bot = commands.Bot(command_prefix="!", status=discord.Status.idle, activity=discord.Game(name="Preparing the lighting goodness"))
lifxtoken = "LIFX TOKEN HERE"
headers = {
    "Authorization": "Bearer %s" % lifxtoken,
    }

bot.remove_command("help")

@bot.event
async def on_ready():
    print("Ready to go!")
    print(f"Serving: {len(bot.guilds)} guilds.")
    await bot.change_presence(status=discord.Status.online, activity=discord.Game(name="Ready to change lights!"))

@bot.command()
async def toggle(ctx):
    response1 = requests.get('https://api.lifx.com/v1/lights/group:Bedroom/state', headers=headers)
    response2 = requests.post('https://api.lifx.com/v1/lights/all/toggle', headers=headers)
    embed_toggle = discord.Embed(title='Toggled the lights 🏡', description=f'Turned the lights **ON**', color=0x22ff00)
    await ctx.send(embed=embed_toggle)

@bot.command()
async def night(ctx):
    scene = '7d2a06f5-72ae-4b62-a571-f2b21c2fe71e'
    response = requests.put('https://api.lifx.com/v1/scenes/scene_id:%s/activate' % scene, headers=headers)
    await ctx.channel.send("Set the theme to night 🌙")

@bot.command()
async def morning(ctx):
    scene = '04b67d21-e26b-47de-b8fa-02a1c529988c'
    response = requests.put('https://api.lifx.com/v1/scenes/scene_id:%s/activate' % scene, headers=headers)
    await ctx.channel.send("Set the theme to morning ☀️")
    
bot.run('DISCORD TOKEN HERE')