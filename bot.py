from os import environ
import aiohttp
from pyrogram import Client, Filters


API_ID = environ.get('API_ID')
API_HASH = environ.get('API_HASH')
BOT_TOKEN = environ.get('BOT_TOKEN')
API_KEY = environ.get('API_KEY','2730715a1b62fd6aea17ce00fb94541e3ddc304b')


bot = Client('gplink bot', 
             api_id=API_ID, 
             api_hash=API_HASH,
             bot_token=BOT_TOKEN)



@bot.on_message(Filters.command('start') & Filters.private)
async def start(bot, message):
    await message.reply(
        f"**Hi {message.chat.first_name}!**\n\n"
        "Hello I am ShortLink For More \help Our Servies \us Creator @seshu2004")

@bot.on_message(Filters.command('help') & Filters.private)
async def help(bot, message):
    await message.reply(
        f"**Hi {message.chat.first_name}!**\n\n"
        "Send Any Link I will convert into shortlink ")

@bot.on_message(Filters.command('us') & Filters.private)
async def us(bot, message):
    await message.reply(
        f"**Hi {message.chat.first_name}!**\n\n"
        "@gryfendor_leecher torrent to Grive and Leecher more Join S4Hteam")
    
@bot.on_message(Filters.regex(r'https?://[^\s]+') & Filters.private)
async def link_handler(bot, message):
    link = message.matches[0].group(0)
    try:
        short_link = await get_shortlink(link)
        await message.reply(f'Here is your [short link]({short_link})', quote=True)
    except Exception as e:
        await message.reply(f'Error: {e}', quote=True)
    
    
async def get_shortlink(link): 
    url = 'https://gplinks.in/api'
    params = {'api': API_KEY, 'url': link}
    
    async with aiohttp.ClientSession() as session:
        async with session.get(url, params=params, raise_for_status=True) as response:
            data = await response.json()
            return data["shortenedUrl"]
            
        
bot.run()
