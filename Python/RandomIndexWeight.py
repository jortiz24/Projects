#leetcode 528
class Solution:

    def __init__(self, w: List[int]):

            self.indexes = w
            
            added = sum(w)
            probabilities = [ i/added for i in w]
            self.probabilities = [sum(probabilities[:x+1]) for x in range(len(probabilities))]
            print(probabilities,self.probabilities)

    def pickIndex(self) -> int:
            pick = random.uniform(0,1)
            print(pick)
            for x in range(len(self.probabilities)):
                if pick < self.probabilities[x]:
                            return x 
                if x == len(self.probabilities) - 1:
                        return x

        
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()
