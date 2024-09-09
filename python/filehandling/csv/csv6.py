import csv
with open('year2017.csv') as c:
    csv_data = csv.DictReader(c,skipinitialspace=True)
    killed = []
    for row in csv_data:
        if row['Weapon_type']=='Explosives':
            if row['Killed'] is '':
                pass
            else:
                killed.append(float(row['Killed']))
    print(sum(killed))
