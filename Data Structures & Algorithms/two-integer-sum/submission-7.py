class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        visto = {}

        for i in range(len(nums)):
            comp = target - nums[i]

            if comp in visto:
                return [visto[comp],i]
            visto[nums[i]] = i