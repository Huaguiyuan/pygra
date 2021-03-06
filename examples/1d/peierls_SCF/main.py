# zigzag ribbon
import sys
sys.path.append("../../../pygra")  # add pygra library

import numpy as np
import geometry
import scftypes
import operators
from scipy.sparse import csc_matrix
g = geometry.chain()
g = g.supercell(4)

h = g.get_hamiltonian() # create hamiltonian of the system
h = h.get_multicell()

h.remove_spin()

mf = np.random.random(h.intra.shape) -.5  
mf = np.matrix(mf)
mf = mf + mf.H

scf = scftypes.selfconsistency(h,nkp=40,filling=0.5,g=3.0,
              mix=0.9,mf=mf,mode="V")
h = scf.hamiltonian # get the Hamiltonian
h.get_bands() # calculate band structure


import groundstate

groundstate.hopping(h)
