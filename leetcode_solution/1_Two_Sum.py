# import sys
# class Solution(object):
#     def twoSum(self, nums, target):
#         """
#         :type nums: List[int]
#         :type target: int
#         :rtype: List[int]
#         """
#         dic = dict()
#         countnum = 0
#         for index,value in enumerate(nums):
#             #print index,value
#             sub = target - value
#             print "sub:",sub
#             print "value:",value
#             if sub in dic:
#                 print "Yes!!! and sub,value,dic",sub,value,dic
#                 countnum += 1  
#                 print [dic[sub],index]
#                 print countnum
#             else:
#                 if sub == value:
#                     countnum += 1
                
#                 dic[value] = index
#                 print " NO!!!  value,dic[value],index:",value,dic[value],index,dic

#         return countnum    
# testnum = [3,2,4,3]
# testtarget = 6




class Solution(object):
    def twoSum(self,nums,target):
        dictionary = {};

        

        for index in range(len(nums)):

            if nums[index] in dictionary.keys():
                return [dictionary[nums[index]],index];
            else:
                residual = target - nums[index];
                dictionary[residual] = index;

