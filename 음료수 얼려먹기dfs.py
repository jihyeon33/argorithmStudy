graph=[[],[2,4],[1,3,5],[2,6],[1,5,7],[2,4,6,8],[3,5,9],[4,8],[5,7,9],[6,8]]
Bool=[0,0,0,1,0,1,0,1,0,1]
visited=[0]*10
stack=[]
result=0


def dfs(v):
  global result
  if Bool[v]==0 and visited[v]==0:
    visited[v]=1
    stack.append(v)
    while len(stack)==0:
      p=stack.pop()
      visited[p]=1
      for i in graph[p]:
        if Bool[i]==0 and visited[i]==0:
          stack.append(i)
    result+=1


for i in range(1,10):
  dfs(i)
print(result)
