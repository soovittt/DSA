class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split()
        words = words[::-1]
        print(words)
        return ' '.join(words)


sol = Solution()
print(sol.reverseWords("the sky is blue"))