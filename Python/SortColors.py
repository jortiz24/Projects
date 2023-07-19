##Leetcode #75

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        I made it single pass
        """

        red = []
        white = []
        blue = []

        for x in nums:
            if x == 0:
                red = red + [x]

            if x == 1:
                white = white + [x]
            
            if x == 2:

                blue = blue + [x]
            
        print(red,white,blue)
        nums[:] = red + white + blue ###this was such a weird fix, nums doesnt work but nums[:] does so im guessing it has to do with memory management
        print(nums)
