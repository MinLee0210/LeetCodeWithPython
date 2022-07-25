import operator
# def findDisappearedNumbers(nums):
#     result= []
#     for num in range(1, len(nums) +1):
#         if num not in nums:
#             result.append(num)
            
#     return result

def findDisappearedNumbers(nums):
    # filter = [i for i in range(1, len(nums) + 1)]
    # nums.sort()
    # for num in nums:
    #     if num in filter: 
    #         filter.remove(num)
    # return filter
    if not nums:
        return None
    return list(set(range(1, len(nums) + 1)) - set(nums))
print(findDisappearedNumbers([4,3,2,7,8,2,3,1]))
print(findDisappearedNumbers([1,1]))