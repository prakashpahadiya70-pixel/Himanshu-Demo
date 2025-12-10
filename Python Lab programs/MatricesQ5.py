r = int(input("Enter number of rows: "))
c = int(input("Enter number of columns: "))

print("Enter elements of Matrix A:")
A = [list(map(int, input().split())) for _ in range(r)]

print("Enter elements of Matrix B:")
B = [list(map(int, input().split())) for _ in range(r)]

# Resultant Matrix
C = [[A[i][j] + B[i][j] for j in range(c)] for i in range(r)]

print("\nResultant Matrix (A + B) :")
for row in C:
    print(*row)