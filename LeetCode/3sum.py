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
        for x in range(len(nums)):
            for y in range(x+1,len(nums)):
                for z in range(y+1,len(nums)):
                    sum = nums[x]+nums[y]+nums[z]
                    if sum == 0:
                        arr = sorted([nums[x],nums[y],nums[z]])
                        print(arr)


Solution.threeSum(0, nums = [-1, 0, 1, 2, -1, -4])
