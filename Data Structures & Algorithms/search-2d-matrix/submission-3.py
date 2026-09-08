class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        r,c = len(matrix),len(matrix[0])

        top = 0
        bot = r - 1

        while top <= bot:

            row = (top + bot)//2
            if target < matrix[row][0]:
                bot = row - 1
            elif target > matrix[row][-1]:
                top = row + 1
            else:
                l,r = 0, c - 1
                while l <= r:
                    mid = (l + r)//2

                    if target == matrix[row][mid]:
                        return True
                    elif target < matrix[row][mid]:
                        r = mid - 1
                    else:
                        l = mid + 1
                return False        
        return False


        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        # r,c = len(matrix),len(matrix[0])

        # top,bot = 0, r-1

        # while top <= bot:
        #     row = (top + bot) // 2
        #     if target > matrix[row][-1]:
        #         top = row + 1
        #     elif target < matrix[row][0]:
        #         bot = row - 1
        #     else:
        #         l,r = 0, c - 1
        #         while l <= r:
        #             mid = (l + r)//2
        #             if matrix[row][mid] == target:
        #                 return True
        #             elif matrix[row][mid] < target:
        #                 l = mid + 1
        #             else:
        #                 r = mid - 1
        #         return False            
        # return False
            
