
def quicksort(nums):
	if len(nums) < 2:
		return nums
	else:
		sup = nums[]
		less = [i for i in nums[1:] if i <= sup]
		greater = [i for i in nums[1:] if i > sup]
		return quicksort(less) + [sup] + quicksort(greater)

nums = [125,43,67,16,27,89]

print(quicksort(nums))





