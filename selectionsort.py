numbers = [5, 2, 8, 1, 3]

sorted_numbers = []
for i in range(len(numbers)):
    num = min(numbers)
    sorted_numbers.append(num)
    numbers.remove(num)

print(sorted_numbers)