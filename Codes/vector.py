import time
import numpy as np

class Vector:
  def __init__(self, lenght = 0):
    self.it = 0
    self.vector = [None] * lenght
     
  def insert(self, value):
    if self.it < len(self.vector):
      
      if self.it == 0: # First insert
        self.vector[self.it] = value
        self.it += 1

      elif value >= self.vector[self.it - 1]: 
        self.vector[self.it] = value
        self.it += 1

      else:
        for (i, j) in enumerate(self.vector):
          if value < j:
            # print(value, i, j, self.it)

            for k in range(self.it ,i, -1 ):
              self.vector[k], self.vector[k-1] = self.vector[k-1], None
            
            self.vector[i] = value
            self.it += 1
            break
  
  def search(self, value):
    for index, i in enumerate(self.vector):
      if i == value:
        return index 

    return "Not found"

  def __getitem__(self, ind):
    return self.vector[ind]

  def __setitem__(self, ind, newvalue):
    self.vector[ind] = newvalue

  def __str__(self) -> str:
    return str(self.vector)

  def binary_search(self, value):
    start = 0
    end = self.it
    index = end // 2 

    if value > self.vector[end-1] or value < self.vector[start]:
      return "Not found"

    while value != self.vector[index]:      
      print("Middle:",index)
      
      if start > end:
        return "--|Not Found|--"

      elif value < self.vector[index]:
        end = index - 1
        print("<", start, "+", end, "//", 2)
        
        index = (start + end) // 2

      elif value > self.vector[index]:
        start = index + 1
        print(">", start // end, "//", 2)

        index = (start + end) // 2

    return index, "|", value
    

SIZE_ = [10,100,1000,2000,4000,8000,16000,32000]

def computer():

  for i in SIZE_:
    v = Vector(i)

    for _ in np.floor(np.random.uniform(0, 100, i)):
      v.insert(_)

    startTime_Linear = time.time()
    v.search(2)
    endTime_Linear = time.time()

    Linear = endTime_Linear - startTime_Linear

    startTime_Binary = time.time()
    v.binary_search(2)
    endTime_Binary = time.time()

    Binary = endTime_Binary - startTime_Binary

    print(f'Size: {i} Linear: {Linear} Binary: {Binary}')

v = Vector(5)

for i in [1,3,5,7,9]:
  v.insert(i)
print(v)

print(v.binary_search(4))
