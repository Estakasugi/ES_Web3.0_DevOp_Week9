def dominantIndex(nums) -> int:
    
        first_max=float('-inf')
        second_max=float('-inf')

        for i in nums:
            if i>first_max:
                second_max=first_max
                first_max=i
            elif i>second_max:
                second_max=i
        
        
        if first_max>=second_max*2:
            return nums.index(first_max)
        else:
            return -1

ans = dominantIndex([1,2,3,4])
print(ans)