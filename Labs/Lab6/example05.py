def interest (amount , interest, year):
  amount = amount * (1 + (interest * 0.01))**year
  return amount

def main():
  start = float(input("Enter the money : "))
  interestrate = float(input("Enter the yearly interest rate in percentage (For example 5 if 5%) : "))
  years = int(input("Enter the num of years you want to keep that money on bank : "))
  lastmoney =interest(start , interestrate, years)
  print(f"Amount of money after {years} year/years is {lastmoney}")

main()

