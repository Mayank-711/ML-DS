n = int(input("Enter the size of the square pattern: "))
i = n

while i >= 1: 
    j = n
    while j >= 1: 
        print(j, end=" ")
        j = j - 1
    print() 
    i = i - 1
