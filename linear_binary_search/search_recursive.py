linear_comparisons = 0
binary_comparisons = 0


def linear_search(numbers, index, key, ):
    global linear_comparisons
    linear_comparisons += 1
    if index == len(numbers) - 1:
        return -1
    if numbers[index] == key:
        return index
    else:
        return linear_search(numbers, index + 1, key)


def binary_search(numbers, low, high, key, ):
    global binary_comparisons
    binary_comparisons += 1
    if low > high:
        return -1

    middle = (low + high) // 2

    if numbers[middle] < key:
        return binary_search(numbers, middle + 1, high, key)
    elif numbers[middle] > key:
        return binary_search(numbers, low, middle - 1, key)
    else:
        return middle


numbers = [12, 75, 18, 22, 94, 16, 22]
print(numbers)

key = int(input("enter an integer key to search for"))

result = linear_search(numbers, 0, key)

if result != -1:
    print(f"element {key} was found at index {result} after {linear_comparisons}")
    print("linear")
else:
    print(f"element {key} was not found in the list after {linear_comparisons}")
    print("linear")

result = binary_search(numbers, 0, len(numbers) - 1, key)

if result != -1:
    print(f"element {key} was found at index {result} after {binary_comparisons} attempts ")
    print("binary")
else:
    print(f"element {key} was not found in the list after {binary_comparisons} attempts")
    print("binary")
