#### import the simple module from the paraview
from paraview.simple import *

def getData(fName):
	data = XMLImageDataReader(FileName=fName)
	return data
	
def setCamera():
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
	
def addContour(data):
	contour = Contour(Input=data)
	contour.ContourBy = ['POINTS', 'Scalars_']
	contour.Isosurfaces = [421.5, -1144.0, -796.1, -448.2, -100.3, 247.5, 595.4, 943.3, 1291.2, 1639.1, 1987.0]	

	return contour
	
### Main ###

# Read in Data
fName = 'D:\\CRDDS\\Paraview_Tutorial\\CAT_Torso.vti'
data = getData(fName)

# Set up the camera view
renderView = setCamera()

# Add a contour filter to the data
contour = addContour(data)

# Add transfer function
normalsLUT = GetColorTransferFunction('Normals')

# show data in view
contourDisplay = Show(contour, renderView)
# set scalar coloring

ColorBy(contourDisplay, ('POINTS', 'Normals', 'Y'))



#### uncomment the following to render all views
# RenderAllViews()
# alternatively, if you want to write images, you can use SaveScreenshot(...).