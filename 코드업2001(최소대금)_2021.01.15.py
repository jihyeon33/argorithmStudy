p=[0 for i in range(3)]
j=[0 for i in range(2)]
for i in range(3):
    p[i]=int(input())
for i in range(2):
    j[i]=int(input())

mp=3000
mj=3000

for i in range(3):
    if p[i]<=mp:
        mp=p[i]

for i in range(2):
    if j[i]<=mj:
        mj=j[i]
mini=(mp+mj)*1.1
print("%.1f"%mini)
