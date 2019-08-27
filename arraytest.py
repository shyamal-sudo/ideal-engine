from array import *

vals=array('i',[5,6,2,3,4,7,34])
new=array(vals.typecode,(a**2 for a in vals))
for i in new:
    print(i)


v=int(input("enter a val:"))
c=0
for n in new:
    if n==v:
        print(c)
        break

    c+=1

