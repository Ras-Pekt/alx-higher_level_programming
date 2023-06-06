#!/usr/bin/python3
for i in range(9):
    for j in range(1, 10):
        if i != j and j > i:
            print("{}{}".format(i, j), end="")
            if (i < 8 or j < 9):
                print(", ", end="")

print("\n", end="")
