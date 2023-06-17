class Solution:
    def taskSchedulerII(self, tasks: List[int], space: int) -> int:


        output = 0
        

        complete = {}

        for x in tasks:

            if x not in complete:
                
                output += 1

                complete = { (key):(value-1 if value-1 >= 0 else 0) for key, value in complete.items()}
                
                complete[x] = space
            else:
                if complete[x] > 0:
                    output += complete[x] + 1

                    days = complete[x]
                    complete = { (key):(value-1-days if value-1-days >= 0 else 0) for key, value in complete.items()}
                    complete[x] = space
                else:
                    output += 1
                    complete = { (key):(value-1 if value-1 >= 0 else 0) for key, value in complete.items()}
                    complete[x] = space
                    
        

        return output

