import telebot
import config
import random
import requests
import parser_merlin
import math
from bs4 import BeautifulSoup as BS
 
from telebot import types
from crypto_news_api import CryptoControlAPI
 
bot = telebot.TeleBot(config.TOKEN)

TICKER_API_URL = 'https://min-api.cryptocompare.com/data/price?fsym=BTC&tsyms=USD'

api = CryptoControlAPI("3478ba36d43880c5a03ef177e85d5290")




def get_price_btc():
  
  response = requests.get('https://min-api.cryptocompare.com/data/price?fsym=BTC&tsyms=USD')
  response_json = response.json()
  
  gg = response_json
  gg = str(gg)
  gg = gg[0:-1]
  gg = gg[8:99]
  return gg
def get_price_eth():
  
  response = requests.get('https://min-api.cryptocompare.com/data/price?fsym=ETH&tsyms=USD')
  response_json = response.json()
  
  qq = response_json
  qq = str(qq)
  qq = qq[0:-1]
  qq = qq[8:99]
  return qq
def get_price_bitcoincash():
  
  response = requests.get('https://min-api.cryptocompare.com/data/price?fsym=BCH&tsyms=USD')
  response_json = response.json()
  
  ww = response_json
  ww = str(ww)
  ww = ww[0:-1]
  ww = ww[8:99]
  return ww
def get_price_eos():
  
  response = requests.get('https://min-api.cryptocompare.com/data/price?fsym=EOS&tsyms=USD')
  response_json = response.json()
  
  ee = response_json
  ee = str(ee)
  ee = ee[0:-1]
  ee = ee[8:99]
  return ee
def get_price_xrp():
  
  response = requests.get('https://min-api.cryptocompare.com/data/price?fsym=XRP&tsyms=USD')
  response_json = response.json()
  
  tt = response_json
  tt = str(tt)
  tt = tt[0:-1]
  tt = tt[8:99]
  return tt
def get_price_ltc():
  
  response = requests.get('https://min-api.cryptocompare.com/data/price?fsym=LTC&tsyms=USD')
  response_json = response.json()
  
  rr = response_json
  rr = str(rr)
  rr = rr[0:-1]
  rr = rr[8:99]
  return rr
def get_price_monero():
  
  response = requests.get('https://min-api.cryptocompare.com/data/price?fsym=XMR&tsyms=USD')
  response_json = response.json()
  
  yy = response_json
  yy = str(yy)
  yy = yy[0:-1]
  yy = yy[8:99]
  return yy
def get_price_tezos():
  
  response = requests.get('https://min-api.cryptocompare.com/data/price?fsym=DASH&tsyms=USD')
  response_json = response.json()
  
  ii = response_json
  ii = str(ii)
  ii = ii[0:-1]
  ii = ii[8:99]
  return ii
def get_price_tether():
  
  response = requests.get('https://min-api.cryptocompare.com/data/price?fsym=DOGE&tsyms=USD')
  response_json = response.json()
  
  vv = response_json
  vv = str(vv)
  vv = vv[0:-1]
  vv = vv[8:99]
  return vv














 
@bot.message_handler(commands=['start'])
def welcome(message):
 
    # keyboard
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Генератор паролей🔐")
    item2 = types.KeyboardButton("Криптовалюты🤑")
 
    markup.add(item1, item2)
 
    bot.send_message(message.chat.id, "Добро пожаловать, {0.first_name}!\nЯ - <b>{1.first_name}</b>, и я лучший бот если говоришь о компьютерной безопасности😏".format(message.from_user, bot.get_me()),
        parse_mode='html', reply_markup=markup)
 
@bot.message_handler(content_types=['text'])
def lalala(message):
    if message.chat.type == 'private':
        if message.text == 'Генератор паролей🔐':
            bot.send_sticker(message.chat.id, 123)
        elif message.text == 'Криптовалюты🤑':
 
            markup = types.InlineKeyboardMarkup()
            item1 = types.InlineKeyboardButton("Bitcoin", callback_data='btc')
            item2 = types.InlineKeyboardButton("Ethereum", callback_data='eth')
            item3 = types.InlineKeyboardButton("XRP", callback_data='xrp')
            item4 = types.InlineKeyboardButton("Bitcoin Cash", callback_data='bchd')
            item5 = types.InlineKeyboardButton("Litecoin", callback_data='ltc')
            item6 = types.InlineKeyboardButton("Doge Coin", callback_data='teth')
            item7 = types.InlineKeyboardButton("EOS", callback_data='eos')
            item8 = types.InlineKeyboardButton("Dash", callback_data='xtz')
            item9 = types.InlineKeyboardButton("Monero", callback_data='xmr')
 
            markup.add(item1, item2, item3, item4 , item5, item6,  item7, item8, item9)
 
            bot.send_message(message.chat.id, 'Вся информацию о самых популярных криптовалют прямо у тебя под носом👇', reply_markup=markup)
        else:
            bot.send_message(message.chat.id, 'Я не знаю что ответить 😢')
 
@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    try:
        if call.message:
            if call.data == 'btc':
                if parser_merlin.get('bitcoin') == '🔻':
                    sti = open('images/stonks-down.webp', 'rb')
                else:
                    sti = open('images/stonks-up.webp', 'rb')

                bot.send_sticker(call.message.chat.id, sti)
                bot.send_message(call.message.chat.id, get_price_btc() + ' USD' + parser_merlin.get('bitcoin'))

            elif call.data == 'eth':
                if parser_merlin.get('ethereum') == '🔻':
                    sti = open('images/stonks-down.webp', 'rb')
                else:
                    sti = open('images/stonks-up.webp', 'rb')
                
                bot.send_sticker(call.message.chat.id, sti)

                bot.send_message(call.message.chat.id, get_price_eth() + ' USD' + parser_merlin.get('ethereum'))

            elif call.data == 'xrp':
                if parser_merlin.get('bitcoin') == '🔻':
                    sti = open('images/stonks-down.webp', 'rb')
                else:
                    sti = open('images/stonks-up.webp', 'rb')

                bot.send_sticker(call.message.chat.id, sti)

                bot.send_message(call.message.chat.id, get_price_xrp() + ' USD' + parser_merlin.get('xrp'))

            elif call.data == 'bchd':
                if parser_merlin.get('bitcoin_cash') == '🔻':
                    sti = open('images/stonks-down.webp', 'rb')
                else:
                    sti = open('images/stonks-up.webp', 'rb')

                bot.send_sticker(call.message.chat.id, sti)
                bot.send_message(call.message.chat.id, get_price_bitcoincash() + ' USD' + parser_merlin.get('bitcoin_cash'))
            elif call.data == 'ltc':
                if parser_merlin.get('litecoin') == '🔻':
                    sti = open('images/stonks-down.webp', 'rb')
                else:
                    sti = open('images/stonks-up.webp', 'rb')

                bot.send_sticker(call.message.chat.id, sti)
                bot.send_message(call.message.chat.id, get_price_ltc() + ' USD' + parser_merlin.get('litecoin'))
            elif call.data == 'teth':
                if parser_merlin.get('dogecoin') == '🔻':
                    sti = open('images/stonks-down.webp', 'rb')
                else:
                    sti = open('images/stonks-up.webp', 'rb')

                bot.send_sticker(call.message.chat.id, sti)

                bot.send_message(call.message.chat.id, get_price_tether() + ' USD' + parser_merlin.get('dogecoin'))
            elif call.data == 'eos':
                if parser_merlin.get('eos') == '🔻':
                    sti = open('images/stonks-down.webp', 'rb')
                else:
                    sti = open('images/stonks-up.webp', 'rb')

                bot.send_sticker(call.message.chat.id, sti)
                bot.send_message(call.message.chat.id, get_price_eos() + ' USD' + parser_merlin.get('eos'))
            elif call.data == 'xtz':
                if parser_merlin.get('dash') == '🔻':
                    sti = open('images/stonks-down.webp', 'rb')
                else:
                    sti = open('images/stonks-up.webp', 'rb')

                bot.send_sticker(call.message.chat.id, sti)
                bot.send_message(call.message.chat.id, get_price_tezos() + ' USD' + parser_merlin.get('dash'))
            elif call.data == 'xmr':
                if parser_merlin.get('monero') == '🔻':
                    sti = open('images/stonks-down.webp', 'rb')
                else:
                    sti = open('images/stonks-up.webp', 'rb')

                bot.send_sticker(call.message.chat.id, sti)
                bot.send_message(call.message.chat.id, get_price_monero() + ' USD' + parser_merlin.get('monero'))  
 
 
 
    except Exception as e:
        print(repr(e))
 
# RUN
bot.polling(none_stop=True)