class Solution:
    def search(self, nums: List[int], target: int) -> int:
        found = False 
        first = 0
        last = len(nums)-1
        
        while first <= last:
            mid = (first + last) // 2 
            # print("mid is ", mid, " first is ", first, " last is ", last)
            if target == nums[mid]:
                return mid
            elif target < nums[mid]:
                last = mid - 1
            else:
                first = mid + 1
            
            
        return -1 
        