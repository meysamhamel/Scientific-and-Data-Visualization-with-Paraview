#### import the simple module from the paraview
from paraview.simple import *
#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

# create a new 'Sphere'
sphere1 = Sphere()

# get active view
renderView1 = GetActiveViewOrCreate('RenderView')
# uncomment following to set a specific view size
# renderView1.ViewSize = [1627, 887]

# show data in view
sphere1Display = Show(sphere1, renderView1)
# trace defaults for the display properties.
sphere1Display.Representation = 'Surface'
sphere1Display.ColorArrayName = [None, '']
sphere1Display.OSPRayScaleArray = 'Normals'
sphere1Display.OSPRayScaleFunction = 'PiecewiseFunction'
sphere1Display.SelectOrientationVectors = 'None'
sphere1Display.ScaleFactor = 0.1
sphere1Display.SelectScaleArray = 'None'
sphere1Display.GlyphType = 'Arrow'
sphere1Display.GlyphTableIndexArray = 'None'
sphere1Display.DataAxesGrid = 'GridAxesRepresentation'
sphere1Display.PolarAxes = 'PolarAxesRepresentation'
sphere1Display.GaussianRadius = 0.05
sphere1Display.SetScaleArray = [None, '']
sphere1Display.ScaleTransferFunction = 'PiecewiseFunction'
sphere1Display.OpacityArray = [None, '']
sphere1Display.OpacityTransferFunction = 'PiecewiseFunction'
sphere1Display.InputVectors = ['POINTS', 'Normals']

# reset view to fit data
renderView1.ResetCamera()

# update the view to ensure updated data information
renderView1.Update()

# Properties modified on sphere1
sphere1.Radius = 1.0

# update the view to ensure updated data information
renderView1.Update()

# Properties modified on sphere1
sphere1.ThetaResolution = 32

# update the view to ensure updated data information
renderView1.Update()

# Properties modified on sphere1
sphere1.PhiResolution = 32

# update the view to ensure updated data information
renderView1.Update()

# set scalar coloring
ColorBy(sphere1Display, ('POINTS', 'Normals', 'Magnitude'))

# rescale color and/or opacity maps used to include current data range
sphere1Display.RescaleTransferFunctionToDataRange(True, False)

# show color bar/color legend
sphere1Display.SetScalarBarVisibility(renderView1, True)

# get color transfer function/color map for 'Normals'
normalsLUT = GetColorTransferFunction('Normals')

# set scalar coloring
ColorBy(sphere1Display, ('POINTS', 'Normals', 'Z'))

# rescale color and/or opacity maps used to exactly fit the current data range
sphere1Display.RescaleTransferFunctionToDataRange(False, False)

# Update a scalar bar component title.
UpdateScalarBarsComponentTitle(normalsLUT, sphere1Display)

# set scalar coloring
ColorBy(sphere1Display, ('POINTS', 'Normals', 'Y'))

# rescale color and/or opacity maps used to exactly fit the current data range
sphere1Display.RescaleTransferFunctionToDataRange(False, False)

# Update a scalar bar component title.
UpdateScalarBarsComponentTitle(normalsLUT, sphere1Display)

#### saving camera placements for all active views

# current camera placement for renderView1
renderView1.CameraPosition = [0.0, 0.0, 3.2903743041222895]
renderView1.CameraParallelScale = 0.8516115354228021

#### uncomment the following to render all views
# RenderAllViews()
# alternatively, if you want to write images, you can use SaveScreenshot(...).