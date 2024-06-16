from pyrogram import *
from pyrogram.types import *
from pyrogram.enums import *
import random, requests
import json, asyncio
import time as taym
import os
from datetime import *
from collections import *
from threading import *
API_ID = 24588661
API_HASH = "332058c74190c9a3739f43676f3a21e0"
TOKEN = "6906460787:AAE3jIVzKZCH3MlKjMQSy2ObkZMRwyJCaZM"
channelname = "RolexBots"
# first create rlxbot.session - ''.session-journal for vercel(if using)
bot = Client("rlxbot", api_id=API_ID, api_hash=API_HASH, bot_token=TOKEN)
bot.start();
bot.set_parse_mode(ParseMode.HTML)
game_sessions = {}

BALANCE_FILE = 'balances.json'

SUDO_USERS = ["6800066189"]  

user_balances = {}

btns = [
  [
    InlineKeyboardButton("Sahip 💛", url="https://t.me/bowed36")
  ],
  [
    InlineKeyboardButton("Kanal 💙", url="https://t.me/voleriaarsiv")
  ]
]

LOG = """
{} <b> Komutunda hata: </b>

<code> {} </code>
"""

def save_user(user_id):
  with open("users.txt", "r") as rfile:
    if user_id not in rfile.read().splitlines():
      with open("users.txt", "a") as afile:
        afile.write("\n" + user_id)
  return "Function End"
 
def all_users():
  with open("users.txt", "r") as gfile:
    return gfile.read().split('\n')
 
def load_balances():
    if os.path.exists(BALANCE_FILE):
        with open(BALANCE_FILE, 'r') as f:
            return json.load(f)
    return {}

def check_sub(cid, uid):
  cid = str(cid)
  uid = int(uid)
  try:
    bot.get_chat_member(cid, uid)
    return True
  except:
    return False 
 
def save_balances():
    with open(BALANCE_FILE, 'w') as f:
        json.dump(user_balances, f)
 
user_balances = load_balances()
    
@bot.on_message(filters.command("al"))
def al(client, message):
  user_id = str(message.from_user.id)
  save_user(user_id)
  save_user(user_id)
  urunler = {
    "disney": "599999999",
    "netflix": "54324553",
    "gain": "3434565",
    "blutv": "32211466"
    }
  if message.text == '/al':
    message.reply("Ürün numarası belirtmeniz gerekiyor.")
    return message.reply(" 1 > disney \n 2 > netflix \n 3 > gain \n 4 > blutv")
  args = message.text.split()
  no = args[1]
  if no == "1":
    fiyat = int(urunler['disney'])
    if user_balances[user_id] < fiyat:
      return message.reply(f"Bakiyeniz yetersiz, olması gereken {fiyat}, olan {user_balances[user_id]}")
    with open("disneys.txt", "r") as disneys:
      satirlar = disneys.read().splitlines()
      sç = random.choice(satirlar)
      user_balances[user_id] -= fiyat
      save_balances()
      return message.reply(f"<code> {sç} </code> (Yeni bakiye {user_balances[user_id]})")
  elif no == "2":
    fiyat = int(urunler['netflix'])
    if user_balances[user_id] < fiyat:
      return message.reply(f"Bakiyeniz yetersiz, olması gereken {fiyat}, olan {user_balances[user_id]}")
    with open("netflixes.txt", "r") as nets:
      satirlar = nets.read().splitlines()
      sç = random.choice(satirlar)
      user_balances[user_id] -= fiyat
      save_balances()
      return message.reply(f"<code> {sç} </code> (Yeni bakiye {user_balances[user_id]})")
  if no == "3":
    fiyat = int(urunler['gain'])
    if user_balances[user_id] < fiyat:
      return message.reply(f"Bakiyeniz yetersiz, olması gereken {fiyat}, olan {user_balances[user_id]}")
    with open("gains.txt", "r") as gain:
      satirlar = gain.read().splitlines()
      sç = random.choice(satirlar)
      user_balances[user_id] -= fiyat
      save_balances()
      return message.reply(f"<code> {sç} </code> (Yeni bakiye {user_balances[user_id]})")
  elif no == "4":
    fiyat = int(urunler['blutv'])
    if user_balances[user_id] < fiyat:
      return message.reply(f"Bakiyeniz yetersiz, olması gereken {fiyat}, olan {user_balances[user_id]}")
    with open("blutv.txt", "r") as blu:
      satirlar = blu.read().splitlines()
      sç = random.choice(satirlar)
      user_balances[user_id] -= fiyat
      save_balances()
      return message.reply(f"<code> {sç} </code> (Yeni bakiye {user_balances[user_id]})")
 
@bot.on_message(filters.command("hesap_ekle"))
def puan(client, message):
  user_id = str(message.from_user.id)
  save_user(user_id)       
  if message.text == '/hesap_ekle':
    return message.reply("Kullanım: /hesap_ekle disney şifre:eposta (disney yerine gain, netflix, blutv yazılabilir)") 
  args = message.text.split()
  tür = args[1]
  hesap = args[2]
  if tür == "disney":
    with open("disneys.txt", "a") as dis:
      dis.write(hesap+"\n")
  elif tür == "netflix":
    with open("netflixes.txt", "a") as dis:
      dis.write(hesap+"\n")
  elif tür == "gain":
    with open("gains.txt", "a") as dis:
      dis.write(hesap+"\n")
  elif tür == "blutv":
    with open("blutv.txt", "a") as dis:
      dis.write(hesap+"\n")
  return message.reply(f"Sunucuya {hesap} eklendi.")                   
@bot.on_message(filters.new_chat_members)
def new_c_mem(c, m):
  for member in m.new_chat_members:
    if str(member.id) == "6800066189":
      return m.reply(f"**Değerli sahibim {member.mention} gruba katıldı ♥️💙💛**")

@bot.on_message(filters.command("f"))
def free(client, message):
  t = Thread(target=send_f, args=(message,))
  t.start();
  
def send_f(message):
  user_id = str(message.from_user.id)
  if not check_sub(channelname, user_id):
    return message.reply(f"Botu kullanmak için @{channelname} kanalına katıl!")    
  if user_id not in SUDO_USERS:
    return message.reply("<b>Komutu kullanmak için yetkin yok.</b>")
  with open('balances.json', "r") as bowed:
    bowedd = bowed.read()
  boweddd = json.loads(bowedd)
  for key, value in boweddd.items():
    if value < 1500:
      user_balances[key] = 1500
      save_balances()
      message.reply(f'{key} kullanıcısına 150.000 bakiye gönderildi.')
      taym.sleep(1)
  message.reply("Gönderme işlemi tamamlandı.")
  return

                             
@bot.on_message(filters.command("puan"))
def puan(client, message):
  user_id = str(message.from_user.id)
  save_user(user_id)
  if not check_sub(channelname, user_id):
    return message.reply(f"Botu kullanmak için @{channelname} kanalına katıl!")
  if user_id not in SUDO_USERS:
    return message.reply("<b>Komutu kullanmak için yetkin yok.</b>")
  s = message.text.split()
  if message.text == '/puan':
    return message.reply("Bir puan belirt.")
  id = str(s[1])
  puan = int(s[2])
  user_balances[id] = puan  
  save_balances()
  message.reply(f"{id} {puan} olarak değiştirildi.")

@bot.on_message(filters.command("bky"))
def bkrm(client, message):
  user_id = str(message.from_user.id)
  save_user(user_id)
  t1 = Thread(target=send_blnc)
  t1.start();
  message.reply("Başlatıldı.")
            
def send_blnc():
  while True:
    bot.send_document(chat_id="bakiyekoruma", document="balances.json")
    taym.sleep(60)
    
# analarını tek elle kaldırmak için 
@bot.on_message(filters.command("kaldir"))
def unblock_user(client, message):
    user_id = str(message.from_user.id)
    if not check_sub(channelname, user_id):
      return message.reply(f"Botu kullanmak için @{channelname} kanalına katıl!")
    if user_id not in SUDO_USERS:
        return message.reply("<b>Komutu kullanmak için yetkin yok.</b>")
        

    try:
        parts = message.text.split()
        target_id = parts[1]
    except IndexError:
        message.reply('anasini sikmek istediğini kişinin ID\'si gir. böyle kullan oc: /kaldir <kullanıcı_id>')
        return

    if target_id in last_message_times:
        del last_message_times[target_id]
        message.reply(f'{target_id} kimlikli kullanıcının engeli kaldırıldı.')
    else:
        message.reply(f'{target_id} kimlikli kullanıcının engeli bulunmuyor.')
        
# anasının ayak numarasına bakmak
@bot.on_message(filters.command("bakiye"))
def check_balance(client, message):
    user_id = str(message.from_user.id)
    if not check_sub(channelname, user_id):
      return message.reply(f"Botu kullanmak için @{channelname} kanalına katıl!")
    user_id = str(message.from_user.id)

    if user_id not in user_balances:
        message.reply('Bota kayıtlı değilsiniz öncelikle bota /start Mesajını atın.')
        return

    message.reply(f"Güncel bakiyeniz: {user_balances[user_id]} RLX")
        
# anası risk altında mi kontrol etmek
@bot.on_message(filters.command("risk"))
def risk_command(client, message):
    user_id = str(message.from_user.id)
    if not check_sub(channelname, user_id):
      return message.reply(f"Botu kullanmak için @{channelname} kanalına katıl!")
    user_id = str(message.from_user.id)

    if user_id not in user_balances:
        message.reply('Bota kayıtlı değilsiniz, öncelikle bota /start mesajını atın.')
        return

    if len(message.text.split()) == 1:
        message.reply('Kullanım: /risk «miktar»')
        return

    try:
        # anasını satın almak
        risk_amount = int(message.text.split()[1])
    except (IndexError, ValueError):
        message.reply('Geçerli bir risk miktarı gir Kullanım: /risk «miktar»')
        return

    if risk_amount <= 0:
        message.reply('Risk miktarı sayı olmalı.')
        return

    if user_balances[user_id] < risk_amount:
        message.reply(f'Yeterli bakiyeniz yok. Mevcut bakiyeniz: {user_balances[user_id]} RLX')
        return

    # riskli anası 
    if random.random() < 0.65:  
        winnings = risk_amount * 2
        user_balances[user_id] = user_balances[user_id] + winnings
        save_balances()
        message.reply(f'Tebrikler  {winnings} RLX kazandınız.\nYeni bakiyeniz: {user_balances[user_id]} RLX')
    else:
        if user_id == "6800066189":
          winnings = risk_amount * 2
          user_balances[user_id] = user_balances[user_id] + winnings
          save_balances()
          message.reply(f'Tebrikler  {winnings} RLX kazandınız.\nYeni bakiyeniz: {user_balances[user_id]} RLX')
        else:
          user_balances[user_id] -= risk_amount
          message.reply(f'Üzgünüm {risk_amount} RLX kaybettiniz.\nbakiyeniz: {user_balances[user_id]} RLX')

    # Bakiyeleri güncelle
        save_balances()

# babasını da sikeyim 
@bot.on_message(filters.command("a"))
def b(client, message):
  user_id = str(message.from_user.id)
  save_user(user_id)
  if not check_sub(channelname, user_id):
    return message.reply(f"Botu kullanmak için @{channelname} kanalına katıl!")
  if message.text == '/a':
    return message.reply("Bir puan belirt.")
  if user_id not in SUDO_USERS:
    return message.reply("<b>Komutu kullanmak için yetkin yok.</b>")
  mktr = int(message.text.split()[1])
  user_balances[user_id] = user_balances[user_id] + mktr
  message.reply('Al cnm')

@bot.on_message(filters.command("yyn"))
def sendtoall(client, message):
  Thread(target=send_toall, args=(client, message,)).start();

def send_toall(client, message):
  if message.text == "/yyn":
    return message.reply("Mesajı girmelisin kanka:)")
  args = message.text.split()
  users = all_users()
  for user in users:
    try:
      client.send_message(user, " ".join(args[1:]))
      taym.sleep(1)
    except Exception as e:
      print(e)
  return message.reply("Gönderim tamamlandı.")
          
@bot.on_message(filters.command("toplam"))
def tplm(client, message):  
  users = all_users()
  return message.reply(len(users))
    
@bot.on_message(filters.command("start"))
def start(client, message):
    user_id = str(message.from_user.id)
    if not check_sub(channelname, user_id):
      return message.reply(f"Botu kullanmak için @{channelname} kanalına katıl!")
    user_id = str(message.from_user.id)
    if user_id not in user_balances:
        user_balances[user_id] = 1500  # Yeni kullanıcıya başlangıç bakiyesi
        save_balances()  # Bakiyeleri kaydet
    markup = InlineKeyboardMarkup(btns)
    message.reply(f"👋🏻 Merhaba {message.from_user.mention}, botu ilk kez başlatıyorsan 1500 RLX ücretsiz gönderilir. Komutlarım için /komutlar yaz.", reply_markup=markup)


@bot.on_message(filters.command("share"))
def send_balance_to_friend(client, message):
    user_id = str(message.from_user.id)
    if not check_sub(channelname, user_id):
      return message.reply(f"Botu kullanmak için @{channelname} kanalına katıl!")
    if not message.reply_to_message:   
      return message.reply("Bir mesaj yanıtlanmalıdır.")
    
    try:
        friend_id = message.reply_to_message.from_user.id
        parts = message.text.split()
        amount = int(parts[1])
    except (IndexError, ValueError):
        message.reply('Geçerli bir miktar girin Kullanım: /share «miktar»')
        return

    if amount <= 0:
        message.reply('Sayı girin')
        return

    if user_id not in user_balances:
        message.reply('Bota kayıtlı değilsiniz öncelikle bota /start Mesajını atın.')
        return

    if user_balances[user_id] < amount:
        message.reply('Yeterli bakiyeniz yok.')
        return

    if friend_id not in user_balances:
        user_balances[friend_id] = 0

    user_balances[user_id] -= amount
    user_balances[str(friend_id)] += amount
    save_balances()
    try:
      us = bot.get_users(friend_id)
      return message.reply(f'Başarılı! {us.first_name} adlı kullanıcıya {amount} RLX bakiye gönderildi. <b>Bakiyenizden {amount} eksiltildi.</b>')
    except Exception as e:
      for suser in SUDO_USERS:
        suser = int(suser)
        bot.send_message(suser, LOG.format("share", e))
      return message.reply(f'Başarılı! {friend_id} kimlikli kullanıcıya {amount} RLX bakiye gönderildi. <b>Bakiyenizden {amount} eksiltildi.</b>')
   
@bot.on_message(filters.command("global"))
def show_leaderboard(Client, message: Message):
    user_id = str(message.from_user.id)
    if not check_sub(channelname, user_id):
      return message.reply(f"Botu kullanmak için @{channelname} kanalına katıl!")
    Thread(target=asyncio.run, args=(lidertahtasi(Client, message),)).start();

async def lidertahtasi(Client, message: Message):   
    ypln = 0
    ldr = "🏆 En İyi 10:\n"
    sorted_balances = sorted(user_balances.values(), reverse=True)
    for vlr in sorted_balances[:10]:      
      for key, value in user_balances.items():
        if value == vlr and value != 1500:
          ypln += 1
          uzr = await Client.get_users(int(key))
          ldr += f"\n {ypln}. {uzr.mention} → {value}"
    await message.reply(ldr)
   
    
@bot.on_message(filters.command("komutlar"))
def send_help_message(client, message):
    user_id = str(message.from_user.id)
    if not check_sub(channelname, user_id):
      return message.reply(f"Botu kullanmak için @{channelname} kanalına katıl!")
    help_message = f"""
⭐ Merhaba {message.from_user.mention} ♥️,

/slot [miktar]: 🎰 Slot oyunu oynamak için.

/bakiye: 💰 Mevcut bakiyenizi kontrol edin.

/risk: Risk oyunu oynayıp bakiye kazanabilirsiniz. Şans oranı %65

/share [Kullanıcıyı Yanıtla] [miktar]: 💸 Başka bir kullanıcıya bakiye göndermek için.

/global: 🏆 Genel Sıralamayı gösterir.

/al: 🏪 Hesap satın almak için.
    """
    message.reply(help_message)

@bot.on_message(filters.command("slot"))
def slot_command(client, message):
    user_id = str(message.from_user.id)
    if not check_sub(channelname, user_id):
      return message.reply(f"Botu kullanmak için @{channelname} kanalına katıl!")
    user_id = str(message.from_user.id)
    if len(message.text.split()) == 1:
        message.reply('Slot Oyununu Oynayarak Bakiyen kasın Çıkarın\nKullanım: /slot «miktar»')
        return

    if user_id not in user_balances:
        message.reply('Bota kayıtlı değilsiniz, öncelikle bota /start mesajını atın.')
        return

    try: 
        bet_amount = int(message.text.split()[1])
    except (IndexError, ValueError):
        message.reply('Lütfen geçerli bir bahis miktarı girin. Kullanım: /slot «miktar»')
        return

    if bet_amount <= 0:
        message.reply('Bahis miktarı sayı olmalı.')
        return

    if user_balances[user_id] < bet_amount:
        message.reply(f'Yeterli bakiyeniz yok. Mevcut bakiyeniz: {user_balances[user_id]} RLX')
        return

    # Slot yarrakları
    slot_result = random.choices(["🍒", "🍋", "🍉", "⭐", "💎", "🍊", "🍏", "🔔"], k=3)
    unique_symbols = len(set(slot_result)) 
    if unique_symbols == 1: 
        winnings = bet_amount * 4
        user_balances[user_id] += winnings - bet_amount 
        message.reply(f'3 sembol eşleşti! Kazandınız!\nKazanılan Bakiye: {winnings} RLX\nYeni bakiyeniz: {user_balances[user_id]} RLX\nSlot sonucu: {" ".join(slot_result)}')
    elif unique_symbols == 2:
        winnings = bet_amount * 3
        user_balances[user_id] += winnings - bet_amount
        message.reply(f'2 sembol eşleşti Kazandınız!\nKazanılan bakiye: {winnings} RLX\nYeni bakiyeniz: {user_balances[user_id]} RLX\nSlot sonucu: {" ".join(slot_result)}')
    else:
        user_balances[user_id] -= bet_amount
        message.reply(f'Kazanamadınız. Bir dahakine daha şanslı olabilirsiniz.\nSlot sonucu: {" ".join(slot_result)}\nKalan bakiye: {user_balances[user_id]} RLX')

    save_balances()        

print(f"Bot @{bot.get_me().username} olarak başlatıldı.")
idle()