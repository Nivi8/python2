e=input()
s=0
for i in range(len(e)):
  if(e[i].isdigit() or e[i].isalpha() or e[i]==(" ")):
    continue
  else:
    s+=1
print(s)
