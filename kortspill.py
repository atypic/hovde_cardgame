import numpy as np
from joblib import Parallel, delayed

num_games = 1000000

def play_game():
    game_won = 0
    deck = np.asarray([[x for x in range(1,14)] for _ in range(4)]).flatten()
    #assert len(deck) == 52, "Erk, wrong deck size"
    np.random.shuffle(deck)
    n = 1
    while True:
        drawn = deck[-1]
        deck = deck[0:-1]
        
        if n == 13:
            break
        
        #we are out of cards. 
        if len(deck) == 0:
            if drawn == n:
                game_won = 1
            break
        
        if drawn == n:
            #we hit, reset counter
            n = 1
        else:
            n += 1

    return game_won

gameres = Parallel(n_jobs=32)(delayed(play_game)() for _ in range(num_games))
game_won = sum(gameres)

print(f"Won {game_won} of {num_games}, or {(100*game_won)/num_games}%")
