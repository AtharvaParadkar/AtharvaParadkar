for a in range(1,5):
    for b in range(1,a+1):
        print(b, end=" ")
    print()
print("\n")

for c in range(5, 0, -1):
    for d in range(c):
        print("*", end=" ")
    print()
print("\n")

for e in range(5, 0, -1):
    for f in range(e):
        print(e, end=" ")
    print()
print("\n")

ch = 65
for g in range(1, 6):
    for h in range(g):
        print(chr(ch), end=" ")
        ch+=1
    print()
