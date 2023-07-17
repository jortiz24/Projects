## Leetcode problem #4

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:



        x = 0
        y = 0
        values = []

        
        
        half = (len(nums1) + len(nums2))//2


        while len(values) < (len(nums1)+len(nums2))//2 + 1:

            if x == len(nums1):
                values = [nums2[y]] + values
                y += 1
           
            elif y == len(nums2):
                values = [nums1[x]] + values
                x += 1
               

            elif nums1[x] < nums2[y]:
                values = [nums1[x]] + values
                x += 1
            else:
                values = [nums2[y]] + values
                y += 1
            
          
        print(values)

        if (len(nums1) + len(nums2)) % 2 == 0:
            return sum(values[0:2])/2
        else:
            return values[0]
