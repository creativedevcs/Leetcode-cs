class Solution:
    def longestPalindrome(self, s: str)->str:
        l = []
        for i in range (len (s)):
            for j in range (i + 1, len (s) + 1):
                l.append (s[i:j])
        #print(l)
        length=-1
        d=dict()
        for i in l:
            if i==i[::-1]:
                length=1
            else:
                length=-1
            if length==1:
                if i not in d:
                    d[i]=len(i)
        #print(d)
        #h=d.get('b')
        # keys=list(d.keys())
        # values=list(d.values())
        # pos=values.index(max(d.values()))
        # reqkey=keys[pos]
        # return reqkey
        d=dict(sorted(d.items(),key=lambda x:(-x[1],x[0])))
        return list(d.keys())[0]
