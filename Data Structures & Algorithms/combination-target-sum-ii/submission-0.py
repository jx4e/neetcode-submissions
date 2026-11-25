class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []

        def backtrack(i, csum, tot):
            if tot == target:
                res.append(csum.copy())
                return
            
            if i >= len(candidates) or tot > target:
                return
            
            csum.append(candidates[i])
            backtrack(i + 1, csum, tot + candidates[i])
            csum.pop()

            while i + 1 < len(candidates) and candidates[i] == candidates[i + 1]:
                i += 1

            backtrack(i + 1, csum, tot)
        
        backtrack(0, [], 0)
        return res