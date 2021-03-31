paan=[[0 for i in range(19)]for j in range(19)]

n=int(input())
for i in range(n):
    a,b=map(int,input().split())
    paan[a][b]=1


for i in paan :
    for j in i:
        print(j,end=' ')
    print()
