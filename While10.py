def main(s):
    """
    A string of numbers is given. Find and return the sum of all odd numbers.
    Args:
        s: str
    Returns:
        int: return answer
    """
    a = 0
    x = 0
    while a<len(s):
        if s[a]%2==1:
            x+=s[a]
        else:
            x+=0    
        a+=1       
    return x
print(main([5,8,9,7,6,5]))    