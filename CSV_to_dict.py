import csv
import dict_for_cityes

data = []

with open('Workbook2_csv.csv', 'r', encoding='utf-8') as f:
    fields = ['city_id', 'country_id', 'region_id', 'name']
    reader = csv.DictReader(f, fields, delimiter=';')
    for row in reader:
        data.append(row["name"])

#print(data)

print(dict_for_cityes.cityes)