class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        matrix = [[0 for _ in range(n)] for _ in range(n)]
        
        topRow = 0
        botRow = n - 1
        leftCol = 0
        rightCol = n - 1
        
        x = 1
        while topRow <= botRow and leftCol <= rightCol:
            
            i = leftCol
            while i <= rightCol:
                matrix[topRow][i] = x
                i += 1
                x += 1
            
            topRow += 1
            
            i = topRow
            while i <= botRow:
                matrix[i][rightCol] = x
                i += 1
                x += 1
            
            rightCol -= 1
            
            if not (topRow <= botRow and leftCol <= rightCol):
                break
            
            i = rightCol
            while i >= leftCol:
                matrix[botRow][i] = x
                i -= 1
                x += 1
            
            botRow -= 1
            
            i = botRow
            while i >= topRow:
                matrix[i][leftCol] = x
                i -= 1
                x += 1
                
            leftCol += 1
        
        return matrix
            
            