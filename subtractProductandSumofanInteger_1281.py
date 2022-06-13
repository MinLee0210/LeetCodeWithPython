from math import prod


class Solution:
    def subtractProductAndSum(self, n:int) -> int:
        product, sum = [], []
        
        n = str(n)
        
        for i in n:
            product.append(int(i))
            sum.append(int(i))
            
        productNum, sumNum = 1, 0
        for i in range (0, len(product)):
            productNum = productNum * product[i]
            sumNum = sumNum + sum[i]

        return productNum - sumNum
    
test = Solution()
num = 234
print(test.subtractProductAndSum(num))