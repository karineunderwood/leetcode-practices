class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        track = {}
        
        for n in nums:
            if n in track:
                track[n] += 1
            else:
                track[n] = 1
        
        for index, value in track.items():
            if value > (len(nums) // 2):
                return index