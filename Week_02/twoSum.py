"""
两数之和
"""
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashMap = {}
        for i,value in enumerate(nums):
            j = hashMap.get(target - value)
            if( j is not None ):
                return [i, j]
            else:
                hashMap[value] = i
