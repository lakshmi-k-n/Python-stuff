def minn(s):
    l = s[0] 
    for x in s:
        if x < l:
            l = x
    return l

print minn(input())
