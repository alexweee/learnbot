import random
dict_city = {}
dict_users = {}

def game_of_city():
    x = random.randint(0,100) 

    dict_city["bot_city"] = x

game_of_city()
print(dict_city)