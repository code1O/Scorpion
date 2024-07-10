"""
# `scorpion.python`
Scientifical and data handler project

::

Scientifical functions ------ apple

::

Scientifical operations  ------ newton

::

Data handler ------ _defdatas

::

Quantic science ------ Quantica
"""

from .apple import (
sqrt, exp,
pi, e,
Delta, DeltaX,
degrees, radians,
fact, logn, floor,
absolute
)
from .newton import (
sin, cos, tangent,
quadratic_gen,
derivative, s_derivative,
factor, findfactor,
vectors, integral_defined,
preciss
)
from ._defdatas import (
matrix, locate_matrix,
matharray, Array,
conjugate
)

from .Quantica import (
  Gamma, phi,
  nabla, nabla_sqr, mats, psi_ket
)

