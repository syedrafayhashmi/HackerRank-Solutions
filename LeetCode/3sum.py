# Given array nums = [-1, 0, 1, 2, -1, -4],
# a+b+c=0
# A solution set is:
# [
#   [-1, 0, 1],
#   [-1, -1, 2]
# ]


class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        sum = 0
        out = []
        for x in xrange(len(nums)):
            for y in xrange(x+1,len(nums)):
                for z in xrange(y+1,len(nums)):
                    sum = nums[x]+nums[y]+nums[z]
                    if sum == 0:
                        arr = sorted([nums[x],nums[y],nums[z]])
                        if arr not in out:
                            out.append(arr)
        return out

Solution.threeSum(0, nums = [-1, 0, 1, 2, -1, -4])
