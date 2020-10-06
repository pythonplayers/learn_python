def opn(data,i,lim):
    values=[]
    print(values)
    for j in range(i,lim-1):
        values.append(data[i][j])
    print(values)
    for j in range(i,lim-1):
        values.append(data[j][lim-1])
    print(values)
    for j in range(lim-1,i,-1):
        values.append(data[lim-1][j])
    print(values)
    for j in range(lim-1,i,-1):
        values.append(data[j][i])
    print(values)
    return  values

m,n=map(int,input().split())
data=[]
for _ in range(m):
    data.append(list(map(int,input().split())))
rotation=map(int,input().split())
opened=[]
lim=m
for i in range(m):
    val=opn(data,i,lim)
    opened.append(val)
    lim-=1
print(data)
print(*opened)
