#동적계획법
def fibo(n):
  for i in range(n):
    if i==0 or i==1: f[i]=1
    else: f[i]=f[i-1]+f[i-2]


n=int(input())
f=[0 for i in range(n)]
fibo(n)

print(f[n-1])


#재귀알고리즘
def fibo(n):
  if n==1: return 1
  elif n==2: return 1
  else: return fibo(n-1)+fibo(n-2)

n= int(input())
fibo(n)


#재귀+동적계획
n= int(input())
f=[0 for i in range(n+1)]
f[1]=1
f[2]=1

def fibo(n):
  if f[n] != 0: return f[n]
  if n==1 or n==2: return f[n]
  else: f[n]= fibo(n-1)+fibo(n-2)
  return f[n]

fibo(n)
  
