#!/usr/bin/python3
for i in range(0, 9):
    for j in range(i + 1, 10):
        if i == 8 and j == 9:
            print(f"{i:d}{j:d}")
        else:
            print("{:d}{:d}".format(i, j), end=", ")
