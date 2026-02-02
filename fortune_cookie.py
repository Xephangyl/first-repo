import random

fortunes = ["Don't pursue happiness – create it.",
              "All things are difficult before they are easy.",
              "The early bird gets the worm, but the second mouse gets the cheese.",
              "Someone in your life needs a letter from you.",
              "Don't just think. Act!",
              "The fortune you search for is in another cookie.",
              "Help! I'm being held prisoner in a chinese bakery!"
             ]

def fortune():
  rfortune = random.randint(0, len(fortunes) -1)
  print(fortunes[rfortune])

fortune()
fortune()
fortune()