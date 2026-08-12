class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        st = set(nums)
        maxLen = 0

        for num in st:

            if (num - 1) not in st:

                length = 1
                maxLen = max(maxLen,length)
                
                while (num + length) in st:

                    length += 1
                    maxLen = max(maxLen,length)
        
        return maxLen