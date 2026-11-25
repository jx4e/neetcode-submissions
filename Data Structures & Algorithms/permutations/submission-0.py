class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)
        used = [False] * n

        def backtrack(cperm):
            if len(cperm) == n:
                res.append(cperm.copy())
                return
            
            for i, x in enumerate(nums):
                if used[i]:
                    continue
                
                used[i] = True
                cperm.append(x)
                backtrack(cperm)

                used[i] = False
                cperm.pop()
        
        backtrack([])
        return res
