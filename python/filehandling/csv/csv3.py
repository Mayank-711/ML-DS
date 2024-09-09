import csv

# Open the CSV file
with open('year2017.csv', 'r') as c:
    csv_data = csv.reader(c, skipinitialspace=True)
    
    # Read all rows from the CSV file
    l_data = list(csv_data)
    
    # Initialize the list to store data from the specific column
    Country = []

    for row in l_data[1:11]:
        Country.append(row[3])
    
    # Print the list of countries
    print(Country)
