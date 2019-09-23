from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging
import settings2
import ephem
import dict_for_cityes
from datetime import datetime
import random

DICTIONARY_WITH_CITIES = dict_for_cityes.cityes

#bot
logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot_dedicated_city.log'
                    )

dict_city = {}
dict_users = {}


def game_of_city(bot, update):
    x = random.randint(0,100) 
    bot_city = DICTIONARY_WITH_CITIES[x]
    bot_city_up = bot_city.upper()
    update.message.reply_text(f" Первый город - {bot_city}")
    dict_city["bot_city"] = bot_city_up
    DICTIONARY_WITH_CITIES.remove(bot_city)

def city(bot, update):
    list_of_cities_of_bukva = []
    final_user_city = str(update.message.text)
    #user_city_split = user_city.split()
    #final_user_city = user_city_split[1]
    first_bukva_in_letter = final_user_city[-1].upper()
    dict_city["user_city"] = final_user_city
    
    current_letter = dict_city["bot_city"][-1]


    if final_user_city in DICTIONARY_WITH_CITIES and final_user_city.startswith(dict_city["bot_city"][-1]):
        update.message.reply_text("все ок")
        for i in DICTIONARY_WITH_CITIES:
            if i.startswith(first_bukva_in_letter):
                list_of_cities_of_bukva.append(i)
        DICTIONARY_WITH_CITIES.remove(final_user_city)
        update.message.reply_text(list_of_cities_of_bukva[0])
        dict_city["bot_city"] = list_of_cities_of_bukva[0].upper()
        DICTIONARY_WITH_CITIES.remove(list_of_cities_of_bukva[0])
        list_of_cities_of_bukva.remove(list_of_cities_of_bukva[0])
        list_of_cities_of_bukva.remove(final_user_city)
    elif final_user_city in DICTIONARY_WITH_CITIES and not final_user_city.startswith(dict_city["bot_city"][-1]):
        update.message.reply_text(f"вы ввели город, который начинается не на последнюю букву моего __ {current_letter} __")
    elif final_user_city not in DICTIONARY_WITH_CITIES:
        update.message.reply_text("Такого города не существует")



def main():
    mybot = Updater(settings2.API_KEY, request_kwargs=settings2.PROXY)
    logging.info("Бот запускается")    
    dp = mybot.dispatcher
    dp.add_handler(CommandHandler('start', game_of_city))
    dp.add_handler(MessageHandler(Filters.text, city))

    mybot.start_polling()
    mybot.idle()

main()

