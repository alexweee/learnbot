from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging
import settings
import ephem
from datetime import datetime


logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log'
                    )

def greet_user(bot, update):
    text = ("Вызван /start")
    logging.info(text)
    update.message.reply_text(text)

def talk_to_me(bot, update):
    user_text = "Привет {}! Ты написал: {}".format(update.message.chat.first_name, update.message.text) 
    logging.info("User: %s, Chat id: %s, Message: %s", update.message.chat.username, 
                update.message.chat.id, update.message.text)
    update.message.reply_text(user_text)

def planetarium(bot, update):
    user_planet = update.message.text
    user_planet_split = user_planet.split()
    final_planeta = user_planet_split[1]
    const = ephem.constellation(getattr(ephem, final_planeta)(datetime.now()))
    update.message.reply_text(const)



def main():
    mybot = Updater(settings.API_KEY, request_kwargs=settings.PROXY)
    logging.info("Бот запускается")    
    dp = mybot.dispatcher
    dp.add_handler(CommandHandler('start', greet_user))

    dp.add_handler(MessageHandler(Filters.text, talk_to_me))

    dp.add_handler(CommandHandler('planet', planetarium))


    mybot.start_polling()
    mybot.idle()

main()


