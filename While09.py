def main(s):
    """
    A string of numbers is given. Find the sum of all the numbers and return.
    Args:
        s: str
    Returns:
        int: return answer
    """
    a = 1
    while a<len(s):
        s[0]+=s[a]
        a+=1
    return s[0]
print(main([9,8,7,6,5,4]))    