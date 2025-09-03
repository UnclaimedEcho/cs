for x in range(9):
    for y in range(abs(4-x)): print(" ",end = "")
    for y in range(5-abs(4-x)): print("@@", end = "")
    print()