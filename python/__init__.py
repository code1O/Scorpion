"""
# `scorpion.python`
Scientifical and data handler project

::

Scientifical funcitons ------ apple

::

Scientifical operations  ------ newton

::

Data handler ------ _defdatas
"""

from .apple import (
sqrt,
exp,
pi,
e,
Delta,
DeltaX,
degrees,
radians,
fact,
logn,
floor,
absolute
)
from .newton import (
sin,
cos,
tangent,
quadratic_gen,
gamma,
psi,
derivative,
s_derivative,
integral,
factor,
findfactor,
functions,
vectors,
integral_undefined,
integral_defined
)
from ._defdatas import (
matrix,
locate_matrix,
matharray,
Array
)

from functools import lru_cache

class demos:
  
  def __init__(self)-> None:...
  
  @property
  @lru_cache()
  def euler_approx(self):
    f = lambda x,y,z: 2*(x**2)+(3*(x*y)+z)**2
    df = (
    (f(6+DeltaX, 12+DeltaX, 30.85+DeltaX)-f(6,12,30.85))
    /DeltaX
    )/1e4
    def compute(dx):
      x,n,s = 0,1,0
      for r in range(x, 4):
        n += 1
        s = dx+(r/10**n)+((r+1)/10**(n or 2))+(10/10**5)
      result = s-(9/10**6)-(2/10**8)
      return result+(5.4e3/10**12)
    
    keywords = dict(guest_name="euler_approx", host_name="euler's num")
    return preciss(guest=compute(df),host=e, keywords=keywords)