def linear_search(numbers, key):
    Comparison = 0
    for i in range(len(numbers)):
        if numbers[i] == key:
            Comparison += 1
            return i, Comparison
    return -1, Comparison


def binary_search(number, keys):
    Comparison = 0
    low = 0
    high = len(number) - 1
    middle = len(number) // 2

    while high >= low:
        middle = (high + low) // 2
        Comparison += 1

        if number[middle] < keys:
            low = middle + 1

        elif number[middle] > keys:
            high = middle - 1

        else:
            return middle, Comparison
    return -1, Comparison


numbers = [2, 4, 7, 10, 11, 32, 45, 87]
print('numbers:', numbers)

key = int(input('enter and integer key to search for:'))
# print(Comparison)
key_index, attempts = linear_search(numbers, key)
key_index_binary, attempts_binary = binary_search(numbers, key)
print("linear:", key_index)
print("linear search number of attempts", attempts)
print("binary:", key_index_binary)
print("binary search attempts", attempts_binary)
