# 70. Climbing Stairs (Easy)
class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """

        ways = []
        for i in range(n):
            if i == 0:
                ways.append(1)
            elif(i == 1):
                ways.append(2)
            else:
                ways.append(ways[i - 1] + ways[i - 2])
                
        return ways[n - 1]

sol = Solution()
n = 90
result = sol.climbStairs(n)
print(result)
                
        
        
