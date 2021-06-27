import random
import math

"""
PART 5 - Average Price
[list of string prices (e.g. [$, $$]) ] => float
"""
def avg_price(prices):

  print("Prices input looks like the following", prices)
  # Replace the below code to calculate the average prices!
  # Keep in mind the type of our input (list of string)
  sum = 0
  for i in range(len(prices)):
    sum += len(prices[i])
  average = sum / len(prices) # <- TODO Replace this line
  average = round(average,2)
  return average

"""
PART 5 - Average Rating
[list of numbers] => float
"""
def avg_rating(ratings):
  print("Ratings input looks like the following", ratings)

  # Replace the below code to return the average of the values of the input
  # Keep in mind that the input here is a list of numbers

  sum=0
  for i in range(len(ratings)):
    sum+=ratings[i]

  average = sum / len(ratings) # <- TODO Replace this line
  #average = round(average,2)
  return average


"""
Don't change this method
[int, int] => [String, float]
"""
#  Calculates the type of emoji to display for current rating.
def calculate_moons(score, multiplier):
  # 🌑🌘🌓🌖🌕
  MOON_EMOJIS = ["&#x1F311","&#x1F318", "&#x1F317", "&#x1F316", "&#x1F315"]
  score = math.floor(float(score) * multiplier + 0.25) / multiplier
  score_copy = score

  display_string = ""
  for i in range (5):
    if(score> 1):
      display_string += MOON_EMOJIS[4]
      score -= 1
    else:
      display_string += MOON_EMOJIS[int(score*4)]
      score = 0

  return (display_string, score_copy)
