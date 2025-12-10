for i in range(4):
    num = 1  
    for j in range(i + 1):
        print(num, end=" ")
        num = 1 - num  
    print()