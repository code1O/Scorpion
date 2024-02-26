from .apple import(
_TypeNum,
sqrt,
pi,
degrees,
fact,
exp
)

def quadratic_gen(a, b, c):
  result_1 = -b+(sqrt(pow(b, 2)-4*a*c))/2*a
  result_2 = -b-(sqrt(pow(b, 2)-4*a*c))/2*a
  return [result_1, result_2]

class factor:
  def __init__(self, values: tuple[_TypeNum]) -> None:
    def __top():
      x = values[0]
      if values[0] == -x and values[1] == x:
        return values[0]
      elif values[0] == x and values[1] == -x:
        return values[1]
      elif values[0] == x and values[1] == x:
        return values[1]
      else:
        return values[1]

    def __bottom():
      x = values[2]; y = values[3]
      if x == -values[0] and y == values[1]:
        return x
      elif x == values[0] and y == -values[1]:
        return y
      elif x == values[0] and y == values[1]:
        return y
      else:
        return y

    self.top = __top()
    self.bottom = __bottom()

  @property
  def Top(self) -> any:
    return self.top

  @property
  def Bottom(self) -> any:
    return self.bottom

  @property
  def Both(self) -> any:
    return [self.top, self.bottom]

  @property
  def Divide(self) -> _TypeNum:
    return self.top/self.bottom

class findfactor:
  def __init__(self, x: _TypeNum, y: _TypeNum) -> None:
    self.x = x
    self.y = y

  def DoubleBoth(self, rtype: str) -> _TypeNum:
    for i in range(round(sqrt(self.x))+1):
      for j in range(round(sqrt(self.y))+2):
        n = i; x = j
    # ========================
    if x > 5 or x == 5:
      x = x-2
    # ========================
    mult = x*n
    rTop = [mult / x, mult / n]
    rBott = [mult / n-1, -(mult /n-1)]
    mult_bott = (rBott[0] * rBott[1])
    mult_top = (rTop[0] * rTop[1])

    # ========================
    if rtype == "division":
      return mult_bott / mult_top
    elif rtype == "top":
      return rTop
    elif rtype == "bottom":
      return rBott

    # ========================

  def DoubleTop(self) -> _TypeNum:
    for i in range(round(sqrt(self.x))+2):
      x = i
    if self.y == 1 or self.y > 1:
      return x

  def DoubleBottom(self) -> _TypeNum:
    for i in range(round(sqrt(self.x))):
      for j in range(round(sqrt(self.y))+2):
        x = i; n = j
    nbott = x * n
    return (self.x / nbott)

class sin:
  def __init__(self, value: _TypeNum) -> None:
    self.value = value

  @property
  def deg(self) -> float:
    x = degrees(self.value)
    r = x-pow(x, 3)/fact(3)+pow(x, 5)/fact(5)
    return r-pow(x, 7)/fact(5)

  @property
  def radians(self) -> float:
    mapn = {0:1, 1:0, 2:-1, 3:0}
    DeltaX = self.value-pi/2
    res = sum([mapn[y%4]*pow(DeltaX, y)/fact(y) for y in range(20)])

class cos:
  def __init__(self, value: _TypeNum) -> None:
    self.value = value

  @property
  def deg(self) -> float:
    x = degrees(self.value)
    return 1-(pow(x, 2)/fact(2))+(pow(x, 4)/fact(4))-(pow(x, 6)/fact(6))
  
  @property
  def radians(self) -> float:
    xr = exp((self.value*1j)).real
    return xr

class tangent:
  def __init__(self, value: _TypeNum) -> None:
    self.value = value

  @property
  def degrees(self) -> float:
    return sin(self.value).degrees/cos(self.value).degrees

  @property
  def radians(self) -> float:
    return sin(self.value).radians/cos(self.value).radians
