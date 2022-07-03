import sys
from typing import List

def searchRange(nums: List[int], target:int) -> List[int]:
    result = []
    left = 0
    right = len(nums) - 1
    while(left <= right):
        mid = left + (right - left)//2
        if(nums[mid] == target):
            result.append(mid)
            nums.remove(nums[mid])
            print('{} - {} - {}'.format(mid, result, nums))
            right = len(nums) - 1
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
            
    result.sort()
    if len(result) != 0:
        return result
    return[-1, -1]

# nums = [5,7,7,8,8,10] 
# target = 6
nums = []
target = 0
print(searchRange(nums, target))

# def searchRange(self, nums: List[int], target: int) -> List[int]:
#     def binary_search(flag):
#         low=0
#         high=len(nums)-1
#         result=-1
#         while(low<=high):
#             mid=low + (high-low)//2
#             if nums[mid]==target:
#                 result=mid
#                 if flag:
#                     high=mid-1
#                 else:
#                     low=mid+1
#             elif target < nums[mid]:
#                 high=mid-1
#             else:
#                 low=mid+1
#         return result
      
    
#     start=binary_search(True)
#     end=binary_search(False)
#     return [start,end]