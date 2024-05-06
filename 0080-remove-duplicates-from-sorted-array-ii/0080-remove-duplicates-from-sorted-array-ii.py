class Solution(object):
    def removeDuplicates(self, nums):
        # nums[:]

        for i in nums[:]:
            if nums.count(i) > 2:
                nums.remove(i)
            k = len(nums)
        return k
                
        