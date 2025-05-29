def next_palindrome(digit_list):
    n = len(digit_list)
    mid = n // 2
    i = mid - 1
    j = mid + (n % 2) 
    
    while i >= 0 and digit_list[i] == digit_list[j]:
        i -= 1
        j += 1
    
    if i < 0 or digit_list[i] < digit_list[j]:
        carry = 1
        i = mid - 1
        
        if n % 2 == 1:
            digit_list[mid] += carry
            carry = digit_list[mid] // 10
            digit_list[mid] %= 10
            j = mid + 1
        else:
            j = mid
        
        while i >= 0:
            digit_list[i] += carry
            carry = digit_list[i] // 10
            digit_list[i] %= 10
            digit_list[j] = digit_list[i]
            i -= 1
            j += 1
        
        if carry:
            return [1] + digit_list
            
    else:
        i = mid - 1
        j = mid + (n % 2)
        while i >= 0:
            digit_list[j] = digit_list[i]
            i -= 1
            j += 1
            
    return digit_list