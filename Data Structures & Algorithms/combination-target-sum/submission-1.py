class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []

        def backtrack(i, csum, tot):
            if tot == target:
                result.append(csum.copy())
                return
            
            if i >= len(nums) or tot > target:
                return
            
            csum.append(nums[i])
            backtrack(i, csum, tot + nums[i])
            csum.pop()
            backtrack(i + 1, csum, tot)
        
        backtrack(0, [], 0)

        return result
