from random import random as rd
from random import randint as ri

# Def used data types and functions

class p_dist():
    def __init__(self):
        self.events = []
        self.probs = []

    def __init__(self, events: list, probs: list):
        self.events = events
        self.probs = probs
    
    def gen_uniform_dist(self, n: int, zero_index: bool):
        self.events = [i + zero_index for i in range(n)] #0 ... n-1 or 1 ... n depending on zero_index
        self.probs = [round(1/n, 10) for _ in range(n)] #round to prevent floating point imprecision
    
    def set_dist(self, events: list, probs: list):
        self.events = events
        self.probs = probs
    
    def set_events(self, events: list):
        self.events = events
    
    def set_probs(self, probs:list):
        self.probs = probs
    
# General functions