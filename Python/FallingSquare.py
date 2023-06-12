##

class Solution(object):
    def fallingSquares(self, positions):

        if len(positions) == 1:
            return positions[0][1]
        
        
        xval = [0]*10000000
        ##print(([ xval[x] for x in range(4) if x in xval]))
        output = []

        for x in positions:
            ##x[0] = left edge position, x[1] = side length
            if output:
                
                if [xval[y] for y in range(x[0],x[0]+x[1]) if xval[y] != 0]:
                
                    
                    heights = max(xval[x[0]:x[0]+x[1]]) + x[1]
                    
                else:
                    heights = x[1]
                
                for y in range(x[0],x[0] + x[1]):
                   
                    xval[y] = heights
                    
                
              
                output.append(max(xval))

            
            else:
                print(xval[:25])
                output.append(x[1])
                for y in range(x[0],x[0]+x[1]):
                    xval[y] = x[1]
            
               

        
        return output
      

####################################################################
class Solution(object):
    def fallingSquares(self, positions):

        if len(positions) == 1:
            return positions[0][1]
        
        xval = {}

        
        ##print(([ xval[x] for x in range(4) if x in xval]))

        output = []

        for x in positions:
            ##x[0] = left edge position, x[1] = side length
            if output:
                if [xval[y] for y in range(x[0],x[0]+x[1]) if y in xval]:
                
                
                    heights = max([xval[y] for y in range(x[0],x[0]+x[1]) if y in xval]) + x[1]
                else:
                    heights = x[1]
                
                for y in range(x[0],x[0] + x[1]):
                   
                    xval[y] = heights
                    
                
              
                output.append(max(xval.values()))

            
            else:
                output.append(x[1])
                for y in range(x[0],x[0]+x[1]):
                    xval[y] = x[1]
            
               

        
        return output
                    
