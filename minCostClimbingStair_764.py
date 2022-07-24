# You are given an integer array cost where cost[i] is the cost of ith step on a staircase. Once you pay the cost, 
# you can either climb one or two steps.
#  -> Number of step for each time climbing is either 1 or 2
# You can either start from the step with index 0, or the step with index 1.

# Return the minimum cost to reach the top of the floor.

def minCostClimbingStair(cost):  
    for i in range(2,len(cost)):
        cost[i] = min(cost[i-1],cost[i-2])+cost[i]
    return min(cost[-1],cost[-2])

print(minCostClimbingStair([1,100,1,1,1,100,1,1,100,1]))

# class Solution(object):
#     def minCostClimbingStairs(self, cost):
#         """
#         :type cost: List[int]
#         :rtype: int
#         """
#         #Top-to-Bottom Approach
#         dp = [-1]*(len(cost))
#         return min(self.topToBottom(cost,dp,len(cost)-1),self.topToBottom(cost,dp,len(cost)-2))
    
#     def topToBottom(self,cost,dp,n):
#         if(n == 0 or n ==1):
#             return cost[n]
        
#         elif(dp[n]!=-1):
#             return dp[n]
#         dp[n] = cost[n]+min(self.topToBottom(cost,dp,n-1),self.topToBottom(cost,dp,n-2))
#         return dp[n]