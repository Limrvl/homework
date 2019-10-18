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

def quick_sort(nums):
    less = []
    equal = []
    greater = []

    if len(nums) > 1:
        first = nums[0]
        for number in nums:
            if number < first:
                less.append(number)
            elif number == first:
                equal.append(number)
            elif number > first:
                greater.append(number)
        return quick_sort(less) + equal + quick_sort(greater)
    else:
        return nums


start_time = datetime.now()
print("Quick sorted array: ", quick_sort(nums))
end_time = datetime.now()
print('---Duration: {}'.format(end_time - start_time))





