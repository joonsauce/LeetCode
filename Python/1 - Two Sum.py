def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            newval = target - nums[i]
            if newval in nums and nums.index(newval) != i:
                return [i, nums.index(newval)]