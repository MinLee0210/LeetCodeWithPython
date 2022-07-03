
def minSubArrayLen(target, nums):
    result = []
    if target in nums:
        result.append(nums.index(target))
    else:
        sum = 0
        for i in range(0, len(nums)):
            left = i
            right = len(nums) - 1
            while(left <= right):
                mid = left + (right - left)//2
                if sum <= target:
                    sum += nums[mid]
                    left = mid + 1
                else:
                    right = mid - 1
                    
    return len(result)

nums = [2,3,1,2,4,3]
target = 3
print(minSubArrayLen(target, nums))

