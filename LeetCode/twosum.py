class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        sum = 0
        for x in range(len(nums)):
            for y in range(x+1,len(nums)):
                sum = nums[x] + nums[y]
                if sum == target:
                    print([x,y])
                else:
                    continue 
            
Solution.twoSum(0, nums = [3, 2, 4], target = 6)
