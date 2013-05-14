from pylab import *
xlist = linspace(-1.0, 1.0, 200)
ylist = linspace(-1.0, 1.0, 200)
X, Y = meshgrid(xlist, ylist)
# print X
# print Y
Z = 12*X**2 + 6*X*Y + 2*Y**2 -2*X - Y
# print Z
figure()

CP1 = contour(X, Y, Z) # replace this
clabel(CP1, inline=True, fontsize=10) # replace this
title('Contour Plot')

xlabel('x (cm)')
ylabel('y (cm)')

savefig("f1.png")
