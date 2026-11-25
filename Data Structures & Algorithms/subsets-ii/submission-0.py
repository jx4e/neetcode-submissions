class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        res = []
        n = len(nums)

        def find_subsets(i, csub):
            if i >= n:
                res.append(csub.copy())
                return
            
            csub.append(nums[i])
            find_subsets(i + 1, csub)

            while i + 1 < n and nums[i + 1] == nums[i]:
                i += 1
            
            csub.pop()
            find_subsets(i + 1, csub)
        
        find_subsets(0, [])
        return res

