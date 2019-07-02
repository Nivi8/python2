m,v=map(int,input().split())
for r in range(m+1,v,1):
  if(r>1):
      for u in range(2,r):
          if(r%u==0):
               break
       else:
           print(r,end=" ")
