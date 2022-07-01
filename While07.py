def main(s):
    """
    A string of numbers is given. Find how many even numbers there are and return.
    Args:
        s: str
    Returns:
        int: return answer
    """
    a=0
    x=0
    while a<len(s):
        if s[a].isdigit() and s[a]!='1' and s[a]!='3' and s[a]!='5' and s[a]!='7' and s[a]!='9':
            x+=1
        a+=1    
    return x
print(main('123456'))    