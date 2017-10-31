#### import the simple module from the paraview
from paraview.simple import *

# create a new 'XML Image Data Reader'
cAT_Torsovti = XMLImageDataReader(FileName=['D:\\CRDDS\\Paraview_Tutorial\\CAT_Torso.vti'])
cAT_Torsovti.PointArrayStatus = ['Scalars_']

# get active view
renderView1 = GetActiveViewOrCreate('RenderView')

# show data in view
cAT_TorsovtiDisplay = Show(cAT_Torsovti, renderView1)

# create a new 'Contour'
contour1 = Contour(Input=cAT_Torsovti)
contour1.ContourBy = ['POINTS', 'Scalars_']

# show data in view
contour1Display = Show(contour1, renderView1)

# Properties modified on contour1
contour1.Isosurfaces = [421.5, -1144.0, -796.1, -448.2, -100.3, 247.5, 595.4, 943.3, 1291.2, 1639.1, 1987.0]

# get color transfer function/color map for 'Normals'
normalsLUT = GetColorTransferFunction('Normals')

# set scalar coloring
ColorBy(contour1Display, ('POINTS', 'Normals', 'Y'))

# reset view to fit data
renderView1.ResetCamera()

# current camera placement for renderView1
renderView1.CameraPosition = [178.12559509277344, -1053.147120033127, 214.6875]
renderView1.CameraFocalPoint = [178.12559509277344, 119.67813873291016, 214.6875]
renderView1.CameraViewUp = [0.0, 0.0, 1.0]
renderView1.CameraParallelScale = 303.54951354594255

#### uncomment the following to render all views
# RenderAllViews()
# alternatively, if you want to write images, you can use SaveScreenshot(...).