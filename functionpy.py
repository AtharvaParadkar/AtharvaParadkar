def add(a, *b):
    c = a
    for i in b:
        c += i
    print("Addition = ", c)

def mul(a, *b):
    c = a
    for i in b:
        c *= i
    print("Multiplication = ", c)

def sub(a, *b):
    c = a
    for i in b:
        c -= i
    print("Subtraction = ", c)

def div(a, *b):
    c = a
    for i in b:
        c /= i
    print("Division = ", c)

add(1, 15, 6, 7, 8, 3)
mul(2, 5, 9, 4, 7, 8, 3)
sub(9, 2, 4, 2, 5, 1)
div(9, 4, 3, 2)
