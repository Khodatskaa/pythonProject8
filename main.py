rows = 5

for i in range(1, rows + 1):
    for j in range(1, rows * 2):
        if j <= i or j >= 2 * rows - i + 1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
