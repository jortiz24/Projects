##Leetcode 685
class Solution:
    def findRedundantDirectedConnection(self, edges: List[List[int]]) -> List[int]:

        parents = {}
        dupe = 0
        for x in edges:

            if x[1] in parents:
                parents[x[1]].append(x[0])
                dupe = x[1]

            
            else:
                parents[x[1]] = [x[0]]
             

        

        """for x in range(len(values)):
            if x == len(values) - 1:
                
                return [(parents[values[x]])[-1],values[x]]
            
            if len(parents[values[x]]) == 2:
                return [(parents[values[x]])[-1],values[x]]
        """
        if dupe != 0:
            
            left = parents[dupe][0]
            right = parents[dupe][1]
            lpath = [left]
            rpath = [right]
            while left in parents or right in parents:
                if left in parents:
                    print([left,right],parents)

                    left = parents[left][0]
                    
                    if left in rpath:
                        print(1)
                        return [rpath[0],dupe]
                    if left in lpath:
                        print(2)
                        return [lpath[0],dupe]
                    lpath.append(left)
                
                if right in parents:
                    right = parents[right][0]
                    
                    if right in rpath or right in lpath:
                        print(3)
                        return [rpath[0],dupe]
                    rpath.append(right)
                
        else:
            values = sorted([x[0] for x in list(parents.values())])
            sets = list({s for s in values})
            print(values,sets)

            if values == sets:
                return edges[-1]

                
            key = edges[0][1]
            
            next = parents[key][0]
            passed = []
            print(key,next)
            while True:
                
                key = next
                passed.append(key)
                next = parents[key][0]
                if next in passed:
                    key = next
                    next = parents[key][0]
                    return [next, key]
  
                
            
                print(key,next)
                
            
        return edges[-1]
