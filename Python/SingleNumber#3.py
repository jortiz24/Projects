##Given an integer array nums, in which exactly two elements appear only once and all the other elements appear exactly twice. Find the two elements that appear only once. You can return the answer in any order.
##You must write an algorithm that runs in linear runtime complexity and uses only constant extra space.

class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:

        solution = []

        dictionary = {}

        for x in nums:
            if x not in dictionary:
                dictionary[x] = 1
            else:
                dictionary[x] += 1

        
        for x in dictionary:
            if dictionary[x] == 1:
                solution += [x]
        return solution
