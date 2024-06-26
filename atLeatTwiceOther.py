def dominantIndex(nums) -> int:
    
    dicOFNum = {}
    for i in range(len(nums)):
        dicOFNum[nums[i]] = i
    
    nums.sort()
    if nums[len(nums) - 1] >= 2 * nums[len(nums) - 2]:

        return dicOFNum[nums[len(nums) - 1]]

    return -1

ans = dominantIndex([1,2,3,4])
print(ans)