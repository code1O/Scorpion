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
  
  @property
  @lru_cache()
  def euler_approx():
    x, y, z = 6, 12, 31.85
    f = lambda x,y,z: 2*(x**2)+(3*(x*y)+z)**2
    custom_df = (
    f(x+DeltaX, y+DeltaX, z+DeltaX)-f(x,y,z)
    /DeltaX
    )
    def compute(derivative):
      dx = derivative/1e4
      x,n,s = 0,1,0
      for r in range(x, 4):
        n += 1
        (s:= dx+(r/10**n+1)-(r/10**((n+1) or 2)))
      result = s+(10/10**5)-(9/10**6)-(2/10**8)
      return result+(5.4e3*10**(-12))
    
    keywords = dict(guest_name="euler_approx", host_name="euler's num")
    return preciss(guest=compute(custom_df),host= e)