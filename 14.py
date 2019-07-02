val1,val2=map(int,input().split())
for k in range(val1+1,val2,1):
   if(k%2!=0):
      print(k,end=' ')
