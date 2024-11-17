n=int(input())
l=list(map(int,input().split()))
m=list()
lweight=0
rweight=0
for i in range(len(l)):
    if(i==0):
        lweight=0
        rweight=sum(l[1:])
        m.append(abs(lweight-rweight))
    elif(i==len(l)-1):
        lweight=sum(l[:len(l)-1])
        rweight=0
        m.append(abs(lweight-rweight))
    else:
        lweight=sum(l[:i])
        rweight=sum(l[i+1: ])
        m.append(abs(lweight-rweight))
for i in m:
    print(i,end=" ")
