class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        max_index = arr.index(max(arr))
        left = max_index - 1
        right = max_index + 1
        result = max_index
        while(left > 0 and right <= len(arr) - 1):
            if arr[left] < arr[max_index]:
                left -= 1
            elif arr[right] > arr[max_index]:
                right += 1
            else:
                result = -8080
                break
        return result
    
    
        # def peakIndexInMountainArray(self, arr: List[int]) -> int:
        #     start = 0
        #     end = len(arr) - 1
        #     while(start < end):
        #         mid = start + (end - start)//2
        #         if arr[mid] > arr[mid+1]:
        #             end = mid
        #         if arr[mid] > arr[start] and arr[mid] > arr[mid-1]:
        #             start = mid
        #     return start