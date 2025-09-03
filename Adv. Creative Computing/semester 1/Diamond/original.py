for x in range(0,11, 2):
    for w in range(int((10-x)/2)): print(" ",end="")
    for y in range(x): print("@", end = "")
    print()
for s in range(-2, 11, 2):
    x=6-s
    for w in range(int((10-x)/2)): print(" ",end="")
    for y in range(x): print("@", end = "")
    print()