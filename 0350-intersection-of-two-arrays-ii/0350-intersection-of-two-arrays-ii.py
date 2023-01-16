class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        frequency_count = {}
        output = []
        for num in nums2:
            if num not in frequency_count:
                frequency_count[num] = 1
            else:
                frequency_count[num] += 1
            
        for num in nums1:
            if num not in frequency_count:
                pass
            elif frequency_count[num] > 0:
                output.append(num)
                frequency_count[num] -= 1
        return output
            
       