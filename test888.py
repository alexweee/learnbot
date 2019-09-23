import dict_for_cityes
PDICTIONARY_WITH_CITIES = dict_for_cityes.cityes


final_user_city = "Бряк"
first_bukva_in_letter = final_user_city[-1].upper()
print(first_bukva_in_letter)

list1 = []
for i in PDICTIONARY_WITH_CITIES:
    if i.startswith(first_bukva_in_letter):
        list1.append(i)

print(list1)