from .apple import _TypeNum

class matrix:
  newvalues = []
  def __init__(self, _matrix: tuple, positional: int=0) -> None:
    self._matrix = _matrix
    self.positional = positional -1

  def create(rows: int, columns: int) -> tuple:
    _values = [0]*rows
    for i in range(columns):
      _values[i] = [0]*columns
    return _values

  def iterate(self, y_matrix: tuple, z_matrix: tuple|None = None, rtype: str = 'add') -> tuple:
    for i in range(len(self._matrix)):
      for j in range(len(self._matrix[self.positional])):
        matrix_x = self._matrix[i][j]; matrix_y = y_matrix[i][j]
        if rtype == 'mult':
          z_matrix[i][j] = matrix_x * matrix_y
        elif rtype == 'add':
          z_matrix[i][j] = matrix_x + matrix_y
        elif rtype == 'sub':
          z_matrix[i][j] = matrix_x - matrix_y
        elif rtype == 'div':
          z_matrix[i][j] = matrix_x / matrix_y
    return z_matrix

  def get(self, rtype: str) -> tuple:
    ArrayColumn = [x for x in self._matrix[self.positional]]
    if rtype == "column":
      return ArrayColumn
    elif rtype == "row":
      for value in self._matrix:
        self.newvalues.append(value[self.positional])
      return self.newvalues
    elif rtype == "matrix":
      return self._matrix

  def overwrite(self, value: any) -> tuple:
    if len(value) > len(self._matrix[self.positional]):
      value = value[:len(self._matrix[self.positional])]
    self._matrix[self.positional] = value
    return self._matrix

  def create_column(self) -> tuple:
    self._matrix.append([0]*len(self._matrix))
    return self._matrix

class locate_matrix:
  import json
  def __init__(self, _matrix: tuple, namefile: str) -> None:
    self._matrix = _matrix
    self.namefile = namefile
  def injson(self, section, position: int, section_value: str) -> any:
    position = position-1
    if not self.namefile.endswith('.json'):
      raise ValueError("File must end with \".json\"!")
    with open(file=self.namefile, mode='r+') as file_:
      data = self.json.load(file_)
      data[section][position][section_value] = self._matrix
      file_.seek(0)
      self.json.dump(data, file_)
      file_.truncate()

  def intxt(self) -> any:
    if not self.namefile.endswith(".txt"):
      raise ValueError("File must end with \".txt\"!")
      return None
    value = f"{self._matrix}\n\t"
    with open(self.namefile, mode="w") as file_dottxt:
      file_dottxt.write(("matrix: "+f"{value}\n"))
      return file_dottxt

class matharray:
  def __init__(self, values: tuple[_TypeNum]) -> None:
    self.values = values

  def sum(self, number: _TypeNum) -> _TypeNum:
    result = [x + number for x in self.values]
    if number < 0:
      raise ValueError('Number must be positive, not negative')
    else:
      return result

  def multiply(self, number: _TypeNum) -> _TypeNum:
    result = [x * number for x in self.values]
    if number < 0:
      raise ValueError('Number must be positive, not negative')
    else:
      return result

  def divide(self, number: _TypeNum) -> _TypeNum:
    result = [x / number for x in self.values]
    if number < 0:
      raise ValueError('Number must be positive, not negative')
    else:
      return result

  def subtract(self, number: _TypeNum) -> _TypeNum:
    result = [x - number for x in self.values]
    if number < 0:
      raise ValueError('Number must be positive, not negative')
    else:
      return result

  def selfsum(self) -> _TypeNum:
    """
    Sum values by itself
    ## Example
    >>> matharray([1, 2, 3, 4, 5]).selfsum()
    >>> 15 # (1 + 2) + (3 + 4) + 5
    """
    x = self.values; sum_ = 0
    for i in self.values:
      sum_ = x[i] + x[i + 1]
    return sum_

  def __str__(self) -> str:
    return self.values


class Array:
  empty_arr = []
  
  def __init__(self, array, position: int):
    self.tup = array; self.position = position -1
    
  def createArrayInside(self) -> tuple[tuple]:
    n = 0
    values = [x for x in self.tup]
    newArrayInside = self.empty_arr.insert(1, values)
    self.tup.insert(1, newArrayInside)
    for i in range (len(self.tup)-1):
      n = n * i
      self.tup[self.position].insert(1, n)
    self.tup[self.position].insert(1, newArrayInside)
    return self.tup