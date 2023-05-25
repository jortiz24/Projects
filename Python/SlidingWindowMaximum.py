    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:

        if k == 1:
            return nums

     
        solution = []
        window = []

        for x , y in enumerate(nums):

            while window and nums[window[-1]] < y:
                window.pop()
            window += [x]

            if window[0] == x - k:
                del window[0]
            if x >= k-1:
                solution += [nums[window[0]]]
        return solution
      


        return solution
