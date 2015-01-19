from pymel.core import *

sel = ls(selection = True)
#children = sel[0].getChildren()

for each in children:
    print each
    
for each in sel[0].edges:
    select(sel[0].e[1:50])
    #print each
