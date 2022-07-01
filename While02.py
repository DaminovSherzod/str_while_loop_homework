def main(s):
    """
    A variable of type str is given. Find how many letters it contains and return.
    Args:
        s: str
    Returns:
        int: return answer
    """
    a = 0
    x = 0
    while a<len(s):
        if s[a].isalpha():
            x+=1
        a+=1    
    return x
print(main('Python 2022'))    