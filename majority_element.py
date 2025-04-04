class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 0
        res = 0

        for num in nums:
            
            if count == 0:
                res = num
            
            
            if res == num:
                count += 1
            else:
                count -= 1
        
        return res
    
    
test = Solution()
input = [-9, -8, -7, 6, 6, 6, 4, 3, -9, 9, -9, -9, 7, -9]
print(test.majorityElement(input))