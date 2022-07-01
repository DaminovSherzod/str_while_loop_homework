def main(s):
    """
    A variable of type str is given. Find how many uppercase letters there are and return.
    Args:
        s: str
    Returns:
        int: return answer
    """
    a=0
    x=0
    while a<len(s):
        if s[a].isupper():
            x+=1
        a+=1    
    return x
print(main('CodeschoolUz'))    