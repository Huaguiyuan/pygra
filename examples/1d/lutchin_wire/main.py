# zigzag ribbon
import sys
sys.path.append("../../../pygra")  # add pygra library

import geometry
import topology
import operators
g = geometry.chain() # create geometry of a chain
h = g.get_hamiltonian(has_spin=True) # get the Hamiltonian, spinfull
h.add_rashba(0.5) # add Rashba SOC
h.add_zeeman(0.3) # add Zeeman field
h.shift_fermi(2.) # add Zeeman field
h.add_swave(0.2) # add swave pairing

h.get_bands(operator=operators.get_sy(h))
exit()
print(h.intra)

phi = topology.berry_phase(h) # get the berry phase
hf = h.supercell(100) # do a supercell
hf = hf.set_finite_system(periodic=False) # do an open finite system
hf.get_bands()
