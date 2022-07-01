def main(s):
    """
    A variable of type str is given. Find and return how many consonant letters there are.
    Args:
        s: str
        consonant: other than vowels(a, e, i, o, u)
    Returns:
        int: return answer
    """
    a = 0
    x = 0
    while a<len(s):
        if s[a]!='a' and s[a]!='e' and s[a]!='i' and s[a]!='o' and s[a]!='A' and s[a]!='E' and s[a]!='I' and s[a]!='O' and s[a]!='u' and s[a]!='U' and s[a].isalpha():
            x+=1
        a+=1
    return x
print(main('COdeSchooluz'))            