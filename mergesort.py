numbers = [5, 2, 8, 1, 3]

def divide(numbers):

    if len(numbers) <= 1:
        return numbers

    mid = len(numbers) // 2

    left = numbers[:mid]
    right = numbers[mid:]

    left = divide(left)
    right = divide(right)

    return left, right

def merge(left, right):
    merged = []
    i = j = 0

    

divide(numbers)
  
