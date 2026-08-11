class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        
        count = Counter(nums)
        bucket = [[] for _ in range(len(nums) + 1)]
        
        for key, value in count.items():

            bucket[value].append(key)

        res = []
        for i in range(len(nums), 0, -1):
            for n in bucket[i]:
                res.append(n)
                if len(res) == k:
                    return res
