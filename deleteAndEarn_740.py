from collections import Counter

def deleteAndEarn(nums):
    count = Counter(nums)
    keys = sorted(count)
    N = len(keys)
    dp = [0]*(N + 1)
    
    for i in range(N): 
        if i != 0 and keys[i] == keys[i-1] + 1: 
            dp[i+1] = max(dp[i-1] + keys[i]*count[keys[i]], dp[i])
        else: 
            dp[i+1] = dp[i] + keys[i]*count[keys[i]]
            
    return dp

print(deleteAndEarn([3, 4, 2]))
print(deleteAndEarn([2, 2, 3, 3, 3 ,4]))