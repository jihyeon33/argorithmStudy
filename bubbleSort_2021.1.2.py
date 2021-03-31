#입력받기
n=int(input())
A=[i for i in range(n)]
for i in range(n):
    A[i]=input().split()
    A[i][0]=int(A[i][0])

#입력받은 리스트 출력해보기
for i in range(n):
    print(A[i])

#버블소트 알고리즘을 사용하여 A[i][0]기준으로 정렬하기
for i in range(n-1,0,-1):
    for j in range(i):
        if A[j][0]>A[j+1][0]:
            A[j],A[j+1]=A[j+1],A[j]
#결과리스트 출력하기
for i in range(n):
    print(A[i][0],A[i][1])
