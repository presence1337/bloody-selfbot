VERSION = "1.0.0"
TOTAL_COMMANDS = "37"
TOTAL_LINES = "409"

import discord, ctypes, json, os, webbrowser, requests, datetime, urllib, time, string, random, asyncio, aiohttp
from discord.ext import commands
from colorama import Fore, Back, Style
from selenium import webdriver

with open("config.json") as f:
    config = json.load(f)

TOKEN = config.get("token")
PREFIX = config.get("prefix")

def ready():
    print(f"""
                    ┌┐   ┬    ┌─┐  ┌─┐  ┌┬┐  ┬ ┬
                    {Fore.BLACK}{Style.BRIGHT}├┴┐  │    │ │  │ │   ││  └┬┘{Style.RESET_ALL}{Fore.RESET}
                    {Fore.RED}└─┘  ┴─┘  └─┘  └─┘  ─┴┘   ┴ {Fore.RESET}

                        {Fore.RED}────────────────────{Fore.RESET}
                            Servers: {Fore.RED}[{Fore.RESET}{len(Bloody.guilds)}{Fore.RED}]{Fore.RESET}
                            Friends: {Fore.RED}[{Fore.RESET}{len(Bloody.user.friends)}{Fore.RED}]{Fore.RESET}
                            Prefix:  {Fore.RED}[{Fore.RESET}{PREFIX}{Fore.RED}]{Fore.RESET}
                        {Fore.RED}────────────────────{Fore.RESET}
    """+Fore.RESET)

def Nitro():
    code = "".join(random.choices(string.ascii_letters + string.digits, k=16))
    return f"https://discord.gift/{code}"

def RandomColor(): 
    randcolor = discord.Color(random.randint(0x000000, 0xFFFFFF))
    return randcolor

def RandString():
    return "".join(random.choice(string.ascii_letters + string.digits) for i in range(random.randint(4, 4)))

client = commands.Bot(
    command_prefix=PREFIX,
    self_bot=True
)
Bloody = client

@Bloody.event
async def on_message_edit(before, after):
    await Bloody.process_commands(after)

@Bloody.event
async def on_connect():
    os.system("mode con: cols=70 lines=21")
    ctypes.windll.kernel32.SetConsoleTitleW(f"Bloody Selfbot | Version {VERSION} | Logged In As: {Bloody.user.name}")
    ready()

#=================================| Fun Commands |=================================#

@Bloody.command(name='8ball')
async def _ball(ctx, *, question):
    responses = [
        'As I see it, yes.',
        'Ask again later.',
        'Better not tell you now.',
        'Cannot predict now.',
        'Concentrate and ask again.',
        'Don’t count on it.',
        'It is certain.',
        'It is decidedly so.',
        'Most likely.',
        'My reply is no.',
        'My sources say no.',
        'Outlook not so good.',
        'Outlook good.',
        'Reply hazy, try again.',
        'Signs point to yes.',
        'Very doubtful.',
        'Without a doubt.',
        'Yes.',
        'Yes – definitely.',
        'You may rely on it.'
    ]
    answer = random.choice(responses)
    embed = discord.Embed(color=RandomColor())
    embed.add_field(name="**Question:**", value=f"```{question}```", inline=False)
    embed.add_field(name="**Answer:**", value=f"```{answer}```", inline=False)
    embed.set_author(name="8 Ball Machine", icon_url="https://pngriver.com/wp-content/uploads/2018/03/Download-8-Ball-Pool-PNG-Photos-For-Designing-Projects.png") 
    await ctx.send(embed=embed)

@Bloody.command()
async def ascii(ctx, *, text):
    await ctx.message.delete()
    r = requests.get(f"http://artii.herokuapp.com/make?text={urllib.parse.quote_plus(text)}").text
    if len("```"+r+"```") > 2000:
        return
    await ctx.send(f"```{r}```")

@Bloody.command()
async def slap(ctx, user: discord.Member):
    r = requests.get("https://nekos.life/api/v2/img/slap")
    res = r.json()
    embed = discord.Embed(description=f"**{ctx.author.mention} Slaps {user.mention}**", color=RandomColor())
    embed.set_image(url=res["url"])
    await ctx.send(embed=embed)

@Bloody.command()
async def hug(ctx, user: discord.Member):
    r = requests.get("https://nekos.life/api/v2/img/hug")
    res = r.json()
    embed = discord.Embed(description=f"**{ctx.author.mention} Hugs {user.mention}**", color=RandomColor())
    embed.set_image(url=res["url"])
    await ctx.send(embed=embed)

@Bloody.command()
async def kiss(ctx, user: discord.Member):
    r = requests.get("https://nekos.life/api/v2/img/kiss")
    res = r.json()
    embed = discord.Embed(description=f"**{ctx.author.mention} Kisses {user.mention}**", color=RandomColor())
    embed.set_image(url=res["url"])
    await ctx.send(embed=embed)

@Bloody.command()
async def cat(ctx):
    r = requests.get("https://some-random-api.ml/img/cat").json()
    embed = discord.Embed(color=RandomColor())
    embed.set_author(name="Here Is The Cat You Requested", icon_url="https://i.stack.imgur.com/DTCra.png") 
    embed.set_image(url=str(r["link"]))
    await ctx.send(embed=embed)

@Bloody.command()
async def dog(ctx):
    r = requests.get("https://some-random-api.ml/img/dog").json()
    embed = discord.Embed(color=RandomColor())
    embed.set_author(name="Here Is The Dog You Requested", icon_url="http://clipart-library.com/images_k/dog-bone-silhouette/dog-bone-silhouette-1.png") 
    embed.set_image(url=str(r["link"]))
    await ctx.send(embed=embed)

@Bloody.command()
async def panda(ctx):
    r = requests.get("https://some-random-api.ml/img/panda").json()
    embed = discord.Embed(color=RandomColor())
    embed.set_author(name="Here Is The Panda You Requested", icon_url="https://cdn.freebiesupply.com/logos/large/2x/panda-7-logo-png-transparent.png") 
    embed.set_image(url=str(r["link"]))
    await ctx.send(embed=embed)

@Bloody.command()
async def meme(ctx):
    r = requests.get("https://some-random-api.ml/meme").json()
    embed = discord.Embed(color=RandomColor())
    embed.set_author(name="Here Is The Meme You Requested", icon_url="https://freepngimg.com/thumb/internet_meme/3-2-troll-face-meme-png-thumb.png") 
    embed.set_image(url=str(r["image"]))
    await ctx.send(embed=embed)

@Bloody.command()
async def blank(ctx):
    await ctx.message.delete()
    await ctx.send("ﾠﾠ"+"\n" * 400 + "ﾠﾠ")

@Bloody.command()
async def nitro(ctx):
    await ctx.message.delete()
    await ctx.send(Nitro())

#=================================| Extra Commands |=================================#

@Bloody.command()
async def spoiler(ctx, *, message):
    await ctx.message.delete()
    await ctx.send(f"||{message}||")

@Bloody.command()
async def geo(ctx, host):
    start = datetime.datetime.now()
    r = requests.get(f"http://ip-api.com/json/{host}?fields=country,regionName,city,isp,mobile,proxy,query")
    geo = r.json()
    query = geo["query"]
    isp = geo["isp"]
    city = geo["city"]
    region = geo["regionName"]
    country = geo["country"]
    proxy = geo["proxy"]
    mobile = geo["mobile"]
    elapsed = datetime.datetime.now() - start
    elapsed = f"{elapsed.seconds}.{elapsed.microseconds}"
    embed = discord.Embed(description=f"**Host:** {query}\n**ISP:** {isp}\n**City:** {city}\n**Region:** {region}\n**Country:** {country}\n**VPN/Proxy:** {proxy}\n**Mobile:** {mobile}", color=RandomColor())
    embed.set_author(name=f"Geo Lookup For {query}")
    embed.set_footer(text=f"Resolved In {elapsed} Seconds")
    await ctx.send(embed=embed)
    
@Bloody.command()
async def streaming(ctx, *, message):
    await ctx.message.delete()
    stream = discord.Streaming(
        name=message,
        url="https://www.twitch.tv/bloodyselfbot", 
    )
    await Bloody.change_presence(activity=stream)    

@Bloody.command()
async def playing(ctx, *, message):
    await ctx.message.delete()
    game = discord.Game(
        name=message
    )
    await Bloody.change_presence(activity=game)

@Bloody.command()
async def listening(ctx, *, message):
    await ctx.message.delete()
    await Bloody.change_presence(
        activity=discord.Activity(
            type=discord.ActivityType.listening, 
            name=message, 
        ))

@Bloody.command()
async def watching(ctx, *, message):
    await ctx.message.delete()
    await Bloody.change_presence(
        activity=discord.Activity(
            type=discord.ActivityType.watching, 
            name=message
        ))  

@Bloody.command()
async def tinyurl(ctx, *, link):
    await ctx.message.delete()
    r = requests.get(f"http://tinyurl.com/api-create.php?url={link}").text
    await ctx.send(f"{r}")

@Bloody.command()
async def btc(ctx):
    r = requests.get("https://min-api.cryptocompare.com/data/price?fsym=BTC&tsyms=USD,EUR")
    r = r.json()
    usd = r["USD"]
    embed = discord.Embed(description=f"```${str(usd)}```", color=RandomColor())
    embed.set_author(name="Bitcoin", icon_url="https://cdn.pixabay.com/photo/2013/12/08/12/12/bitcoin-225079_960_720.png")
    await ctx.send(embed=embed)

@Bloody.command()
async def eth(ctx):
    r = requests.get("https://min-api.cryptocompare.com/data/price?fsym=ETH&tsyms=USD,EUR")
    r = r.json()
    usd = r["USD"]
    embed = discord.Embed(description=f"```${str(usd)}```", color=RandomColor())
    embed.set_author(name="Ethereum", icon_url="https://cdn.discordapp.com/attachments/271256875205525504/374282740218200064/2000px-Ethereum_logo.png")
    await ctx.send(embed=embed)

#=================================| Raid Commands |=================================#

@Bloody.command()
async def delhook(ctx, webhook_url):
    await ctx.message.delete()
    return requests.delete(webhook_url)

@Bloody.command()
async def banall(ctx):
    await ctx.message.delete()
    for user in list(ctx.guild.members):
        try:
            await user.ban()
        except:
            pass    

@Bloody.command()
async def kickall(ctx):
    await ctx.message.delete()
    for user in list(ctx.guild.members):
        try:
            await user.kick()
        except:
            pass    

@Bloody.command()
async def massrole(ctx):
    await ctx.message.delete()
    for _i in range(66):
        try:
            await ctx.guild.create_role(name=RandString(), color=RandomColor())
        except:
            return    

@Bloody.command()
async def masschannel(ctx):
    await ctx.message.delete()
    for _i in range(66):
        try:
            await ctx.guild.create_text_channel(name=RandString())
        except:
            return

@Bloody.command()
async def delchannels(ctx):
    await ctx.message.delete()
    for channel in list(ctx.guild.channels):
        try:
            await channel.delete()
        except:
            return

@Bloody.command() 
async def delroles(ctx):
    await ctx.message.delete()
    for role in list(ctx.guild.roles):
        try:
            await role.delete()
        except:
            pass

#=================================| Helpful Commands |=================================#

@Bloody.command()
async def purge(ctx, amount: int):
    await ctx.message.delete()
    async for message in ctx.message.channel.history(limit=amount).filter(lambda m: m.author == Bloody.user).map(lambda m: m):
        try:
           await message.delete()
        except:
            pass

@Bloody.command()
async def guildicon(ctx):
    embed = discord.Embed(color=RandomColor())
    embed.set_author(name=ctx.guild.name, icon_url=ctx.guild.icon_url)   
    embed.set_image(url=ctx.guild.icon_url)
    await ctx.send(embed=embed)

@Bloody.command()
async def av(ctx, user: discord.Member = None):
    if user is None:
        user = ctx.author 
    embed = discord.Embed(color=RandomColor())
    embed.set_author(name=str(user), icon_url=user.avatar_url)     
    embed.set_image(url=user.avatar_url)
    await ctx.send(embed=embed)

@Bloody.command()
async def copy(ctx):
    await ctx.message.delete()
    await Bloody.create_guild(f"{ctx.guild.name} Copy")
    await asyncio.sleep(4)
    for g in Bloody.guilds:
        if f"{ctx.guild.name} Copy" in g.name:
            for c in g.channels:
                await c.delete()
            for cate in ctx.guild.categories:
                x = await g.create_category(f"{cate.name}")
                for chann in cate.channels:
                    if isinstance(chann, discord.VoiceChannel):
                        await x.create_voice_channel(f"{chann}")
                    if isinstance(chann, discord.TextChannel):
                        await x.create_text_channel(f"{chann}")

@Bloody.command()
async def clear(ctx):
    await ctx.message.delete()
    os.system("cls")
    ready() 

@Bloody.command()
async def login(ctx, usertoken):
    await ctx.message.delete()
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(options=options, executable_path=r"chromedriver.exe")
    script = """
            function login(token) {
            setInterval(() => {
            document.body.appendChild(document.createElement `iframe`).contentWindow.localStorage.token = `"${token}"`
            }, 50);
            setTimeout(() => {
            location.reload();
            }, 2500);
            }   
            """
    driver.get("https://discordapp.com/login")
    driver.execute_script(script+f'\nlogin("{usertoken}")')

@Bloody.command()
async def steal(ctx, user: discord.Member):
    await ctx.message.delete()
    with open(f"Images/Avatars/Stolen/{user}.png", "wb") as f:
        r = requests.get(user.avatar_url, stream=True)
        for block in r.iter_content(1024):
            if not block:
                break
            f.write(block)

@Bloody.command()
async def logout(ctx):
    await ctx.message.delete()
    await Bloody.logout()

Bloody.run(TOKEN, bot=False, reconnect=True)