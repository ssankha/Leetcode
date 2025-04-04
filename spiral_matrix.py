class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        topRow = 0
        leftCol = 0
        rightCol = len(matrix[0]) - 1
        bottomRow = len(matrix) - 1

        res = []
        
        while leftCol <= rightCol and topRow <= bottomRow:
            
            i = leftCol
            while i <= rightCol:
                res.append(matrix[topRow][i])
                i += 1
            
            topRow += 1
            
            i = topRow    
            while i <= bottomRow:
                res.append(matrix[i][rightCol])
                i += 1
            rightCol -= 1
            
            if not (leftCol <= rightCol and topRow <= bottomRow):
                break
            
            i = rightCol
            while i >= leftCol:
                res.append(matrix[bottomRow][i])
                i -= 1
            
            bottomRow -= 1
            
            i = bottomRow 
            while i >= topRow:
                res.append(matrix[i][leftCol])
                i -= 1
            
            leftCol += 1
        
            
        return res

            


test = Solution()

input = [[1,2,3],[4,5,6],[7,8,9]]
#input = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
print(test.spiralOrder(input))