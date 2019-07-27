import sys,string,math
str1,str2=input().split()
mt1=len(str1)
mt2=len(str2)
if mt2>mt1:
   i=0
   while i<mt1 and str1[i]==str2[i]:
     i+=1
   print(mt2-i)    
elif mt2==mt1:
   i=0
   while i<mt2 and str1[i]==str2[i]:
     i+=1
   print(mt2-i)
else:
   i=0
   while i<mt2 and str1[i]==str2[i]:
      i+=1
   str31=str1[i:]
   str32=ts2[i:]
   Lt=list(str31)
   kt=0
   for ct in str32:
      if ct in Lt:
         kt+=1
         Lt.remove(ct)
   print(mt1-i-kt)      
