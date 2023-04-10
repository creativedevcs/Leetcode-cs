class Solution:
    def isValid(self, s: str) -> bool:
        stackseen=[]
        d={')':'(',']':'[','}':'{'}
        for i in s:
            if i in d:
                if stackseen and stackseen[-1]==d[i]:
                    stackseen.pop()
                else:
                    return False
            else:
                stackseen.append(i)
        return stackseen==[]
