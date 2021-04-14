#https://leetcode.com/problems/valid-parentheses/submissions/
class Solution(object):    
    def match(self, lastAdded, character):
        if lastAdded == "{":
            if character == "}":
                return True
        elif lastAdded == "(":
            if character == ")":
                return True
        elif lastAdded == "[":
            if character == "]":
                return True
        return False

    def isValid(self, s):
        pila = []
        for i in range(len(s)):
            if i == 0:
                pila.append(s[i])
            else:
                if(len(pila) > 0):
                    if(self.match(pila[len(pila) - 1], s[i])):
                        pila.pop()
                    else:
                        pila.append(s[i])
                    
                else:
                    pila.append(s[i])
                
        if(len(pila) == 0): return True
        print(pila)
        return False
