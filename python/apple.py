"""
## `apple.py`

 Contains mathematical functions as

    * square root `sqrt`
    * factorial `fact`
    * e exponential `exp`
    * degrees
    * radians
    * natural logarithm `logn`

 Components
    
    * Delta
    * Standart Delta `DeltaX`
    * pi number `pi`
    * euler's number `e`
"""

from typing import (
SupportsFloat,
Union,
Dict,
Tuple,
List,
Set,
overload
)
from typing_extensions import (
SupportsIndex,
Literal,
TypeAlias
)

# Imported from external library
# as a type of data to return 
from numpy import (
    # Series of ints
    int8, int16, int32, int64,
    # Series of floats
    float16, float32, float64
)

from functools import lru_cache
import sys

pi: float = 3.141592653589793
e: float = 2.7182818284590452

# `Delta` is dynamic, `DeltaX` is constant
# in other words, `DeltaX` it's the standart value
# meanwhile `Delta` is for any Real value

Delta: float = lambda x,y: 0 if not y > 1 else (x*10**(-y))
DeltaX: float = (1*10**(-3))


if sys.version_info >= (3, 8):
    _TypeNum: TypeAlias = SupportsFloat | SupportsIndex
else:
    _TypeNum: TypeAlias = SupportsFloat

_Typedata: TypeAlias = Union[List[_TypeNum], Set[_TypeNum],
Tuple[_TypeNum], Dict[str, _TypeNum]]

PositiveInt = Literal[
0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12,
13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23,
24, 25
]

NegativeInt = Literal [
-1, -2, -3, -4, -5, -6, -7, -8, -9, -10, -11,
-12, -13, -14, -15, -16, -17, -18, -19, -20
]

LiteralInteger: TypeAlias = PositiveInt | NegativeInt | Literal[0]

_TdataNum: TypeAlias = _Typedata | _TypeNum

def __degrees(value) -> float: return (value*pi)/180
@overload
def degrees(value: float) -> float:...
@overload
def degrees(value: LiteralInteger) -> float:...
@lru_cache()
def degrees(value) -> float: return __degrees(value)

def __radians(value) -> float: return (value/180)*pi
@overload
def radians(value: LiteralInteger) -> float:...
@overload
def radians(value: float) -> float:...
@lru_cache()
def radians(value) -> float: return __radians(value)

def __sqrt(value) -> float:
    res = 0
    if value < 0:
        res = abs(value)**(1/2)
    else:
        res = value**(1/2)
    return res
@overload
def sqrt(value: LiteralInteger) -> float:...
@overload
def sqrt(value: float) -> float:...
@lru_cache()
def sqrt(value) -> float: return __sqrt(value)

def __exp(value) -> float: return pow(e, value)
def exp(value: _TypeNum) -> float: return __exp(value)

@overload
def fact(value: LiteralInteger) -> float:...
@overload
def fact(value: float) -> float:...
@lru_cache()
def fact(value) -> float:
    n = float(1)
    if value == 0 or value == 1: return 1
    for i in range(1, value+1):
        n = n * i
    return float(n)

def __logn(value) -> float: n=float(10*100); return n*((value**(1/n))-1)
@overload
def logn(value: LiteralInteger) -> float:...
@overload
def logn(value: float) -> float:...
def logn(value) -> float: return __logn(value)

@lru_cache()
def floor(x: _TypeNum) -> int:
    if type(x) == int: return x
    return int(x)

@lru_cache()
def absolute(x: _TypeNum):
    if x > 0: return x
    elif x < 0: return (x)*(-1)