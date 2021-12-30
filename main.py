
import sys
from dino.GameController import GameController
import weakref
args = sys.argv

if(args[1] in ['game', 'simulation', 'train']):
    dinos_per_gen = 10  # population
    if(args[1] in ['simulation', 'train']):
        if(len(args) > 2):
            dinos_per_gen = int(args[2])
    game = GameController(args[1], dinos_per_gen)
    f = weakref.finalize(game, game.saveGeneralRecord)
    game.run()
else:
    print('Command not found')
