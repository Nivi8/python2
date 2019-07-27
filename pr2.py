fac,gof=input().strip().split(" ")
gof=int(gof)
wow=0
while wow<len(fac)-1 and gof:
    if(fac[wow]>fac[wow+1]):
        gof-=1
        fac=fac[:wow]+fac[wow+1:]
        if(wow!=0):
             wow-=1
    else:
        wow+=1
pae=fac[:len(fac)-gof]
print(pae)
