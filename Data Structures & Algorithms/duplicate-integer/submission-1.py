class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        size = len(nums)
        thisset = set(nums)
        sizeset = len(thisset)
        if size == sizeset:
            return False
        else:
            return True
        