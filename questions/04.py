def concat (a, b):
  return a + ', ' + b

def input_concat():
  first_parameter = str(input("First parameter: "))
  second_parameter = str(input("Second parameter: "))
  result = concat(first_parameter, second_parameter)
  print(result)

input_concat()