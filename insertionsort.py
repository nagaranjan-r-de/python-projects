numbers = [5, 2, 8, 1, 3]

insertion_sorted = []

for i in range(len(numbers)):
    if insertion_sorted[i] < numbers[i]:
        insertion_sorted.append(numbers[i])
    else:
        insertion_sorted.insert(i, numbers[i])

print(insertion_sorted)