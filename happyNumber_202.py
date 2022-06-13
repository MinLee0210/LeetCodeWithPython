class Solution:
        
    # Iterative solution
    def isHappy(self, n: int) -> bool:
        # flag = 0
        while(n != 1):
            sum = 0
            tempString = str(n)
            tempArr = [int(i) for i in tempString]
            for i in tempArr:
                sum += i**2
            n = sum
        return True
    
    #Another solution
        #     def get_sum(n):
        #     s = str(n)
        #     a = 0
        #     for i in s:
        #         a += int(i)**2
        #     return a
        
        # visited = set()
        # while(n != 1):
        #     #print(n)
        #     visited.add(n)
        #     n = get_sum(n)
        #     if n in visited:
        #         return False
        
        # return True
# ex = Solution()
# print(ex.isHappy(19))

# ex1 = Solution()
# print(ex1.isHappy(2))

# Recursion solution
def rec(a,b):
    if(b==1):
        return True
    if(b in a):
        return False
    a.append(b)
    c=0
    while(b>0):
        c+=(b%10)**2
        b//=10
    return rec(a,c)

print(rec([], 19))
    