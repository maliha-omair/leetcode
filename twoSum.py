
class Solution:
    def twoSum(self, nums, target):
        dict = {}
        for indx in range(0,len(nums)):
            key = target - nums[indx]
            if key in dict.keys():
                return ([dict[key],indx])
            else:
                newKey = nums[indx]
                dict[newKey] =  indx

obj = Solution()
print(obj.twoSum([2,7,11,15], 9))
