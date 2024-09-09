import csv
c = open('year2017.csv')
csv_data = csv.reader(c,delimiter="|",skipinitialspace=True)
l_data=list(csv_data)[0]
for row in l_data:
    print(row)
    