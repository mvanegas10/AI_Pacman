# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
#
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print "Start:", problem.getStartState()
    print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    print "Start's successors:", problem.getSuccessors(problem.getStartState())
    """
    "*** YOUR CODE HERE ***"

    pila = util.Stack()
    explorador = list()

    start = (problem.getStartState(),[],0)

    pila.push(start)

    while not pila.isEmpty():
        nodo, acciones, costo = pila.pop()

        if problem.isGoalState(nodo):
            return acciones

        if nodo not in explorador:
            explorador.append(nodo)
            for hijo, accion, costo_h in problem.getSuccessors(nodo):
                nuevo = (hijo, acciones+[accion], costo+costo_h)
                pila.push(nuevo)

    print "%s DFS no puede solucionar el ejercicio: Se acabo la pila %s" % ("*"*30,"*"*30)

    return []

    util.raiseNotDefined()

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"

    pila = []
    explorador = list()

    start = (problem.getStartState(),[],0)

    pila.append(start)


    while len(pila) != 0:
        nodo, acciones, costo = pila.pop()

        if problem.isGoalState(nodo):
            return acciones

        if nodo not in explorador:
            explorador.append(nodo)
            for hijo, accion, costo_h in problem.getSuccessors(nodo):
                nuevo = (hijo, acciones+[accion], costo+costo_h)
                pila.insert(0,nuevo)

    print "%s BFS no puede solucionar el ejercicio: Se acabo la pila %s" % ("*"*30,"*"*30)

    return []

    util.raiseNotDefined()

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    cola_prioritaria = util.PriorityQueue()
    nodos_explorados = list() #Lista que guarda los nodos explorados

    cola_prioritaria.push((problem.getStartState(),[]), 0) #Se agrega la tupla donde se encuentra el pacman

    while not cola_prioritaria.isEmpty(): #Si la cola no esta vacia
        nodo, acciones  = cola_prioritaria.pop()  #Se asigna el nodo eliminado de la cola prioritaria

        if problem.isGoalState(nodo): #Si el nodo es el objetivo se retorna la accion
            return acciones

        nodos_explorados.append(nodo)

        for hijo, accion, costo_h in problem.getSuccessors(nodo):
            if hijo not in nodos_explorados: #Si el nodo no esta en el nodo explorado
                cola_prioritaria.push((hijo, acciones + [accion]), problem.getCostOfActions(acciones + [accion]))#Se agrega hijo a la cola


    return []

    util.raiseNotDefined()

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    Abiertas = problem.getStartState();
    Cerradas = list()
    cola_prioritaria = util.PriorityQueue()

    cola_prioritaria.push((Abiertas, []), heuristic(Abiertas,problem))

    while not cola_prioritaria.isEmpty():
        nodo, acciones = cola_prioritaria.pop()

        if problem.isGoalState(nodo):
            return acciones

        Cerradas.append(nodo)

        for hijo, accion, costo_h in problem.getSuccessors(nodo):
            if hijo not in Cerradas:
                cola_prioritaria.push((hijo, acciones + [accion]), problem.getCostOfActions(acciones + [accion]) + heuristic(hijo, problem))


    return []
    util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
