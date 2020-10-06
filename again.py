n=int(input())
data2={}
for _ in range(n):
    temp=input()
    if temp not in data2.keys():
        data2[temp]=1
    else:
        data2[temp]+=1
print(data2)
