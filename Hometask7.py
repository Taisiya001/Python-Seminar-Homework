s=list(map(int,input().split()))[1:]
ma=max(s)
mi=min(s)
n=list(map((lambda x: mi if (x==ma) else x),s))
for a in n:
    print(a,end=' ')
