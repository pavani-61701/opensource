mango,truck,bridge=map(int,input().split())
msum=mango
count=0
while(truck+msum<=bridge):
    count+=1
    msum+=mango
print(count)
