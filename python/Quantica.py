"""
# `Quantica`
Python module made for quantum science.

Areas like:
- Quantum mechanics
- Quantum physics

"""

from .apple import (
pi, sqrt, fact, _Typedata, _TypeNum
)
from .newton import (
derivative, s_derivative, sin, cos
)
from ._defdatas import (
conjugate
)
from typing import TypeAlias
import scipy.linalg as linalg

# type of data
from .apple import (
    int16, float16
)

h = 6.62607015e-34
hbar = h/(2*pi)
gamma = 0.57721
phi = (1+sqrt(5))/2

class mats:
    """
    Essential maatresses for quantum mechanic
    
    - Pauli's matresses
    
      \\sigma^\\mu
    - gamma matresses
    
      \\gamma^\\mu
    """
    Pauli = {
    "mat_1": [0, 1, 1, 0],
    "mat_2": [0, -1j.imag, 1j.imag, 0],
    "mat_3": [1, 0, 0, -1],
    }
    __Pauli_conjg = {
        "mat_1": conjugate(Pauli["mat_1"]),
        "mat_2": conjugate(Pauli["mat_2"]),
        "mat_3": conjugate(Pauli["mat_3"])
    }
    gamma_mats = {
        "mat_1": [0, Pauli["mat_1"], __Pauli_conjg["mat_1"], 0],
        "mat_2": [0, Pauli["mat_2"], __Pauli_conjg["mat_2"], 0],
        "mat_3": [0, Pauli["mat_3"], __Pauli_conjg["mat_3"], 0]
    }

def nabla_sqr(beggin=[1,1,1],*,var: _Typedata, power: _Typedata):
    
    derivatives = None
    for k in beggin:
        for v in var:
            (derivatives:= [s_derivative(k,v,n) for n in power])
    return sum(derivatives)

def nabla(beggin=[1,1,1],*,var: _Typedata, power: _Typedata):
    
    derivatives = None
    for k in beggin:
        for v in var:
            (derivatives := [derivative(k,v,n) for n in power])
    return derivatives

optional: TypeAlias = _Typedata | _TypeNum

def psi_ket(dtype=bool,*,alpha, beta):
    """
    Calculate the basic of quantum mechanics
    
    \\ket{\\psi} = \\alpha\\ket{0} + \\alpha\\ket{1}
    """
    calculus = int(alpha) + int(beta)
    result = dtype(calculus)
    return result

def inverse_qubit(t_data=optional):
    """
    Implement an hadamard's gate to a bit
    
    H\\ket{0} = \\ket{1}
    
    H\\ket{1} = \\ket{0}
    """
    
    # in case of t_data=(...)
    def inverse_vector(vector):
        new_vec = []
        for bit in vector:
            if bit > 1 or bit < 0:
                raise ValueError("bit must contain only 0 and 1")
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
        
        formula = lambda num: ((-1)**(num+1))*fact(num)
        k, limit = 0, 100
        calculus = None
        while k <= limit:
            add = (x+y+k)**(k+1)
            (calculus:= 1/add)
            k+=1
        return formula(k)*calculus

def Gamma(x: _TypeNum, y: _TypeNum=0, recursive: bool=False):
    n = x-2 if x >= 3 else 1
    recursive_ = lambda x,y: (x/y)*n/y if not y == 0 else x*fact(x-1)
    not_recursive = lambda x,y: n/y*int(sqrt(pi)) if not y == 0 else fact(x-1)
    return not_recursive(x,y) if recursive == False else recursive_(x,y)


class hilbert:
    def __init__(self, alpha, beta):
        self.vec_alpha, self.vec_beta = alpha, beta
    
    def dagger(self):
        functionality = lambda vector: [item.conjugate() for item in vector]
        
        beta_conjugation = functionality(self.vec_beta)
        alpha_conjugation = functionality(self.vec_alpha)
        return (alpha_conjugation, beta_conjugation)