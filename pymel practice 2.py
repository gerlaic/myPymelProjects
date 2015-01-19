from pymel.core import *

spy = polySphere()
#create a sphere
print spy
#return a list

spy[0].tx.set(3)
#spy[0].tx.set(-3)
spy[0].ty.set(3)
spy[0].tz.set(3)
spy[0].t.set(-3,3,3)
spy[0].s.set(1,2,1)
spy[0].r.set(45,80,60)
#print (spy[0].t.get() [0])

s = spy[0].getShape()
s.rename('blabla')

s = spy[0].getShape().inputs()[0].radius.set(2)
