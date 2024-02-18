import random as rand

# [Head, Tail] = [True, False]
HEAD = True
TAIL = False
def coin_toss():
     return rand.choice((HEAD, TAIL))