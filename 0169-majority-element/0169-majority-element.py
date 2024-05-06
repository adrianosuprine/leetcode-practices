class Solution(object):
    def majorityElement(self, nums):
        nums.sort()
        N = len(nums)

        return nums[N//2]

              
[7,9,9,0,9,9,7]

        