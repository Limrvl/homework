nums = [125,43,67,16,27,89]

def insertionSort(nums):
    for i in range(len(nums)):
        tmp = nums[i]
        j = i - 1
        while j >= 0 and tmp < nums[j]:
            nums[j+1], nums[j] = nums[j], nums[j+1]
            j -= 1
    return nums

print(insertionSort(nums))