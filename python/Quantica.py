"""
# `Quantica`
Python module made for quantum science.

Areas like:
- Quantum mechanics
- Quantum physics

"""

# Just advances of this module

from .apple import (
pi, sqrt, fact, _TypeData, _TypeNum
)
from .newton import (
derivative, s_derivative, sin, cos
)
from typing import TypeAlias

optional: TypeAlias = _TypeData | _TypeNum

def psi_qubit(dtype=bool,*,alpha, beta):
    """
    ```tex
    \left|\psi\rangle = \lfloor\alpha\rfloor+\lfloor\beta\rfloor
    ```
    """
    calculus = int(alpha) + int(beta)
    result = dtype(calculus)
    return result


def inverse_qubit(t_data=optional):
    """
    ```tex
    H\left|0\rangle = H\left|1\rangle
    ```
    """
    # in case of t_data=(...)
    def inverse_vector(vector):
        new_vec = []
        for bit in vector:
            new_vec.append(bit+1 if bit < 0 else bit-1)
        return new_vec
    # in case of t_data=n
    inverse_num = lambda n: n-1 if n > 0 else n+1
    is_num = isinstance(t_data, _TypeNum)
    return inverse_num(t_data) if is_num else inverse_vector(t_data)

class bidimension:
    
    def psi(n: _TypeNum=1,m: _TypeNum=2,*,x: _TypeNum, y: _TypeNum):
        equation_1 = sqrt(2)*sin(n*pi*x).deg
        equation_2 = sqrt(2)*sin(m*pi*y).deg
        return equation_1*equation_2
    
    def psi_pow(p: _TypeNum=1,*,x: _TypeNum, y: _TypeNum):
        """
        ```tex
        \psi^{(n}}(x+y)
        ```
        """
        formula = lambda num: ((-1)**(num+1))*fact(num)
        k, limit = 0, 100
        calculus = None
        while k <= limit:
            add = (x+y+k)**(n+1)
            (calculus:= 1/add)
            k+=1
        return formula(n)*calculus