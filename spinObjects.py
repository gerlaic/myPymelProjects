from pymel.core import *
import random as r

delete(ls("sphere*"))
delete(ls("cam_grp*"))

#create the render cam and spin it
c = camera(n="render_cam#")
move(0, 7.5, 30, c)
grp = group(empty=True, name='cam_grp')
parent(c[0], grp)


for i in range(0, 12):
    shape = polySphere(n="sphere#")
    move(0, 0, 5, shape)
    rotate(shape, 0, str(360 / 12 * i) + 'deg', 0, p=[0,0,0])
    
    t = shape[0].attr("visibility")
    t.set(0)
    

    setKeyframe(grp.rotateY, v=360 / 15 * i, itt="spline", t=i+2)
    setKeyframe(t, v=0, t=1)
    setKeyframe(t, v=1, t=i+2*r.random())
