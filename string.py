str = "Hello Python!"
print(str)
print("Reverse String:-", str[::-1])

vowels = 0
constants = 0
for i in str:
    if i in 'aeiou':
        vowels+=1
    else:
        constants+=1
print("Vowels in string are:-", vowels)
print("Constants in string are:-", constants)

print("Number of letters in", str, "are", len(str))

print(str.swapcase())

lower = 0
upper = 0
numeric = 0
special = 0
for j in str:
    if j.islower():
        lower+=1
    elif j.isupper():
        upper+=1
    elif j.isnumeric():
        numeric+=1
    else:
        special+=1
print("Lower characters in",str,"are", lower)
print("Upper characters in",str,"are", upper)
print("Numeric characters in",str,"are", numeric)
print("Special characters in",str,"are", special)