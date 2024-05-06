class Solution(object):
    def twoSum(self, nums, target):
        result = []
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                sum = nums[i] + nums[j]
                if sum == target:
                    result.append(i)
                    result.append(j)
        return result

        

        

        