def minSubArrayLen(target, nums):
    left = 0
    right = len(nums) + 1
    temp = 0
    
    for i in range(len(nums)):
        temp += nums[i]
        # When the temp number is larger the target, we resize the list and decrease the sum
        while temp >= target:
            # We will reduce the upper-bound
            right = min(i - left + 1, right)
            temp -= nums[left]
            left += 1
            
    return 0 if right == len(nums) else right 
        
target = 7
nums = [2,3,1,2,4,3]

print(minSubArrayLen(target, nums))