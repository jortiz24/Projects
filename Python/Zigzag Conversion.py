class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """

        if numRows == 1 or len(s) == 1:
            return s
        
        solution = ""

        for x in range(numRows):
            pos = x
            
            counter = 0
            while (pos < len(s)) == True:
                solution += s[pos]
                print(solution)

                if x == 0 or x == numRows-1:
                    pos += (numRows-1)*2
                elif counter%2 == 0:
                    pos += abs((numRows-1)*2 - 2*x)
                else:
                    pos += abs((numRows-1)*2 - 2*x - (numRows-1)*2)
                print(pos)
                counter += 1
        
        return solution


