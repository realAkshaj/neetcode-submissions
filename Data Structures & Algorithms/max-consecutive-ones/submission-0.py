class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        
        maxm = 0
        curr = 0
        for i in range(len(nums)):

            if nums[i] == 1:
                curr += 1
                maxm = max(curr,maxm)
            else:               
                curr = 0
        
        return maxm
