class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:

        res = [[]]

        for num in nums:
            res += [i + [num] for i in res]
        
        for i in range(len(res)):
            res[i] = sorted(res[i])

        res = set((tuple(i)) for i in res)
        
        return list(res)

        