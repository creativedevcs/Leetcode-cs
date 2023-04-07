class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # for i in range(len(nums)):
        #     for j in range(i+1,len(nums)):
        #         if nums[i]+nums[j]==target:
        #             return [i,j]
        # return [-1,-1]
        d=dict()
        for i in range(len(nums)):
            if target-nums[i] not in d:
                d[nums[i]]=i
            else:
                return [d[target-nums[i]],i]
        return [-1,-1]
