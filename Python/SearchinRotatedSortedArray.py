##Leetcode # 81

class Solution:
    def search(self, nums: List[int], target: int) -> int:


        output = 0

        if nums[0] == target and len(nums) == 1:
            return 0

        if target >= nums[0]:
            while output < len(nums):
                if nums[output] == target:
                    return output
                if nums[output] > target or output == len(nums)-1:
                    return - 1
                output += 1
                
         ## if target is greater than starting point, search to the right in above loop, else target is below snd search to the left in below loop
        else:
            output = -1
            while output % len(nums) >= 1:
                
                if nums[output] == target:
                    return output % len(nums)
                if nums[output] < target or output == -len(nums):
                    return - 1
                output -= 1
                    
        
        return -1 
