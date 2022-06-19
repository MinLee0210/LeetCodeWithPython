from typing import List

def search(nums:List[int], target:int) -> int:
    return binarySearch(nums, 0, len(nums) - 1, target)

def binarySearch(nums, left, right, target) -> int:
    if(right >= left):
        mid = left + (right - left) // 2
        if(nums[mid] == target):
            return mid      
        elif(nums[mid] > target):
            return binarySearch(nums, left, mid - 1, target)
        else:
            return binarySearch(nums, mid + 1, right, target)
    else:
        return -1
    
nums=[-1, 0, 1, 3, 9, 10]
print(search(nums, 9))
        