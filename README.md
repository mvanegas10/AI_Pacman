#The Pacman Projects: Search

Refer to the original project in [here](http://ai.berkeley.edu/search.html).

## Description
Solution to one of [The Pacman Projects](http://ai.berkeley.edu/project_overview.html) by the [University of California, Berkeley](http://berkeley.edu/).

![Animated gif pacman game](http://ai.berkeley.edu/images/pacman_game.gif)

## Scenarios

```
$ cd pacman-projects/p1_search

$ python pacman.py -l bigMaze -p SearchAgent -a fn=dfs -z .5
$ python pacman.py -l bigMaze -p SearchAgent -a fn=bfs -z .5

$ python pacman.py -l openMaze -p SearchAgent -a fn=dfs -z .5
$ python pacman.py -l openMaze -p SearchAgent -a fn=bfs -z .5

$ python pacman.py -l mediumMaze -p SearchAgent -a fn=ucs
$ python pacman.py -l mediumDottedMaze -p StayEastSearchAgent
$ python pacman.py -l mediumScaryMaze -p StayWestSearchAgent

$ python pacman.py -l trickySearch -p SearchAgent -a fn=bfs,prob=FoodSearchProblem
$ python pacman.py -l trickySearch -p SearchAgent -a fn=astar,prob=FoodSearchProblem,heuristic=foodHeuristic
```

## Author
<!-- Contributors table START -->
| [![Meili Vanegas](https://avatars.githubusercontent.com/mvanegas10?s=100)<br /><sub>Meili Vanegas</sub>](https://github.com/mvanegas10)<br /> |
| :---: |

<!-- Contributors table END -->
