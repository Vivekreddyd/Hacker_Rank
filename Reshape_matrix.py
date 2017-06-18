# class Solution(object):
#     def matrixReshape(self, nums, r, c):
"""
:type nums: List[List[int]]
:type r: int
:type c: int
:rtype: List[List[int]]
"""
nums=[[1,2],[3,4]]
r=4
c=1
array_length=sum(len(num) for num in nums)
# print array_length
if (array_length==r*c):
    list_old=[]
    for num in nums:
        for num1 in num:
            list_old.append(num1)
            #print(len(list_old))
    list_new=[[]for i in range(r)]
    print list_new
    new_c=0
    for i in range(0,r):
        for j in range(0,c):
            #print(list_old[(i*(i+1))+j])
            list_new[i].append(list_old[(c*i)+j])
        new_c = new_c + c
            #print list_new
        # else:
        #     return nums
        # return list_new