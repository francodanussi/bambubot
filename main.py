from telegram.ext import Updater, InlineQueryHandler, CommandHandler
import requests
import re

def get_url():
    contents = requests.get('https://random.dog/woof.json').json()
    url = contents['url']
    return url

def get_image_url():
    allowed_extension = ['jpg','jpeg','png']
    file_extension = ''
    while file_extension not in allowed_extension:
        url = get_url()
        file_extension = re.search("([^.]*)$",url).group(1).lower()
    return url

def perrito(bot, update):
    url = get_image_url()
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)

def durmiendo(bot,update):
    chat_id = update.message.chat_id
    bot.send_message(chat_id=chat_id,text="Estaba durmiendo la siesta y me despertaron!!!!")

def hambre(bot,update):
    chat_id = update.message.chat_id
    bot.send_message(chat_id=chat_id,text="Tengo hambre!")

def foto(bot,update):
    chat_id = update.message.chat_id
    bot.send_message(chat_id=chat_id,text="Todavía no tengo fotos para compartir...")

def sayHyDomi(bot,update):
    chat_id = update.message.chat_id
    bot.send_message(chat_id=chat_id,text="hola súper pastelito")

def main():
    updater = Updater('782605232:AAE78p5rKeL2UZuOPM7TlHhjWUp2SUaNlE0')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('perrito',perrito))
    dp.add_handler(CommandHandler('saludarADomi',sayHyDomi))
    dp.add_handler(CommandHandler('estasdurmiendo?',durmiendo))
    dp.add_handler(CommandHandler('teneshambre?',hambre))
    dp.add_handler(CommandHandler('bambufoto',foto))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
