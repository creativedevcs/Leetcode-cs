class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # if st=='':
        #     return 0
        # l=[]
        # for i in range(0,len(st)):
        #      for j in range(i+1,len(st)+1):
        #           l.append(st[i:j])
        # #print(l)
        # length=-1
        # d=dict()
        # for i in l:
        #     # for j in i:
        #     #      if i.count(j)>1:
        #     #          length=1
        #     #          break
        #     # if length!=1:
        #     if len(set(i))==len(i):
        #             d[i]=len(i)
        # #print(d) 
        # h=max(d.values())
        # return h
        #*************************************************************************

        # i,j=0,0
        # maxi=0#-float('inf')
        # d=dict()
        # while j<len(s):
        #     d[s[j]]=1+d.get(s[j],0)
        #     if len(d)==(j-i+1):
        #         maxi=max(maxi,(j-i+1))
        #         j+=1
        #     elif len(d)<(j-i+1):
        #         while len(d)<(j-i+1):
        #             d[s[i]]-=1
        #             if d[s[i]]==0:
        #                 del d[s[i]]
        #             i+=1
                    
        #         j+=1
        # return maxi

        se=set()
        i,j=0,0
        maxi=0

        while j<len(s):
            if s[j] not in se:
                se.add(s[j])
                maxi=max(maxi,(j-i+1))
                j+=1
            else:
                se.remove(s[i])
                i+=1
        return maxi
        

            
        



        
