import sys
import os
sys.path.append("../../../pygra")  # add the pygra library
import geometry
import numpy as np
import hybrid
import films
import operators

g = geometry.diamond_lattice_minimal() # get the three dimensional diamond lattice

g = films.geometry_film(g,nz=20) # create a film
h = g.get_hamiltonian(is_multicell=True) # create hamiltonian



def get_hamiltonian():
  """Hamiltonian for parameter p"""
  h = g.get_hamiltonian(is_multicell=True,is_sparse=False) # create hamiltonian
  def step(z,width=0.00001):
    """This will yield 0 for z<0 and 1 for z>0"""
    out = (-np.tanh(z/width)+1.0)/2. # this is the interpolator
    return out
  h.add_antiferromagnetism(lambda r: 0.7*step(r[2])
          ,axis=[0.,0.,1.])
  h.shift_fermi(lambda r: 1.*(-step(r[2],width=0.0001)+1.0))
  h.add_swave(lambda r: 0.4*(-step(r[2])+1.0))
  h.add_kane_mele(0.05)
  return h

h = get_hamiltonian()

h.get_bands(operator=operators.get_sz(h))

import kdos
#kdos.kdos_bands(h,delta=0.01)
