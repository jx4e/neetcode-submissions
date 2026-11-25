class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def backtrack(s, l, r):
            if len(s) == n * 2:
                res.append(s)
                return

            if r > l:
                return
            
            if l < n:
                backtrack(s + '(', l + 1, r)
            
            if r < n:
                backtrack(s + ')', l, r + 1)

        backtrack('', 0, 0)
        return res