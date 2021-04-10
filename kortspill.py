import numpy as np
from joblib import Parallel, delayed

num_games = 1000000

def play_game():
    game_won = 0
    deck = np.asarray([[x for x in range(1,14)] for _ in range(4)]).flatten()
    #assert len(deck) == 52, "Erk, wrong deck size"
    np.random.shuffle(deck)
    game_over = False
    n = 1
    while not game_over:
        if len(deck) == 0:
            game_won = 1
            game_over = True
            continue
        drawn = deck[-1]
        deck = deck[0:-1]
        #print(deck)
        if drawn == n:
            n = 0
        n += 1
        if n == 13:
            game_over = True

    return game_won

gameres = Parallel(n_jobs=32)(delayed(play_game)() for _ in range(num_games))
game_won = sum(gameres)

print(f"Won {game_won} of {num_games}, or {(100*game_won)/num_games}%")
