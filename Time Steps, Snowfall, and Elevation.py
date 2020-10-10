import numpy
import matplotlib.pyplot as plt

# Constant definitions:
nX = 10                # number of grid points
domainWidth = 1e6      # meters
timeStep = 100         # years
nYears = 25000         # years
flowParam = 1e4        # m horizontal / yr
snowFall = 0.5         # m / y
dX = domainWidth / nX  # years

#Configure matplotlib plot figure and add a subplot
fig = plt.figure()
ax = fig.add_subplot(1,1,1)

#Initialize the elevations as array of nX+2 elements and set to zero
elevations = numpy.zeros(nX+2)

#Initialize the fluxes as array of nX+1 elements and set to zero
flows = numpy.zeros(nX+1)

#Time steps loop
for Years in range (0,nYears+1, timeStep):

    #flow calculations loop
    for ix in range (0,nX+1):
        flows[ix] = ( elevations[ix] - elevations[ix+1] ) / dX * flowParam  * ( elevations[ix]+elevations[ix+1] ) / 2 / dX
    
    #elevation calculations loop
    for ix in range (1,nX+1):
        elevations[ix] = elevations[ix] + ( snowFall + flows[ix-1] - flows[ix] ) * timeStep
    
    #print timestep years and plot elevations
    print(Years)
    ax.clear()
    ax.plot(elevations)
    plt.ylim(0,5000)
    plt.show(block=False)
    plt.pause(0.001)
