n=int(input())
for i in range(n):
    totscore,passedcases=map(int,input().split())
    each=totscore//10
    print(passedcases*each)
    
