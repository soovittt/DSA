class Solution:
    def asteroidCollision(self, asteroids):
        stack = []
        if not asteroids:
            return []
        stack.append(asteroids[0])
        for asteroid in asteroids[1:]:
            print("the asteroid is",asteroid)
            if(asteroid>0 and stack[-1]>0):
                print("went here now")
                stack.append(asteroid)
            elif(asteroid<0 and stack[-1]<0):
                print("went here now 2")
                stack.append(asteroid)
            elif(asteroid<0 and stack[-1]>0):
                print("went here now 3")
                if(abs(asteroid)>abs(stack[-1])):
                    print("went here now 4")
                    stack.pop()
                    stack.append(asteroid)
                elif(abs(asteroid)<abs(stack[-1])):
                    print("went here now 5")
                    pass
                else:
                    print("went here now 6")
                    stack.pop()
        print(stack)
        
sol = Solution()
sol.asteroidCollision([10,2,-5])
            