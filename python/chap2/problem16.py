def extsort(s):
        for x in range(len(s)):
                s[x]=s[x].split('.')
        s.sort(key=lambda x: x[1])
        for x in range(len(s)):
                s[x]='.'.join(s[x])
        print s


