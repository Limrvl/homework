import time
from datetime import datetime
file = open("ai183.txt", "r")
nums = []
test1 = False
test2 = False

while True:
    check = file.read(1)
    if not check:
        break

    if check == "1":
        check = file.read(1)
        if check == "1":
            test1 = True
            check = file.read(1)
            if check == ":":
                test2 = True

    if test1 == True and test2 == True:
        file.seek(file.tell() + 1)
        check = file.read(1)
        while check != "}":
            nums.append(int(check))
            check = file.read(1)
        break

file.close()
print("Array: ", nums)

def find_smallest(nums):
	smallest = nums[0]
	smallest_index = 0
	for i in range(1, len(nums)):
		if nums[i] < smallest:
			smallest = nums[i]
			smallest_index = i
	return smallest_index

def main_sort(nums):
    new_arr = list()
	for i in range(len(nums)):
        smallest = find_smallest(nums)
		new_arr.append(nums.pop(smallest))

    return new_arr

start_time = datetime.now()
print("Quick sorted array: ", main_sort(nums))
end_time = datetime.now()
print('---Duration: {}'.format(end_time - start_time))