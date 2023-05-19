print("\nNatural Numbers are:- ")
for i in range(1, 11):
    print(i, end=" ")

print("\n\nEven Numbers in Reverse Order are:- ")
for j in range(20, 0, -2):
    print(j, end=" ")

n= int(input("\n\nEnter number to display it's table: "))
print("Table of",n)
for k in range(1,11):
    print(f"{n} x {k} = {n*k}")

print("\nFirst 10 prime numbers:")
count = 0
num = 2
while count < 10:
    prime = True
    for i in range(2, int(num/2) + 1):
        if num % i == 0:
            prime = False
            break
    if prime:
        print(num, end=" ")
        count += 1
    num += 1