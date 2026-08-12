class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:

        length = len(arr)
        maxm = arr[-1] 

        for i in range(length - 2,-1,-1):
            curr = arr[i]
            arr[i] = maxm
            if curr > maxm:
                maxm = curr
        arr[-1] = -1
        return arr

# length = len(arr)
#         maxm = -1
#         for i in range(length-1,-1,-1):
#             current = arr[i]
#             arr[i] = maxm
#             if current > maxm:
#                 maxm = current
#         return arr