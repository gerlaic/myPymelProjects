#import pymel.core as c
from pymel.core import *

print (sceneName())
print (sceneName().name)
path =  (sceneName().parent.parent.parent)

if 'Users' in  path:
    print 'Oh yes'
else:
    print 'Oh No'
