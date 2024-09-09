import csv
with open('year2017.csv') as c:
    csv_data = csv.reader(c,skipinitialspace=True)
    l_data = list(csv_data)
    wounded = []
    for row in l_data[1:]:
        if row[10] == '':
            pass
        else:
            wounded.append(float(row[10]))
    print(sum(wounded))