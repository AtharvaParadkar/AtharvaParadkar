numbers = [5, 2, 9, 1, 7]
unique_numbers = set(numbers)
unique_numbers.remove(max(unique_numbers))
second_largest = max(unique_numbers)

print("Second Largest Number:", second_largest)
