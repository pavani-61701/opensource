n=int(input())
l=list(map(int,input().split()))
m=list()
for i in l:
    if i not in m:
        m.append(i)
for i in m:
    print(i,end=" ")
