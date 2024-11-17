n=int(input())
for i in range(n):
    totmarks, casesPassed=map(int,input().split())
    scoreForEach=totmarks/10
    pointsScored=casesPassed*scoreForEach
    print(int(pointsScored))
