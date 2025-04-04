class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = [0] * len(nums)

        if(len(nums) == 1):
            return nums[0]
        
        if(len(nums) == 2):
            return max(nums[0], nums[1])

        res[0] = nums[0]
        res[1] = nums[1]

        for i in range(1, len(nums) - 2):
            res[i + 1] = max(res[i] + nums[i + 2],  res[i - 1])

        return res

test = Solution()

input = [2, 1, 1, 2]
print(test.rob(input))