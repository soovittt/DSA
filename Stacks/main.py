def isValid(s) -> bool:
        paranthesis_stack = []
        mapping = {')': '(', '}': '{', ']': '['}
        for char in s:
            print("current char : ",char)
            if char in mapping.values():
                paranthesis_stack.insert(0,char)
                print("stack 1 : " , paranthesis_stack)
            elif char in mapping.keys():
                if paranthesis_stack and paranthesis_stack[0] == mapping[char]:
                    paranthesis_stack.pop(0)
                    print("stack 2 : " ,paranthesis_stack)
                else:
                    return False
            else:
                return False
        return not paranthesis_stack

print(isValid("([)]"))