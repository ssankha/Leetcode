# 2491. Divide Players Into Teams of Equal Skill (Medium) 
class Solution(object):

    def dividePlayers(self, skill):
        """
        :type skill: List[int]
        :rtype: int
        """
        def merge(arr, left, mid, right):
            left_arr = arr[left:mid+1]
            right_arr = arr[mid+1:right+1]
            

            i = 0  
            j = 0  
            k = left  
            
            #print(left_arr, right_arr)

            # merge the arrays
            while i < len(left_arr) and j < len(right_arr):
                if left_arr[i] <= right_arr[j]:
                    arr[k] = left_arr[i]
                    i += 1
                else:
                    arr[k] = right_arr[j]
                    j += 1
                k += 1

            # copy left over elements
            while i < len(left_arr):
                arr[k] = left_arr[i]
                i += 1
                k += 1

            # Copy the remaining elements of R[], 
            # if there are any
            while j < len(right_arr):
                arr[k] = right_arr[j]
                j += 1
                k += 1

        def sort(arr, left, right):
            if left < right:
                mid = (left + right) // 2

                sort(arr, left, mid)
                sort(arr, mid + 1, right)
                merge(arr, left, mid, right)
                
        sort(skill, 0, len(skill) - 1)
        
        print(skill)
        
        total_skill = 0
        for num in skill:
            total_skill += num
        
        target = total_skill / (len(skill) / 2)

        i = 0
        j = len(skill) - 1
        chemistry = 0
        while i < j:
            if skill[i] + skill[j] != target:
                return -1
            else:
                chemistry += skill[i] * skill[j]
                
            i += 1
            j -= 1
        
        return chemistry

    
sol = Solution()

# Example input
skill = [5,4,1,1,5,2]

# Call the dividePlayers method
result = sol.dividePlayers(skill)

# Print the result
print(result)