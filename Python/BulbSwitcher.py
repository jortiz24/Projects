#Leetcode 319

class Solution:
    def bulbSwitch(self, n: int) -> int:

        if n ==1:
            return 1

        bulbs = ["on" for x in range(n)]

        for round in range(2,n+1):
            for bulb in range(1,n):

                if (bulb + 1) % round == 0:
                    if bulbs[bulb] == "off":
                        bulbs[bulb] = "on"
                    else:
                        bulbs[bulb] = "off"
        ### Could be more efficient, instead of using on and offs use 1s and 0s and mod them then return the sum of the list at the end
                        
        total = 0
        for x in bulbs:
            if x == "on":
                total += 1
        return total
