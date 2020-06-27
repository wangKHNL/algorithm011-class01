'''
旋转数组
'''
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        if( len(nums) <= 1 or k == 0 ):
            pass
        else:
            nums[:-k], nums[-k:] = nums[-k:], nums[0:-k]
        return nums