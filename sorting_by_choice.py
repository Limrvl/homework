def find_smallest(arr):
	smallest = arr[0]
	smallest_index = 0
	for i in range(1, len(arr)):
		if arr[i] < smallest:
			smallest = arr[i]
			smallest_index = i
	return smallest_index

def main_sort(arr):
    new_arr = list()
	for i in range(len(arr)):
        smallest = find_smallest(arr)
		new_arr.append(arr.pop(smallest))

    return new_arr

arr = [125,43,67,16,27,89]

print(arr)

print(main_sort(arr))