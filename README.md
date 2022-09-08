# Dinosaur game with Genetic Algorithm

The dinosaur game by google chrome is a built-in game which is very simple and easy to play. Main goal of this project is to simulate the game and reach the high score. Genetic algorithm is used for optimization. The high score is achieved, and the game gets optimized more in every generation.

Usage of internet is increasing rapidly all over the world. People struggle what to do when the internet is down. It hard to pass time without internet. Playing games would be one of the options to do. Games are played for enjoyment, sometimes for achievements or for rewards. Google came up with the offline game called Dinosaur game, which is very simple, easy to play. This game is simulated using python creating ground and obstacles. The game should be optimized more to reach high score. For optimization, Genetic algorithm is used.

## Genetic algorithm

Genetic algorithm uses heuristic approach to get the optimized solution. Basically, GA have five steps of process, Initial population, Fitness function, Selection, Crossover, and mutation. These tasks are performed in every generation. This is repeated for pre-defined number of generations.

<img width="511" alt="Screen Shot 2022-08-29 at 8 21 42 PM" src="https://user-images.githubusercontent.com/38185827/187321287-f3997922-6b78-4607-b6f3-c92ac7c984c3.png">

## Implementation

Three modes are performed in this project. Game, Train, Simulate are these modes. Setting up the game with dinosaurs, obstacles, and the ground is the game mode.
The game is optimized with the best scores from n generations in the train mode. Once the game is trained, simulated game will be much better than the trained version, this can be compared in the simulated version.

Cactus is one of the obstacles where the image of the cactus is loaded with the help of pickle python package. This image is converted to data and stored in .npy file. Pterodactyls is also an obstacle where the image of it is loaded and masked into binary values and stored in a file. All these obstacles are simulated in the game these are controlled separately. This is performed by obstacle generator function.

The main program file initialise the population and it is set to 10 by default. We can increase the number of the population (or dino) by entering the number in the run time.
The whole game, simulation and the optimization is performed by game controller.

The interface displays 6 parameters while the game is simulated. The speed of the dinosaurs, number of dinosaurs alive, score, record is the best score from the pervious generation, generation, general record is the record the overall high score.

Here, the genetic algorithm is performed where the score of the dinosaur is the fitness function. Simple mutation is performed to find the best dinosaur from the generation and passed to the next generation. The canvas is reset to the initial position before every generation.

## Results

The weights and the bases are calculated for avoiding the collision while running on the path. These data are stored retrieved as array

<img width="680" alt="Screen Shot 2022-08-29 at 8 29 49 PM" src="https://user-images.githubusercontent.com/38185827/187322048-8dca4a6f-d1a9-49e7-b54b-e9f07fa54330.png">


## Alternative Approach

I have tried to implement this game using NEAT algorithm. Only one obstacle is implemented. Still more scope to improve the optimization. This is not that efficient currently. This is the network used to train the brain of the dinosaur. Optimization will be better compared to the original method.

## Conclusion

The dinosaur game by google is recreated, simulated, and optimized with the help of genetic algorithm. This project shows how to use the optimization algorithm (Genetic algorithm) to play a simple game designed by google. This project has more scope to improvise. Exploration of NEAT algorithm and implementing it in the game. Adding more efficient checkpoints to increase the speed of the dinosaurs. optimizing by reducing the generation number and increasing the score. enhance features of the game by adding more obstacles or adding actions other than jumping, ducking, and running. Increase convolution layers to predict the actions accurately.
