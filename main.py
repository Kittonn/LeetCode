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

@bot.event
async def on_message(message):
    if message.content.startswith(';ping'):
        await message.channel.send('Hello')
    
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
        await message.channel.send('กำลังพัฒนา เร็วนี้จะเต็มระบบ!!!')
bot.run(TOKEN)