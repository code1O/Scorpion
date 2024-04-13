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
    return res

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
    return sin(self.value).deg/cos(self.ivalue).deg

  @property
  def radians(self) -> float:
    return sin(self.value).deg/cos(self.value).radians


class functions:
  """
  functions or also called:
  
  f(x), g(x), h(x), etc...
  """
  def __init__(self, func, x_value) -> None:
    self.func = func
    self.function_x, self.x_value = func(x_value), x_value
  
  def set_function(self):
    return self.func
  
  def fdeltax(self, deltax: _TypeNum=0.001):
    result = ((self.func(self.x_value+deltax)-(self.function_x))/deltax)
    return result

class vectors:
  import matplotlib.pyplot as plt
  import numpy as np
  def __init__(self, Fx: _TypeNum, Fy: _TypeNum) -> None:
    self.Fx, self.Fy = Fx, Fy
  
  def calculate(self, angule:tuple[bool, _TypeNum], R_:tuple[bool, _TypeNum]):
    result = None
    if angule[0] == True and R_[0] == True:
      tanAlpha = self.np.arctan(self.np.degrees(self.Fx/self.Fy))
      (result:= [angule[1], R_[1], tanAlpha])
    elif angule[0] == True and (R_[0] == False and R_[1] == 0):
      R = sqrt((self.Fx**2)+(self.Fy**2))
      tanAlpha = self.np.arctan(self.np.degrees(self.Fx/self.Fy))
      (result:= [angule[1], R, tanAlpha])
    return result
  
  def plot(self, *args) -> None:
    R_Params = args[1]
    result = self.calculate(angule=args[0], R_=R_Params)
    Vx, Vy = result[1]*cos(result[0]).radians, result[1]*sin(result[0]).radians
    def set_info(Vx, Vy):
      fig, ax = self.plt.subplots(figsize=(8,8))
      ax.spines['left'].set_position('zero')
      ax.spines['bottom'].set_position('zero')
      ax.spines['top'].set_visible(False)
      ax.plot((1), (0), marker='>', transform=ax.get_yaxis_transform(), color='black')
      ax.plot((0), (1), marker='^', transform=ax.get_xaxis_transform(), color='black')
      ax.set_xlim(-5, 5)
      ax.set_ylim(-5, 5)
      ax.set_xticks(self.np.arange(-5, 6, 1))
      ax.set_yticks(self.np.arange(-5, 6, 1))
      ax.grid(which='both', color='grey', linewidth=1, linestyle='-', alpha=0.2)
      self.plt.quiver(0, 0, Vx, Vy, angles='xy', scale_units='xy', scale=1, color='r')
    set_info(Vx, Vy)
    self.plt.show()

class integral_undefined:
  from ._defdatas import Array
  def __init__(self, operation) -> None:
    self.operation = operation

  def sum_pownums(self, x: str) -> str:
      list_: tuple = []
      nums: tuple[str] = x.replace(" ", "").split(";")
      array_values = nums[0:self.Array(nums, 1).bignotation("O(log n)", "")]
      for x in array_values:
          y: int = int(x[2])+1
          list_.append((int(x[0])**y)/y)
      return list_

  def calculate(self, *args, func_result=lambda x,y: x*y):
    arg1 = self.sum_pownums(args[0])
    return [func_result(self.operation, float(y[2])) for y in arg1]

class integral_defined(integral_undefined):
    from ._defdatas import Array
    def __init__(self, operation, range_:tuple[int, int]) -> None:
        self.ranges, self.operation = range_, operation

    def sum_pownums(self, x: str) -> str:
        list_: tuple = []
        nums: tuple[str] = x.replace(" ", "").split(";")
        for params in nums:
            _powchar_pos = self.Array(nums, 1)\
            .bignotation("O(log n)", "^")
            if not params in ["x", "y"]:
                y = float(params[0])**(float(params[_powchar_pos+1:])+self.ranges[0])
            else:
                y = float(params[_powchar_pos+1:])+self.ranges[0]
            list_.append(y)
        return list_

    def calculate(self, *args):
        dx, arg1 = (self.ranges[0]/self.ranges[1]), self.sum_pownums(args[0])
        return [dx*y for y in arg1]

class preciss:
    import matplotlib.pyplot as plt
    def __init__(self, guest: _TypeNum, host: _TypeNum, keywords: dict|None = None) -> None:
        self.keywords = keywords
        self._guest, self._host = guest, host
        similar_percent = abs(guest-host)
        error_percent = (similar_percent/host)/10
        self.percents = (similar_percent, error_percent)
    
    def plot(self, title: str, **kwargs) -> None:
        list_ = {
            "path_file": str,
            "name_file": str
        }
        list_.update(kwargs)
        categories = ["Similar", "Error"]
        self.plt.figure(figsize=(8,5))
        self.plt.bar(categories, self.percents, color=["blue", "red"])
        self.plt.title(title)
        self.plt.ylabel("percent %")
        self.plt.ylim(0,10)
        for x,y in enumerate(self.percents):
            self.plt.text(x, y+0.2, f"{y}%", ha="center", va="bottom")
        self.plt.show()
        self.plt.savefig(f"{list_['path_file']}/{list_['name_file']}.png")
    
    def __str__(self) -> str:
        str1 = f"{self.keywords['guest_name']}: {self._guest}\n"
        str2 = f"Similarity to {self.keywords['host_name']}: {str(self.percents[0])[:4]}%\n"
        str3 = f"Error percent: {str(self.percents[1])[:4]}%"
        return str1+str2+str3