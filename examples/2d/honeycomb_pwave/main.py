# zigzag ribbon
import sys
sys.path.append("../../../pygra")  # add pygra library

import numpy as np
import geometry
g = geometry.honeycomb_lattice()
g.write()
h = g.get_hamiltonian() # create hamiltonian of the system
h = h.get_multicell()
h.shift_fermi(.4)
h.add_pwave(0.1)
#h.add_swave(0.05)
h.check() # check that there is not anything weird
import topology

#a = topology.z2_vanderbilt(h)
import kdos
line = lambda x,y: np.linspace(x,y,200)
kdos.write_surface(h,energies=line(-.5,.5),klist=line(0.,1.))

h.get_bands()
