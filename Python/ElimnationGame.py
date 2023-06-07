##Leetcode 390

class Solution:
    def lastRemaining(self, n: int) -> int:


        output = [x for x in range(1,n+1)]

        x = 0
        while len(output) > 1:


            if x % 2 == 0:
                output = output[1::2]
                output.reverse()

            x = x + 1
        
        ## uses too much memory?
        return output[0]
