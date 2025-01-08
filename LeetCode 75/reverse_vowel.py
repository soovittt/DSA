class Solution:
    def reverse_dict_values(self,d):
        # Step 1: Extract and reverse the values
        reversed_values = list(d.values())[::-1]
    
        # Step 2: Create a new dictionary with reversed values
        reversed_dict = {key: reversed_values[i] for i, key in enumerate(d.keys())}
    
        return reversed_dict
    
    
    def reverseVowels_slow(self, s: str) -> str:
        vowels = set('aeiouAEIOU')
        vowel_in_string , non_vowel_in_string = {} , {}
        for index in range(0,len(s)):
            if s[index] in vowels:
                vowel_in_string[index] = s[index]
            else:
                non_vowel_in_string[index] = s[index]
        vowel_in_string = self.reverse_dict_values(vowel_in_string)
        combined_dict = vowel_in_string.copy()
        combined_dict.update(non_vowel_in_string)
        sorted_dict = {key: combined_dict[key] for key in sorted(combined_dict)}
        combined_string = ''.join(sorted_dict.values())
        return combined_string
    
    def reverseVowels(self, s):
        vowels = set('aeiouAEIOU')
        i = 0 
        j = len(s) - 1
        st = list(s)
        while(i<j):
            if(s[i] in vowels and s[j] in vowels):
                temp = st[i]
                st[i] = st[j]
                st[j] = temp
                i+=1
                j-=1
            if(st[i] not in vowels):
                i+=1
            if(st[j] not in vowels):
                j-=1
        return "".join(st)




sol = Solution()
print(sol.reverseVowels("leetcode"))