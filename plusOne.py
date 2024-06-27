def plusOne(digits):
    digits[len(digits)-1] += 1
    
    j = len(digits)-2
    for i in range(len(digits)-1, 0, -1):
        
        if digits[i] == 10:
            digits[j] += 1
            digits[i] %= 10
        j -= 1

    if digits[0] == 10:
        digits[0] %= 10
        digits = [1] + digits

    return digits


digits = [9,9,9,9]
ans = plusOne(digits)
print(ans)