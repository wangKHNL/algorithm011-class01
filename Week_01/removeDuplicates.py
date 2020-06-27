'''
删除排序数组中的重复项
'''
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            if i > len(nums)-2:
                continue
            else:
                j = i+1
                while( j< len(nums)):
                    if ( nums[i] == nums[j] ):
                        nums.pop(j)
                    else:
                        break
        return nums.__len__()