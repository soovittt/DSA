class Solution:
    def reverseWords(self, s):
        reversed_string = []
        for element in s:
            if(element!=" "):
                reversed_string.insert(0,element)
        print(reversed_string)

sol = Solution()
sol.reverseWords("the sky is blue")

        