from SABRs.util import *
from random import random as rd

"""
In baseball, a pitcher must record 27 outs in a row to throw a perfect game.
In this Monte Carlo Simulation, we will be simulating the first 27 batters who come
to the plate. If each and every batter makes an out (doesn’t get on base), our
simulated pitcher will have thrown a perfect game. Otherwise, at least one batter
will have reached base thus no perfect game, and we will ignore the rest of the
game. Using On-Base Percentage (OBP – i.e., not an out!) of 0.317, simulate the
outcome of 27 batters. Total up the number of batters who get on base. A perfect
game would have a total of zero batters reach base. This represents one simulated
game.
Run the simulation the 2,430 times (this is the total number of games in an MLB
regular season).
Run the simulation several times. How frequently did you get a perfect game?
"""

# consts
OBP = 0.317
num_batters = 27
num_seasons_simmed = 1000

# dyns
num_games_played = 0
num_perfect_games = 0

for _ in range(num_seasons_simmed * 2340): # n seasons * 2340 games per season
    OB = False
    for _ in range(27): # Number of ABs per game
        if rd() < OBP: # add one to OBP then break if a batter gets on
            OB = True
            break
    num_perfect_games += int(not OB)
    num_games_played += 1

print(f"{num_perfect_games} perfect games in {num_games_played} played, or {num_games_played / 2340} seasons")

# 78 games in 1000 seasons, or 12.82 seasons between games