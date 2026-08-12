class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        n = len(nums)
        postfix = [1] * n
        prefix = [1] * n

        for i in range(1,n):

            prefix[i] = prefix[i-1] * nums[i-1]
        
        # print(prefix)    

        for i in range(n-2,-1,-1):

            postfix[i] = postfix[i+1] * nums[i+1]
        
        # print(postfix)
        result = []

        for i in range(n):

            result.append(postfix[i] * prefix[i])

        return result


