b=int(input())
if(b<=1000)
   for i in range(2,b):
       if(b%i==0):
          print("no")
          break
    else:
        print("yes")
else:
    print("no")
