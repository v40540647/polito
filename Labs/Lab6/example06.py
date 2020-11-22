def returner(value):
  if value == "I":
    return 1
  elif value == "V":
    return 5 
  elif value == "X":
    return 10
  elif value == "L":
    return 50
  elif value == "C":
    return 100
  elif value == "D":
    return 500
  elif value == "M":
    return 1000
  else:
    return None
def Calculator(values):
  endvalue = 0
  while len(values) != 1:
    if returner(values[0]) >= returner(values[1]) or len(values) == 1:
      endvalue = endvalue + returner(values[0])
      values.pop(0)
    else:
      endvalue = endvalue + (returner(values[1]) - returner(values[0]))
      values.pop(0)
      values.pop(0)
  endvalue = endvalue + returner(values[0])
  return endvalue 




def main():
  n = input("Enter the roman numbers : ")
  list1 = list(n.upper())
  
  slatt = Calculator(list1)
  print(slatt)




main()