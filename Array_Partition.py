# class Solution(object):
#     def arrayPairSum(self, nums):
nums=[1,4,3,2]
"""
:type nums: List[int]
:rtype: int
"""
nums.sort()
print nums[::2]
sum=0
for i in range(0,len(nums)):
    if (i%2==0):
        sum=sum+nums[i]
# print (sum(nums[i] for i%2==1 in len(nums))
#         return(sum)