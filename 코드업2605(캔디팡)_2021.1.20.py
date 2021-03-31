shot=0
cnt=0

def search(i,j):
  global shot
  global cnt
  if cnt==2:
    shot+=1

  if paan[i][j]==paan[i-1][j]:
    cnt+=1
    search(i-1,j)
  elif paan[i][j]==paan[i][j-1]:
    cnt+=1
    search(i,j-1)
  elif paan[i][j]==paan[i+1][j]:
    cnt+=1
    search(i+1,j)
  elif paan[i][j]==paan[i][j+1]:
    cnt+=1
    search(i,j+1)
  else:cnt=0
