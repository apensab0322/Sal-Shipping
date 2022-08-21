name = "Bozo"
question = "Am I going to be rich?"
answer = ""
import random

random_number = random.randint(1,9)

print(name + " asks: " + question)


if random_number == 1:
  answer = "Hell yea Brother, give me some."
elif random_number == 2:
  answer = "Only if you share you will win."
elif random_number == 3:
  answer = "I am not sure"
elif random_number == 4:
  answer = "You look greedy, so heck no"
elif random_number == 5:
  answer = "Not only you are not winning, I am taking all your money"
else:
  answer = "Error"

print("Magic 8-Ball's answer: " + answer)
