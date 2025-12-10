lst = list(map(int, input("Enter list elements separated by space: ").split()))
key = int(input("Enter the number to search: "))

flag = False

for i in range(len(lst)):
    if lst[i] == key:
        print("Success! Number found at position:", i + 1)
        flag = True
        break

if not flag:
    print("Failure! Number not found in list.")