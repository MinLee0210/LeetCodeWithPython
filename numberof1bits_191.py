class Solution:
    def hammingWeight(self, n:int) -> int:
        tempString = str(bin(n))
        count = 0
        for i in tempString:
            if i == "1":
                count += 1
        return count          
    
a = Solution()
num = 0o001011110101
print(a.hammingWeight(num))
