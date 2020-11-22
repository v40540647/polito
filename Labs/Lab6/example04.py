def financialAid(kid , income):
  Aid = None
  if (income <=40000 and income >= 30000) and kid >=3:
    Aid = 1000 * kid
  elif (income < 30000 and income >20000) and kid >=2:
    Aid = 1500 * kid
  elif (income <20000):
    Aid = 2000 * kid
  return Aid
  
def main():
  metro = int(input("Enter the yearly income : "))
  kiddo = int(input("Enter the number of kids you have : "))
  Slatt = financialAid(kiddo , metro)
  print(f"Aid you recieve is : {Slatt}")

main()