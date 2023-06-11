
class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:


        output = []
        compare = []

        for x in range(len(s)-9):
            if s[x:x+10] not in compare:
                compare.append(s[x:x+10])
            else:
                if s[x:x+10] not in output:
                    output.append(s[x:x+10])

        
        


        return output
