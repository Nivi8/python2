d=input()
t=0
for i in range(len(d)):
  if(d[i].isdigit() or d[i].isalpha() or d[i]==(" ")):
    continue
  else:
    t+=1
print(t)
