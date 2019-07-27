er=int(input())
tr=[]
for i in range(er):
  gr=input()
  tr.append(gr)
mv2=min(tr,key=len)
tr.remove(mv2)
for i in range(len(mv2)):
  for j in range(len(tr)):
    cv2=tr[j]
    if mv2[:i+1]==cv2[:i+1]
  else:
    break
print(result)
