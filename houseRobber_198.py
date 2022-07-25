def rob(nums): 
    nums.append(0)
    nums.append(0)

    dp = [0] * len(nums)
    
    for i in range(len(nums)):
        dp[i] = max(nums[i] + dp[i - 2], dp[i - 1])
    return dp
print(rob([1, 2, 3, 1]))
print(rob([2,7,9,3,1]))

    #   # memoized recursion
    #     memo = {}
	# 	def robFrom(idx, nums):
    #          if idx in memo:
    #              return memo[idx]
    #          if idx >= len(nums):
    #              return 0
            
    #          ans = max(robFrom(idx + 1, nums), robFrom(idx + 2, nums) + nums[idx])
    #          memo[idx] = ans
    #          return ans
        
    #      return robFrom(0, nums)
    #     # dynamic programming
    #     nums.append(0)
    #     nums.append(0)

    #     dp = [0] * len(nums)
        
    #     for i in range(len(nums) -3, -1, -1):
    #         dp[i] = max(nums[i] + dp[i + 2], dp[i + 1])
    #     return dp[0]         
    #     # dynamic programming, space O(1)

    #     next1 = 0
    #     next2 = 0
        
    #     for i in range(len(nums) - 1, -1, -1):
    #         tmp = max(nums[i] + next2, next1)
    #         next2 = next1
    #         next1 = tmp
    #     return tmp