
# Time exceeding.
# def findDuplicates(numList):
#     bloomingFilter = [False]*len(numList)
#     result = []
#     for num in numList: 
#         numIndex = numList.index(num)
#         bloomingFilter[numIndex] = True
#     for i in range(len(bloomingFilter)): 
#         if bloomingFilter[i] == False:
#             result.append(numList[i])
#     return result

def findDuplicates(nums): 
    filter = [0]*(len(nums) + 1)
    result = []
    for num in nums: 
        if filter[num] == 0:
            filter[num] += 1
        elif filter[num] == 1:
            result.append(num)
    return result

print(findDuplicates([4,3,2,7,8,2,3,1]))