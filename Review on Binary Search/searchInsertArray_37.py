from unicodedata import category


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if target in nums:
            return nums.index(target)
        else:
            i = 0
            while( i < len(nums)):
                if nums[i] > target:
                    return nums.index(target)
                i += 1
            return len(nums)
        
    # def searchInsert(self, nums: List[int], target: int) -> int:
    #     left, right = 0, len(nums) - 1
    #     while(left <= right):
    #         mid = left + (right - left)//2
    #         if(target == nums[mid]):
    #             return mid
    #         elif target < nums[mid]:
    #             right = mid - 1
    #         else:
    #             left = mid + 1
    #     return left
    
    # Note: Too focus on type of the category of the exercise more than itself