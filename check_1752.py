from typing import List

def check(nums:List[int]):
    original_arr = nums.copy()
    original_arr.sort()
    flag = 0
    count = 0
    while flag < len(original_arr):
        for i in range(0, len(nums)):
            if(nums[i] == original_arr[(i + flag) % len(original_arr)]):
                count += 1
        if count == len(nums):
            return True
        count = 0
        flag += 1
    return False

print(check([3, 4, 5, 1, 2]))
print(check([2, 1, 3, 4]))
print(check([1, 3, 2]))