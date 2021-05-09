from numpy import random

#Calculating the Probability theoretically

count = 0;
i = 0;
trials = 1000000
#array which stores the deck of cards
arr = ["K", "Q", "J", "A", 1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
       "K", "Q", "J", "A", 1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
       "K", "Q", "J", "A", 1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
       "K", "Q", "J", "A", 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

while i < trials:
  x = random.choice(arr, size = (3))

  if x[0] == "K" and x[1] == "K" and x[2] == "A" :
    count +=1

  i +=1    

theoretical_probability = count/trials

#Calculating experimental Probability
experimental_probability = (4/52)*(3/51)*(4/52)        #Since, cards drawn are King,King and then Ace

#printing probabilities
print("The Theoretical Proability is: ",theoretical_probability)
print("The Experimental Probability is: ",experimental_probability)
    


