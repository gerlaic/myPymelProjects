from pymel.core import *

#input parameter
camera_distance = 100
#set time
t1 = 1
t2 = 120

#find selects
sel = ls(selection = True)

if not (len(sel)>0):
	print "\n No obeject selected. \n"
else:
	if (len(sel)>1):
		print 'WARNING: more than 1 object selected, Using the first object'

	#select First Object
	s = sel[0]

	#grab selected object XYZ
	sO_x=cmds.getAttr("%s.translateX" %s)
	sO_y=cmds.getAttr("%s.translateY" %s)
	sO_z=cmds.getAttr("%s.translateZ" %s)

	#Camera setting 
	renderCamName = 'turntable_cam'

	#find if we have render cam
	renderCam = ls(renderCamName)

	#Check and create a rendercam
	if not len(renderCam) >0:
	    print 'WARNING: no render cam detected'
	    print 'yolo'
	    #create camera
	    renderCam = camera()
	    #print renderCam
	    renderCam[0].rename('turntable_cam')
	    print 'render cam created'

	tCam = renderCam[0]
	
	#set tCam XYZ
	tCam.tx.set(sO_x)
	tCam.ty.set(sO_y)
	print sO_z
	tCam.tz.set(sO_z+camera_distance)

	#set pivot
	xform(tCam, pivots=(sO_x,sO_y,sO_z),ws=1)

	#set key frame
	setKeyframe(at='rotateY',t=1, v=0)
	setKeyframe(at='rotateY',t=120,v=360)

	#set tangent
	keyTangent(itt="linear",ott="linear")

	#look through the camera
	mel.eval('lookThroughModelPanelClipped turntable_cam modelPanel4 0.001 1000');

	#let's playblast
	#parameters
	s_fullname = sceneName() 
	s_path = s_fullname.parent
	pb_filename = s_fullname.name.split('.')[0]+'_playblast'
	pb_path = s_path + "/" +pb_filename
	format = "qt"
	comp = "H.264"
	qual = 100

	#set w&h
	w=640
	h=360

	pb_actual_path = playblast(	filename = pb_path,
								format = format,
								forceOverwrite = True,
								offScreen = False,
								sequenceTime = 0,
								clearCache = 1,
								viewer = True,
								showOrnaments = False,
								framePadding = 0,
								compression = comp,
								quality = qual,
								percent = 100,
								width = w,
								height = h,
								useTraxSounds = True,
								startTime = t1,
								endTime = t2	)

	print 'Video has been outputed to: ' + pb_actual_path
								
from pymel.core import *

#input parameter
camera_distance = 100
#set time
t1 = 1
t2 = 120

#find selects
sel = ls(selection = True)

if not (len(sel)>0):
	print "\n No obeject selected. \n"
else:
	if (len(sel)>1):
		print 'WARNING: more than 1 object selected, Using the first object'

	#select First Object
	s = sel[0]

	#grab selected object XYZ
	sO_x=cmds.getAttr("%s.translateX" %s)
	sO_y=cmds.getAttr("%s.translateY" %s)
	sO_z=cmds.getAttr("%s.translateZ" %s)

	#Camera setting 
	renderCamName = 'turntable_cam'

	#find if we have render cam
	renderCam = ls(renderCamName)

	#Check and create a rendercam
	if not len(renderCam) >0:
	    print 'WARNING: no render cam detected'
	    print 'yolo'
	    #create camera
	    renderCam = camera()
	    #print renderCam
	    renderCam[0].rename('turntable_cam')
	    print 'render cam created'

	tCam = renderCam[0]
	
	#set tCam XYZ
	tCam.tx.set(sO_x)
	tCam.ty.set(sO_y)
	print sO_z
	tCam.tz.set(sO_z+camera_distance)

	#set pivot
	xform(tCam, pivots=(sO_x,sO_y,sO_z),ws=1)

	#set key frame
	setKeyframe(at='rotateY',t=1, v=0)
	setKeyframe(at='rotateY',t=120,v=360)

	#set tangent
	keyTangent(itt="linear",ott="linear")

	#look through the camera
	mel.eval('lookThroughModelPanelClipped turntable_cam modelPanel4 0.001 1000');

	#let's playblast
	#parameters
	s_fullname = sceneName() 
	s_path = s_fullname.parent
	pb_filename = s_fullname.name.split('.')[0]+'_playblast'
	pb_path = s_path + "/" +pb_filename
	format = "qt"
	comp = "H.264"
	qual = 100

	#set w&h
	w=640
	h=360

	pb_actual_path = playblast(	filename = pb_path,
								format = format,
								forceOverwrite = True,
								offScreen = False,
								sequenceTime = 0,
								clearCache = 1,
								viewer = True,
								showOrnaments = False,
								framePadding = 0,
								compression = comp,
								quality = qual,
								percent = 100,
								width = w,
								height = h,
								useTraxSounds = True,
								startTime = t1,
								endTime = t2	)

	print 'Video has been outputed to: ' + pb_actual_path
								
