import json, csv

with open('sample1.json', "r") as a:
    data = []
    data.append(json.load(a))
    print(data)

with open('jsontocsv.csv', 'w') as b:
    writing = csv.DictWriter(b, data[0].keys())
    writing.writeheader()
    writing.writerows(data)
