import os
from discord import embeds
import requests
from discord.ext import commands
import discord
from dotenv import load_dotenv


load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix=';')

@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')
    await bot.change_presence(activity=discord.Game(name=";command | lnwtxn"))

url_watasalim = 'https://watasalim.vercel.app/api/quotes/random'
url_inspire = 'https://zenquotes.io/api/quotes'
url_covid_thailand = "https://covid19.ddc.moph.go.th/api/Cases/today-cases-all"
url_github = 'https://github.com/lnwtxn'
url_facebook = 'https://web.facebook.com/Thunder2004/'
url_ig = 'https://www.instagram.com/kitton._/'

@bot.event
async def on_message(message):
    if message.content.startswith(';dev'):
        devEmbed = discord.Embed(title=':computer: Developer Profile',
                                 description= '**This Bot is Develop by : <@400087960428609536> **'+ 
                            f'\n\n :envelope: **Contact Me** \n :link: My Github : {url_github}'+
                            f'\n :link: My Facebook : {url_facebook} \n :link: My Instagram : {url_ig}')
        
        await message.channel.send(embed=devEmbed)
    
    elif message.content.startswith(';salim'):
        
        res = requests.get(url_watasalim)
        data = res.json()
        wata = data['quote']['body']
        
        wataEmbed = discord.Embed(title=':speech_balloon: วาทกรรมสลิ่ม',
                                  description = f"**{wata}**")
        
        await message.channel.send(embed=wataEmbed)

    elif message.content.startswith(';inspire'):
        res = requests.get(url_inspire)
        data = res.json()
        
        quote = data[0]['q']
        name = data[0]['a']
        
        inspireEmbed = discord.Embed(title=':speech_balloon: Inspirational Quotes',
                                     description = f'**{quote}**\n{name}')
        
        await message.channel.send(embed=inspireEmbed)
        
    elif message.content.startswith(';covid'):
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
        
        covidEmbed = discord.Embed(title = f':microbe: รายงานยอดผู้ติดเชื้อประจำวันที่ {txn_date}')
        
        covidEmbed.add_field(name= 'ติดเชื้อเพิ่มวันนี้', value= f'{new_case}', inline= True)
        covidEmbed.add_field(name= 'ติดเชื้อสะสมในประเทศ', value= f'{total_case}', inline= True)
        covidEmbed.add_field(name= 'เสียชีวิตเพิ่ม', value= f'{new_death}', inline= True)
        covidEmbed.add_field(name= 'เสียชีวิตรวม', value= f'{total_death}', inline= True)
        covidEmbed.add_field(name= 'รักษาหาย', value= f'{new_recovered}', inline= True)
        covidEmbed.add_field(name= 'รักษาหายรวม', value= f'{total_recovered}', inline= True)
        
        await message.channel.send(embed=covidEmbed)
        
    elif message.content.startswith(';command'):
        commandEmbed = discord.Embed(title=':file_folder: Command List',
                                   description= '**:red_circle: Prefix : `;`**'+ 
                            '\n\n**:school: Class Schedule** \n`;schedule` = `ดูตารางสอน online` \n`;friend ชื่อเล่น` = `ข้อมูลส่วนตัวของเพื่อน`'+ 
                            '\n\n**:memo: TCAS65 Schudule**\n `;gatpat` = `ดูตารางสอบ Gat & Pat และดูเวลาเตรียมตัว` \n `;tcas ชื่อย่อของมหาวิทยาลัย` = `ดูข้อมูล Admission`'+ 
                            '\n `;saman` = `ดูตารางสอบ 9 วิชาสามัญ และดูเวลาเตรียมตัว` \n `;tcas65` = `ดูปฏิทิน TCAS65`'+ 
                            '\n\n **:speech_left: Message API** \n `;covid19 thailand` = `ดูรายงานโควิดประจำวัน`\n`;covid ชื่อจังหวัด` = `ดูรายงานโควิดประจำจังหวัด`'+
                            ' \n `;inspire` = `ดูแรงบันดาลใจ`'+
                            '\n`;watasalim` = `ดูวาทกรรมสลิ่ม` \n `;cheab` = `คำคมเฉียบๆ`'+
                            '\n\n **:mag_right: About** \n `;dev` = `ข้อมูลผู้พัฒนา`')
        
        await message.channel.send(embed=commandEmbed)
bot.run(TOKEN)