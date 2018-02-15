def unique(s):
        print s
        uni=[]
        for a in s:
                if a not in uni:
                        uni.append(a)
        return uni

def dup(s):
        dupp=[]
        for a in unique(s):
                if s.count(a)>1:
                        dupp.append(a)
        print dupp

