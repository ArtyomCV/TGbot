import telebot
import wikipedia
import re

bot = telebot.TeleBot('6164538889:AAFc7li8go2bkC6w0BZ5553GdLAKDIEqROc')
wikipedia.set_lang('ru')


def gewiki(s):
    try:
        ny = wikipedia.page(s)
        witext = ny.content[:1000]
        wimas = witext.split('.')
        wimas = wimas[:-1]
        witext2 = ''
        for i in wimas:
            if not ('==' in i):
                if (len((i.strip())) > 3):
                    witext2 = witext2 + i + '.'
                else:
                    break
        witext2 = re.sub('\([^()]*\)', '', witext2)
        witext2 = re.sub('\([^()]*\)', '', witext2)
        witext2 = re.sub('\{[^\{\}]*\}', '', witext2)
        return witext2
    except Exception as e:
        return 'Нет такой инфы'


@bot.message_handler(commands=['start'])
def start(m, res=False):
    bot.send_message(m.chat.id, 'Отправь мне любое слово и я найду его')


@bot.message_handler(content_types=['text'])
def handle_text(message):
    bot.send_message(message.chat.id, gewiki(message.text))


bot.polling(non_stop=True, interval=0)