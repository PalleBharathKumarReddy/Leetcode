class Solution:
    def concatWithReverse(self, nums: list[int]) -> list[int]:
        temp=nums
        for i in range(len(temp)-1,-1,-1):
            nums.append(temp[i])
        return nums