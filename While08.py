def main(s):
    """
    A string of numbers is given. Find how many odd numbers there are and return.
    Args:
        s: str
    Returns:
        int: return answer
    """
    a=0
    x=0
    while a<len(s):
        if s[a].isdigit() and s[a]!='2' and s[a]!='4' and s[a]!='6' and s[a]!='8' and s[a]!='0':
            x+=1
        a+=1    
    return x
print(main('123456548')) 