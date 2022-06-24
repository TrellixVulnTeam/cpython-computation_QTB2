def check_number(N):
    
    digit_limit  = len(N)
    
    if (digit_limit < 10):
        return "NO"
    elif (digit_limit > 10):
        return "NO"
    else:
        return "YES"
    
print(check_number("65487000000"))