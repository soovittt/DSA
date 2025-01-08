
class Solution:
    #This is the recursive method
    def gcdOfStrings_recur(self, str1, str2): # -> The time complexity is is NlogB
        if(len(str2) > len(str1)):
            return self.gcdOfStrings(str2, str1)
        elif(not str1.startswith(str2)):
            return ""
        elif(len(str2)==0):
            return str1
        else:
            return self.gcdOfStrings(str1[len(str2):],str2)
        
    def gcdOfStrings(self, str1, str2):
        len_1 , len_2  = len(str1) , len(str2)
        def isDivisor(l):
            if(len_1%l or len_2%l):
                return False
            f1 , f2 = len_1//l , len_2//l
            return str1[:l]*f1 == str1 and str1[:l]*f2==str2
        
        for l in range(min(len_1,len_2),0,-1):
            if isDivisor(l):
                return str1[:l]
        return ""

