def binary_search(list, item):
    low = 0
    high = len(list) - 1

    while low <= high:
        mid = int((low + high)/2)
        print(mid)
        guess = list[mid]

        if guess == item:
            return mid
        if guess > item:
            high = mid - 1

        if guess < item:
            low = mid + 1

    return None


list1 = list(range(0,129))
item = 65

print(binary_search(list1,item))