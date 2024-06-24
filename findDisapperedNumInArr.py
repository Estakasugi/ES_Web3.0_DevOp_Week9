"""
448. Find All Numbers Disappeared in an Array
Given an array nums of n integers where nums[i] is in the range [1, n], return an array of all the integers in the range [1, n] that do not appear in nums.


Example 1:

Input: nums = [4,3,2,7,8,2,3,1]

Output: [5,6]
Example 2:

Input: nums = [1,1]
Output: [2]
"""

def findDisappearedNumbers(nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    ansList = []
    listDic = {}

    for i in range(1,len(nums)+1):
        listDic[i] = 0
    
    for i in range(len(nums)):
        if nums[i] in listDic:
            listDic[nums[i]] += 1
    
    for key in listDic:
        if listDic[key] == 0:
            ansList.append(key)


    return ansList

nums = [1,1]
ans = findDisappearedNumbers(nums)

print(ans)
