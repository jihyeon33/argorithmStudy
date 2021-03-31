n,m,k= map(int,input().split())
arr=list(map(int,input().split()))
arr.sort(reverse=True)

cnt=0
while cnt<=m:
  for i in range(k):
    if cnt>=m: break
    sum +=n[0]
    cnt+=1
  if cnt>=m: break
  sum +=n[1]
  cnt+=1

print(sum)
