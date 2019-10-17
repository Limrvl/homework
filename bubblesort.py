nums = [125,43,67,16,27,89]

def bubbleSort(nums):
 for i in range(len(nums)-1):
  for j in range(len(nums)-i-1):
   temp = nums[j]
   if temp > nums[j+1]:
    nums[j],nums[j+1] = nums[j+1],temp
 return nums
 
print(bubbleSort(nums))