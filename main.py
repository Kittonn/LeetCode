import os
from discord import embeds
import requests
from discord.ext import commands
import discord
from dotenv import load_dotenv
import random
from datetime import date

url_watasalim = 'https://watasalim.vercel.app/api/quotes/random'
url_inspire = 'https://zenquotes.io/api/quotes'
url_covid_thailand = "https://covid19.ddc.moph.go.th/api/Cases/today-cases-all"
url_github = 'https://github.com/lnwtxn'
url_facebook = 'https://web.facebook.com/Thunder2004/'
url_ig = 'https://www.instagram.com/kitton._/'
url_tcas65 = 'https://media.discordapp.net/attachments/906186108650528808/910210700692049920/IMG_9777.jpg?width=705&height=393'
url_mytcas_img = 'https://media.discordapp.net/attachments/906186108650528808/910442373576806420/9k.png'
url_MOPH_img = 'https://media.discordapp.net/attachments/910557153356550164/911654142768996352/logo_web.png'
url_gatpat_img = 'https://media.discordapp.net/attachments/906186108650528808/910210699999985684/IMG_9779.jpg?width=502&height=502'
url_9saman_img = 'https://media.discordapp.net/attachments/906186108650528808/910210700218101860/IMG_9778.jpg?width=502&height=502'
url_schedule = 'https://media.discordapp.net/attachments/912032605845741578/914551150747979826/IMG_9866.png?width=769&height=490'
url_friend = 'https://mvk19-section3-api.herokuapp.com/'
url_tcas_university = 'https://api-tcas.herokuapp.com/'
url_cheab_quote = 'https://cheab-quote.herokuapp.com'
url_covid_province = 'https://covid19.ddc.moph.go.th/api/Cases/today-cases-by-provinces'

province_data = {"krabi": "0", "bangkok": "1", "kanchanaburi": "2","kalasin": "3","kamphaengphet": "4","khonkaen": "5","chanthaburi": "6","chachoengsao": "7",
                 "chonburi": "8","chainat": "9","chaiyaphum": "10","chumphon": "11","trang": "12","trat": "13","tak": "14","nakhonnayok": "15","nakhonpathom":"16",           
                 "nakhonphanom":"17","nakhonratchasima":"18","nakhonsithammarat":"19","nakhonsawan":"20","nonthaburi":"21","narathiwat":"22","nan":"23","buengkan":"24",
                 "buriram":"25","pathumthani":"26","prachuapkhirikhan":"27","prachinburi":"28","pattani":"29","ayutthaya":"30","phayao":"31","phangnga":"32","phatthalung":"33",
                 "phichit":"34","phitsanulok":"35","phuket":"36","mahasarakham":"37","mukdahan":"38","yala":"39","yasothon":"40","roiet":"41","ranong":"42","rayong":"43",
                 "ratchaburi":"44","lopburi":"45","lampang":"46","lamphun":"47","sisaket":"48","sakonnakhon":"49","songkhla":"50","satun":"51","samutprakan":"52",
                 "samutsongkhram":"53","samutsakhon":"54","saraburi":"55","sakaew":"56","singburi":"57","suphanburi":"58","suratthani":"59","surin":"60","sukhothai":"61",
                 "nongkhai":"62","nongbualamphu":"63","angthong":"64","amnatcharoen":"65","udonthani":"66","uttaradit":"67","uthaithani":"68","ubonratchathani":"69",
                 "chiangrai":"70","chiangmai":"71","phetchaburi":"72","phetchabun":"73","loei":"74","phrae":"75","maehongson":"76"
}

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix=';')

@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')
    await bot.change_presence(activity=discord.Game(name=";command | lnwtxn"))

@bot.command()
async def dev(message):
    
    devEmbed = discord.Embed(title=':computer: Developer Profile',
                                 description= '**This Bot is Develop by : <@400087960428609536> **'+ 
                            f'\n\n :envelope: **Contact Me** \n :link: My Github : {url_github}'+
                            f'\n :link: My Facebook : {url_facebook} \n :link: My Instagram : {url_ig}',
                            color =0x001524)
        
    await message.send(embed=devEmbed)

@bot.command()
async def watasalim(message):
    
    res = requests.get(url_watasalim)
    data = res.json()
    wata = data['quote']['body']
    
    wataEmbed = discord.Embed(title=':speech_balloon: วาทกรรมสลิ่ม',
                              description = f"**{wata}**",
                              color =0x001524)
    
    await message.send(embed=wataEmbed)

@bot.command()
async def inspire(message):
    
    res = requests.get(url_inspire)
    data = res.json()
    
    quote = data[0]['q']
    name = data[0]['a']
    
    inspireEmbed = discord.Embed(title=':speech_balloon: Inspirational Quotes',
                                description = f'**{quote}**\n{name}',
                                color =0x001524)
    
    await message.channel.send(embed=inspireEmbed)

@bot.command()
async def covid(message, *, arg):
    
    if (arg == 'thailand'):
        res = requests.get(url_covid_thailand)
        data = res.json()

        txn_date = data[0]['txn_date']
        update_date = data[0]['update_date']
        new_case = data[0]['new_case']
        total_case = data[0]['total_case']
        new_death = data[0]['new_death']
        total_death = data[0]['total_death']
        new_recovered = data[0]['new_recovered']
        total_recovered = data[0]['total_recovered']

        covidEmbed = discord.Embed(title = f':microbe: รายงานยอดผู้ติดเชื้อประจำวันที่ {txn_date}',
                                   description=f'`อัพเดตข้อมูล ณ วันที่ {update_date}`',
                                   color =0x001524)

        covidEmbed.add_field(name= 'ติดเชื้อเพิ่มวันนี้', value= f'{new_case}', inline= True)
        covidEmbed.add_field(name= 'ติดเชื้อสะสมในประเทศ', value= f'{total_case}', inline= True)
        covidEmbed.add_field(name= 'เสียชีวิตเพิ่ม', value= f'{new_death}', inline= True)
        covidEmbed.add_field(name= 'เสียชีวิตรวม', value= f'{total_death}', inline= True)
        covidEmbed.add_field(name= 'รักษาหาย', value= f'{new_recovered}', inline= True)
        covidEmbed.add_field(name= 'รักษาหายรวม', value= f'{total_recovered}', inline= True)
        covidEmbed.set_footer(text='อ้างอิงข้อมูลจาก กรมควบคุมโรค',icon_url=url_MOPH_img)

        await message.send(embed=covidEmbed)
    else:
        res = requests.get(url_covid_province)
        data = res.json()
        fetch = data[int(province_data[arg])]
        
        txn_date = fetch['txn_date']
        update_date = fetch['update_date']
        new_case = fetch['new_case']
        total_case = fetch['total_case']
        new_death = fetch['new_death']
        total_death = fetch['total_death']
        pro = fetch['province']
        
        provinceEmbed = discord.Embed(title = f':microbe: รายงานยอดผู้ติดเชื้อ {pro} ประจำวันที่ {txn_date}',
                                   description=f'`อัพเดตข้อมูล ณ วันที่ {update_date}`',
                                   color =0x001524)

        provinceEmbed.add_field(name= 'ติดเชื้อเพิ่มวันนี้', value= f'{new_case}', inline= True)
        provinceEmbed.add_field(name= 'ติดเชื้อสะสมในประเทศ', value= f'{total_case}', inline= True)
        provinceEmbed.add_field(name= 'เสียชีวิตเพิ่ม', value= f'{new_death}', inline= True)
        provinceEmbed.add_field(name= 'เสียชีวิตรวม', value= f'{total_death}', inline= True)
        provinceEmbed.set_footer(text='อ้างอิงข้อมูลจาก กรมควบคุมโรค',icon_url=url_MOPH_img)

        await message.send(embed=provinceEmbed)
        
@covid.error
async def covid_error(message, error):
    if isinstance(error, commands.CommandError):
        await message.reply('No data in API!!!')
    
@bot.command()
async def command(message):
    
    commandEmbed = discord.Embed(title=':file_folder: Command List',
                                 color =0x001524,
                                   description= '**:red_circle: Prefix : `;`**'+ 
                            '\n\n**:school: Class Schedule** \n`;schedule` = `ดูตารางสอน online` \n`;friend ชื่อเล่น` = `ข้อมูลส่วนตัวของเพื่อน`'+ 
                            '\n\n**:memo: TCAS65 Schudule**\n `;gatpat` = `ดูตารางสอบ Gat & Pat และดูเวลาเตรียมตัว` \n `;tcas ชื่อย่อของมหาวิทยาลัย` = `ดูข้อมูล Admission`'+ 
                            '\n `;saman` = `ดูตารางสอบ 9 วิชาสามัญ และดูเวลาเตรียมตัว` \n `;tcas65` = `ดูปฏิทิน TCAS65`'+ 
                            '\n\n **:speech_left: Message API** \n `;covid19 thailand` = `ดูรายงานโควิดประจำวัน`\n`;covid ชื่อจังหวัด` = `ดูรายงานโควิดประจำจังหวัด`'+
                            ' \n `;inspire` = `ดูแรงบันดาลใจ`'+
                            '\n`;watasalim` = `ดูวาทกรรมสลิ่ม` \n `;cheab` = `คำคมเฉียบๆ`'+
                            '\n\n **:mag_right: About** \n `;dev` = `ข้อมูลผู้พัฒนา`')
        
    await message.send(embed=commandEmbed)
    
@bot.command()
async def tcas65(message):
    
    tcas65Embed = discord.Embed(title=':date: ปฏิทิน TCAS65',
                                color =0x001524)
    tcas65Embed.set_image(url=url_tcas65)
    tcas65Embed.set_footer(text='อ้างอิงข้อมูลจาก www.mytcas.com',icon_url=url_mytcas_img)
    
    await message.send(embed=tcas65Embed)
    
@bot.command()
async def gatpat(message):
    
    today = date.today()
    future = date(2022,3,12)
    diff = future - today
    
    gatpatEmbed = discord.Embed(title=':hourglass: ตารางสอบ Gat & Pat',
                                color =0x001524,
                                description = f'====== **เหลือเวลาเตรียมตัวอีก {diff.days} วัน** ======')
    gatpatEmbed.set_image(url=url_gatpat_img)
    gatpatEmbed.set_footer(text='อ้างอิงข้อมูลจาก www.mytcas.com',icon_url=url_mytcas_img)
    
    await message.send(embed=gatpatEmbed)

@bot.command()
async def saman(message):
    
    today = date.today()
    future = date(2022,3,19)
    diff = future - today
    
    samanEmbed = discord.Embed(title=':hourglass: ตารางสอบ 9 วิชาสามัญ',
                               color =0x001524,
                               description = f'====== **เหลือเวลาเตรียมตัวอีก {diff.days} วัน** ======')
    samanEmbed.set_image(url=url_9saman_img)
    samanEmbed.set_footer(text='อ้างอิงข้อมูลจาก www.mytcas.com',icon_url=url_mytcas_img)
    
    await message.send(embed=samanEmbed)
    
@bot.command()
async def schedule(message):
    
    scheduleEmbed = discord.Embed(title=':memo: ตารางสอน ชั้นมัธยมศึกษาปีที่ 6/3',
                                  color =0x001524)
    scheduleEmbed.set_image(url=url_schedule)
    scheduleEmbed.set_footer(text='อ้างอิงข้อมูลจาก ฝ่ายวิชาการโรงเรียนมารีวิทยากบินทร์บุรี')
    
    await message.send(embed=scheduleEmbed)

@bot.command()
async def friend(message, *, arg):
    
    res = requests.get(url_friend)
    data = res.json()
    
    name = data[f'{arg}']['name']
    nickname = data[f'{arg}']['nickname']
    ig = data[f'{arg}']['ig']
    img = data[f'{arg}']['url_img']
    
    friendEmbed = discord.Embed(title = ':bookmark_tabs: Friend Information',
                                description = f'ชื่อ-นามสกุล : {name}\nชื่อเล่น : {nickname}\nInstagram : {ig}',
                                color =0x001524)
    friendEmbed.set_thumbnail(url=img)
    friendEmbed.set_footer(text='อ้างอิงข้อมูลจาก https://github.com/lnwtxn')
    
    await message.send(embed=friendEmbed)
    
@friend.error
async def friend_error(message, error):
    if isinstance(error, commands.CommandError):
        await message.reply('No data in API!!!')
        
@bot.command()
async def tcas(message, *, arg):
    
    res = requests.get(url_tcas_university)
    data = res.json()
    
    name_lower = arg.lower()
    name = data[f'{name_lower}']['name']
    url = data[f'{name_lower}']['url']
    img = data[f'{name_lower}']['url_img']
    name_upper = arg.upper()
    
    tcasEmbed = discord.Embed(title = f':school: TCAS65 {name_upper}',
                                description = f'{name}\n{url}',
                                color =0x001524)
    tcasEmbed.set_image(url=img)
    tcasEmbed.set_footer(text=f'อ้างอิงข้อมูลจาก {name}')
    
    await message.send(embed=tcasEmbed)

@tcas.error
async def tcas_error(message, error):
    if isinstance(error, commands.CommandError):
        await message.reply('No data in API!!!')

@bot.command()
async def cheab(message):

    res = requests.get(url_cheab_quote)
    data = res.json()
    
    num_list = len(data['quote'])
    n = random.randint(0,num_list)
    
    q = data['quote'][n]
    await message.reply(f'{q}')


    
bot.run(TOKEN)