pp=int(input())
l=list(map(int,input().split()))
qq=[]
r=1
for i in range(pp):
  v=l[i:]
  ans=len(v)
  for j in range(ans-1):
    if v[j]>0 and v[j+1]<0:
      r=r+1
    elif v[j]<0 and v[j+1]>0:
      r=r+1
    else:
      break
  qq.append(str(r))
  r=1
print(" ".join(qq))
