a,s=map(int,input().split())
for f in range(a+1,s):
  ch=f
  fnd=0
  while(f>0):
   v=f%10
   fnd=fnd+(v**3)
   f=f//10
   if(fnd==ch):
      print(fnd,end=" ")
