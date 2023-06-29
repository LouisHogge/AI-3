# Complete this class for all parts of the project

from pacman_module.game import Agent
from pacman_module.pacman import Directions


class PacmanAgent(Agent):
    def __init__(self, args):
        """
        Arguments:
        ----------
        - `args`: Namespace of arguments from command-line prompt.
        """
        self.args = args

    def get_action(self, state, belief_state):
        """
        Given a pacman game state and a belief state,
                returns a legal move.

        Arguments:
        ----------
        - `state`: the current game state. See FAQ and class
                   `pacman.GameState`.
        - `belief_state`: a list of probability matrices.

        Return:
        -------
        - A legal move as defined in `game.Directions`.
        """

        # XXX: Your code here to obtain bonus
        import numpy as np

        pacman_position = state.getPacmanPosition()

        # On récupère la position de la probabilité la plus haute de "belief_state"
        max_value = np.max(belief_state)
        max_indice = np.where(belief_state == max_value)
        x = max_indice[1]
        y = max_indice[2]

        # On calcule la distance entre la position actuelle de pacman et la position de la plus haute probabilité
        dist = abs(pacman_position[0]-x[0]) + abs(pacman_position[1]-y[0])

        good = []

        # On note dans "good" la ou les mouvements qui réduisent la distance pacman-ghost
        for next_state, action in state.generatePacmanSuccessors():
            next_pacmanpos = next_state.getPacmanPosition()

            new_dist = abs(next_pacmanpos[0]-x[0]) + abs(next_pacmanpos[1]-y[0])

            if new_dist < dist:
                good.append(action)

        Directions.STOP = 'Stop'

        # On privilégie la direction dans laquelle la distance pacman-ghost est la plus grande,
        # si aucun mouvement ne correspond à ce critère, on en choisi un qui est simplement inclu dans "good"
        if abs(pacman_position[0]-x[0]) > abs(pacman_position[1]-y[0]):
            if 'East' in good:
                Directions.STOP = 'East'
            elif 'West' in good:
                Directions.STOP = 'West'
        if Directions.STOP == 'Stop':
            if 'South' in good:
                Directions.STOP = 'South'
            elif 'North' in good:
                Directions.STOP = 'North'
        if Directions.STOP == 'Stop':
            if 'East' in good:
                Directions.STOP = 'East'
            elif 'West' in good:
                Directions.STOP = 'West'

        # XXX: End of your code here to obtain bonus

        return Directions.STOP
