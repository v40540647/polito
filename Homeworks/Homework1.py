from random import randint
 
#Doing first one as elegant as possible and second one as compact as possible
def main():
  num_scores = int(input("Number of scores: "))
  scores = []
  for i in range(num_scores):
      scores.append(randint(1, 30))
  removed_scores = sortnpop(scores)
  average_scores = average(scores)
  print(f"Original scores: {scores}, removing lowest: {removed_scores}, average: {average_scores}")

def sortnpop(scores):
  # ∬ ✧✧ ♛♛♛♛♛♛♛♛♛♛♛♛♛♛♛♛♛♛♛♛♛♛ ✧✧ ∬ 
  changed_list = list(scores)
  changed_list.sort()
  changed_list.pop(0)
  return changed_list
  # ∬ ✧✧ ♛♛♛♛♛♛♛♛♛♛♛♛♛♛♛♛♛♛♛♛♛♛ ✧✧ ∬ 

def average(scores):
  t=0  
  for s in scores:
    t+=s
  return t/len(scores)

if __name__ == '__main__':     
    main()