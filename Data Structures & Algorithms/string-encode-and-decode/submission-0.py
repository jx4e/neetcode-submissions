class Solution:

    def encode(self, strs: List[str]) -> str:
        message = ''
        for s in strs:
            prefix = str(len(s)) + '!'
            message += prefix + s
        
        return message

    def decode(self, s: str) -> List[str]:
        strs = []
        i = 0

        while i < len(s):
            j = i
            while s[j] != '!':
                j += 1
            length = int(s[i:j])
            strs.append(s[j + 1 : j + 1 + length])
            i = j + 1 + length

        return strs
        
            