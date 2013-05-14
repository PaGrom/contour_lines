from pylab import *
xlist = linspace(-10.0, 10.0, 200)
ylist = linspace(-5.0, 15.0, 200)
X, Y = meshgrid(xlist, ylist)
# print X
# print Y
Z = 0.5*(Y - X**2)**2 + (1 - X**2)
# print Z
figure()

CP1 = contour(X, Y, Z) # replace this
clabel(CP1, inline=True, fontsize=10) # replace this
title('Contour Plot')

xlabel('x (cm)')
ylabel('y (cm)')

savefig("f2.png")
