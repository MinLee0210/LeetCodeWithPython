from typing import List


def findTheDistanceValue(arr1: List[int], arr2: List[int], d: int) -> int:
    count = 0
    temp = 0
    left = 0
    while left < len(arr1):
        for i in range (0, len(arr2)):
            distance = abs(arr1[left] - arr2[i])
            if distance > d:
                temp += 1
            else:
                temp -= 1
        if temp == len(arr2):
            count += 1
        left += 1
        temp = 0
    return count

# arr1 = [4,5,8] 
# arr2 = [10,9,1,8]

arr1 = [1,4,2,3] 
arr2 = [-4,-3,6,10,20,30]
print(findTheDistanceValue(arr1, arr2, 3))

# Other solution: Using binary search for sorted array reduce the complexity of searching to O(log(n))

# def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
    
# 	arr2.sort()
# 	low = 0
# 	high = len(arr2) - 1
# 	count = 0

# 	for n in arr1:
# 		while low <= high:
# 			mid = low + (high-low)//2
# 			if abs(n - arr2[mid]) <= d:
# 				count -= 1 # to counter 'count += 1' in end of loop
# 				break
# 			elif n <= arr2[mid]:
# 				high = mid - 1
# 			else:
# 				low = mid + 1
# 		low = 0
# 		high = len(arr2) - 1
# 		count += 1    

# 	return count