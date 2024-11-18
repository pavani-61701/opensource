n=int(input())
l=list(map(int,input().split()))
flag=1
for i in range(1,n):
    if l[i]<l[i-1]:
        flag=0
        break
if(flag==1):
    print("true")
else:
    print("false")
