from baseCompounds import *
from PotentialWell import PotentialWell
from PotWellSolver import PotWellSolver
from Plotter import Plotter
from pylab import *

GaAs = Compound(GaAsValues)
myPotWell = PotentialWell("z", 130, 1)

myPotWellSolver = PotWellSolver(GaAs, myPotWell, 6)
myPotWellSolver.setGridPoints(100)
myPlotter = Plotter()


kVec = arange(-3, 3, 0.1)
gridPointVec = arange(10, 350, 10)

myPlotter.plotGridPointAnalysis(myPotWellSolver, gridPointVec, 2)
myPlotter.displayPlots()






