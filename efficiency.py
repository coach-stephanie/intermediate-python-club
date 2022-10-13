#
# Efficiency Challenges
# 
# Each of the following functions take as input a list of "manatees"
# Each "manatee" is represented by a dictionary with properties like "name", "age", etc.
# n = the number of elements in the the manatees list 
# m = the number of properties each "manatee" dictionary has (ie. the number of keys in the dictionary)
#
# Using Big O notation, write the time complexity of each function. 
#
# Tip: Step through the code with some example input if you need help figuring out what it does!
#
#

def example1(manatees):
  for manatee in manatees:
    print(manatee['name'])


def example2(manatees):
  print(manatees[0]['name'])
  print(manatees[0]['age'])


def example3(manatees):
  for manatee in manatees:
    for manatee_property in manatee:
      print(manatee_property, ": ", manatee[manatee_property])


def example4(manatees):
  oldest_manatee = "No manatees here!"
  for manatee1 in manatees:
    for manatee2 in manatees:
      if manatee1['age'] < manatee2['age']:
        oldest_manatee = manatee2['name']
      else:
        oldest_manatee = manatee1['name']
  print(oldest_manatee)