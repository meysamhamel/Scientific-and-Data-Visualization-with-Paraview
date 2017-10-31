#### import the simple module from the paraview
from paraview.simple import *

def getData(fName):
	"""
	Load the desired data file
	
	Args: fName - Path and name of the data file to open
	
	Returns: data - A handle to the full, opened dataset
	"""
	data = XMLImageDataReader(FileName=fName)
	return data
	
def setCamera():
	"""
	Sets up the camera view for this scene
	
	Args: None
	
	Returns: renderView - A handle to the current active renderview
	"""
	# get active view
	renderView = GetActiveViewOrCreate('RenderView')
	# reset view to fit data
	renderView.ResetCamera()

	# current camera placement for renderView
	renderView.CameraPosition = [178.12559509277344, -1053.147120033127, 214.6875]
	renderView.CameraFocalPoint = [178.12559509277344, 119.67813873291016, 214.6875]
	renderView.CameraViewUp = [0.0, 0.0, 1.0]
	renderView.CameraParallelScale = 303.54951354594255

	return renderView
	
def addContour(inData):
	"""
	Adds a contour filter to the dataset using 10 hardcoded but even divisions
	
	Args: inData - The object layer (in this case the dataset itself) to apply the 
								 contour filter to.
	
	Returns: contour - A handle to the new contoured filtered layers data
	"""
	contour = Contour(Input=inData)
	contour.ContourBy = ['POINTS', 'Scalars_']
	contour.Isosurfaces = [421.5, -1144.0, -796.1, -448.2, -100.3, 247.5, 595.4, 943.3, 1291.2, 1639.1, 1987.0]	

	return contour


def addClip(inData, y):
	"""
	Adds a clip filter to the input data (in this case the contour layer) and clipping
	along the y-axis at a specified position
	
	Args: inData - the object layer (in this case the contour layer) to which the clipping
	               will be applied
	              
	      y - the y-axis position where the clipping will be made         
	
	Returns: clip - A handle to thdatae new clipped layers 
	"""
	
	clip = Clip(Input=inData)
	clip.ClipType = 'Plane'

	# init the 'Plane' selected for 'ClipType'
	clip.ClipType.Origin = [175.39791604876518, y, 214.6875]

	# Properties modified on clip1.ClipType
	clip.ClipType.Normal = [0.0, 1.0, 0.0]

	clip1Display = Show(clip, renderView)
	return clip
		
##################		
###### Main ######
##################
# Read in Data
fName = 'D:\\CRDDS\\Paraview_Tutorial\\CAT_Torso.vti'
data = getData(fName)

# Set up the camera view
renderView = setCamera()

# Add a contour filter to the data
contour = addContour(data)

# Add transfer function coloring the normals along the Y axis (depth in this case)
contourDisplay = Show(contour, renderView)
normalsLUT = GetColorTransferFunction('Normals')
ColorBy(contourDisplay, ('POINTS', 'Normals', 'Y'))

#Hide the contour layer so only the new clipped contour layer will be visible
Hide(contour, renderView)

#Create a loop for animating clipping along the y-axis and saving the image to disk
for y in range(0,240):
	#Create the clip along the the y axis position (0-240)
	clip = addClip(contour, y)

	# Hide the clipping plane widget 
	Hide3DWidgets(proxy=clip.ClipType)

	#Update the renderView
	renderView.Update()
	
	#Create a padding for the frame numbers and build the image file name (iName)
	fnum = str(y)
	fnum = fnum.zfill(3)
	iName = 'D:/CRDDS/Paraview_Tutorial/Images/TorsoAnim/Torso_clip'+fnum+'.png'
	
	#Save the render to disk making sure they are all the same size
	SaveScreenshot(iName, renderView, ImageResolution=[800, 473])
	
	# Delete clip so we just create a replacement layer and not 240 new layers
	Delete(clip)
	del clip
