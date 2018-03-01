def read_file(filename):
  map = Nil

  with open(filename) as f:
    lines = f.readlines()

    first_line = true
    for line in lines:
      elements = line.split(" ")
      int_elements = [int(el) for el in elements]
      if first_line:
        first_line = false
        map = Map(int_elements[0], int_elements[1])

      else:


  return {'map': map}



