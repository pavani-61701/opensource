n,m=map(int,input().split())
l=list(map(int,input().split()))
divisibleSum=0
notDivisibleSum=0
for i in l:
    if(i%m==0):
        divisibleSum+=i
    else:
        notDivisibleSum+=i
print(divisibleSum-notDivisibleSum)
