M=int(input())
length=len(str(M))
sum=0
temp=M
while(temp!=0)and(M<=100000):
   sum=sum+((temp%10)**length)
   temp=temp//10
if sum==M:
   print("yes")
else:
   print("no")
