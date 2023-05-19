ml = [1, 2, 5, -8, 11, 9, -4, 3, -21, 11, 50, -14, 2, -8, 17]
print(ml)

sum=0
for i in ml:
    sum+=i
print("Sum =", sum)

print("Largest Number =", max(ml))

ml2 = list(set(ml))
print("List after removing duplicate items:-", ml2)

pml = []
nml = []
for j in ml:
    if j >= 0:
        pml.append(j)
    else:
        nml.append(j)
print("Positive numbers form list are:-", pml)
print("Negative numbers from list are:-", nml)

eml = []
oml = []
for k in ml:
    if k % 2 == 0:
        eml.append(k)
    else:
        oml.append(k)
print("Even numbers from list are:-", eml)
print("Odd numbers from list are:-", oml)