#### import the simple module from the paraview
from paraview.simple import *

# create a new 'Sphere'
sphere1 = Sphere()

# get active view
renderView1 = GetActiveViewOrCreate('RenderView')

# show data in view
sphere1Display = Show(sphere1, renderView1)

# Properties modified on sphere1
sphere1.Radius = 1.0

# Properties modified on sphere1
sphere1.ThetaResolution = 64

# Properties modified on sphere1
sphere1.PhiResolution = 64

# get color transfer function/color map for 'Normals'
normalsLUT = GetColorTransferFunction('Normals')

# set scalar coloring
ColorBy(sphere1Display, ('POINTS', 'Normals', 'Y'))

# Apply a preset using its name. Note this may not work as expected when presets have duplicate names.
normalsLUT.ApplyPreset('jet', True)

# Properties modified on normalsLUT
normalsLUT.RGBPoints = [-0.9987165331840515, 0.0, 0.0, 0.5625, -0.7767797477468252, 0.0, 0.0, 1.0, -0.2694946680309176, 0.0, 1.0, 1.0, -0.015852627531230512, 1.0, 1.0, 1.0, 0.2377894129684568, 1.0, 1.0, 0.0, 0.7450744926843644, 1.0, 0.0, 0.0, 0.9987165331840515, 0.5, 0.0, 0.0]

#### uncomment the following to render all views
# RenderAllViews()
# alternatively, if you want to write images, you can use SaveScreenshot(...).
