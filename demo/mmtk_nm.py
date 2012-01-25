# -*- coding: utf-8 -*-
"""
Created on Tue Nov  8 14:21:35 2011

@author: -
"""

# Standard normal mode calculation.
#

from MMTK import *

from MMTK.Proteins import Protein
from MMTK.ForceFields import Amber94ForceField
from MMTK.NormalModes import NormalModes

from MMTK.Minimization import ConjugateGradientMinimizer
from MMTK.Trajectory import StandardLogOutput
from MMTK.Visualization import view


# Construct system
universe = InfiniteUniverse(Amber94ForceField())
universe.protein = Protein('bala1')

# Minimize
minimizer = ConjugateGradientMinimizer(universe,
                                       actions=[StandardLogOutput(50)])
minimizer(convergence = 1.e-3, steps = 10000)

# Calculate normal modes
modes = NormalModes(universe)

# Print frequencies
for mode in modes:
    print mode


# Show animation of the first non-trivial mode 
#view(modes[6])