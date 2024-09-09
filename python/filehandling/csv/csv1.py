import csv
c = open('year2017.csv')
csv_data = csv.reader(c,delimiter="|",skipinitialspace=True)
l_data=list(csv_data)[1:4]
for row in l_data:
    for data in row:
        print(data,end="")
    print()
