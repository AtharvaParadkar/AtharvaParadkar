md = {"Mango":12, "Apple":5, "Watermelon":1}
print(md)

if "Mango" in md:
    print("Key 'Mango' exists in Dictionary")
else:
    print("Key 'Mango' doesn't exists in Dictionary")

for i,j in md.items():
    print(i,":",j)

dict1 = {"Cherry": 2, "banana": 6}
dict2 = {"orange": 4, "pear": 5}
concat_dict = {**dict1, **dict2}
print("Concatenated dictionary:", concat_dict)

sum = sum(md.values())
print("Sum of values in Dictionary:", sum)

max = max(md.values())
min = min(md.values())
print("Maximum value in Dictionary", max)
print("Minimum value in Dictionary", min)