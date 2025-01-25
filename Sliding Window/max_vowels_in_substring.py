class Solution:
    def maxVowels(self, s: str, k: int) -> int:

    	'''
		start with a initial window and clauclate intiitail value of num vowels 
		then move the window to calculate the next number of vowels and so on
    	'''

    	n = len(s)
    	vowels = ["a","e","i","o","u"]
    	window_vowel = 0
    	for i in range(0,k):
    		if s[i] in vowels:
    			window_vowel+=1
    	print(window_vowel)

sol = Solution()
sol.maxVowels("leetcode",3)




