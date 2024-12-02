import csv, json

with open('updated.csv', 'r') as a:
    data = csv.DictReader(a)

    csvdata = []
    for i in data:
        csvdata.append(i)

    print(csvdata)

with open('csvtojson.json', 'w') as b:
    json.dump(csvdata, b, indent=4)
