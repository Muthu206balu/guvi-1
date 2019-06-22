z1=input()
z2=[]
for k in z1:
  if(k.isnumeric()):
    z2.append(k)
print(*z2,sep='')
