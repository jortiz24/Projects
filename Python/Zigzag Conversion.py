##Leetcode Solution for problem #6

class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """

        if numRows == 1 or len(s) == 1: ## base case
            return s
        
        solution = ""

        for x in range(numRows):
            pos = x
            
            counter = 0 # used to alternate when youre closer to the top row or bottom
            while (pos < len(s)) == True:
                solution += s[pos]
                print(solution)

                if x == 0 or x == numRows-1:
                    ## Slices string S when at the first or last row of the zigzag
                    pos += (numRows-1)*2
                elif counter%2 == 0:
                    pos += abs((numRows-1)*2 - 2*x)
                else: ## these two condtionals slice depending whether youre closer to the top row or the bottom row (row 0 or row numRows-1)
                    pos += abs((numRows-1)*2 - 2*x - (numRows-1)*2)
                print(pos)
                counter += 1
        
        return solution

