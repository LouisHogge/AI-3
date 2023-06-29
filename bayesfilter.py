# Complete this class for all parts of the project

from pacman_module.game import Agent
import numpy as np
from pacman_module import util
from scipy.stats import binom


class BeliefStateAgent(Agent):
    def __init__(self, args):
        """
        Arguments:
        ----------
        - `args`: Namespace of arguments from command-line prompt.
        """
        self.args = args

        """
            Variables to use in 'update_belief_state' method.
            Initialization occurs in 'get_action' method.

            XXX: DO NOT MODIFY THE DEFINITION OF THESE VARIABLES
            # Doing so will result in a 0 grade.
        """

        # Current list of belief states over ghost positions
        self.beliefGhostStates = None

        # Grid of walls (assigned with 'state.getWalls()' method)
        self.walls = None

        # Hyper-parameters
        self.ghost_type = self.args.ghostagent
        self.sensor_variance = self.args.sensorvariance

        self.p = 0.5
        self.n = int(self.sensor_variance/(self.p*(1-self.p)))

        # XXX: Your code here
        # NB: Adding code here is not necessarily useful, but you may.
        # XXX: End of your code

    def _get_sensor_model(self, pacman_position, evidence):
        """
        Arguments:
        ----------
        - `pacman_position`: 2D coordinates position
          of pacman at state x_{t}
          where 't' is the current time step

        Return:
        -------
        The sensor model represented as a 2D numpy array of
        size [width, height].
        The element at position (w, h) is the probability
        P(E_t=evidence | X_t=(w, h))
        """

        w_max = self.walls.width
        h_max = self.walls.height
        prob = np.zeros((w_max, h_max))

        # On rempli le tableau "prob" avec les pmf binomiales
        for x in range(0, w_max):
            for y in range(0, h_max):
                distance = abs(util.manhattanDistance((x, y), pacman_position) - evidence)
                noise = binom.pmf(self.n*self.p + distance, self.n, self.p)
                prob[x][y] = noise

        return prob

    def _get_transition_model(self, pacman_position):
        """
        Arguments:
        ----------
        - `pacman_position`: 2D coordinates position
          of pacman at state x_{t}
          where 't' is the current time step

        Return:
        -------
        The transition model represented as a 4D numpy array of
        size [width, height, width, height].
        The element at position (w1, h1, w2, h2) is the probability
        P(X_t+1=(w1, h1) | X_t=(w2, h2))
        """
        w_max = self.walls.width
        h_max = self.walls.height
        walls = self.walls
        scared_prob = 2**3
        afraid_prob = 2
        confused_prob = 1

        # On determine le coefficient en fonction du ghost
        if self.ghost_type == 'scared':
            ghost_prob = scared_prob
        elif self.ghost_type == 'afraid':
            ghost_prob = afraid_prob
        else:
            ghost_prob = confused_prob

        prob = np.zeros((w_max, h_max, w_max, h_max))

        for x in range(0, w_max):
            for y in range(0, h_max):
                possible_move = 0
                prob_near = np.array([0, 0, 0, 0])
                if walls[x][y] == 1:
                    possible_move = 0

                # On regarde si la case appartient au plateau
                # Et si la manhattan distance de la position actuelle en fonction de celle de pacman
                # est plus petite que celle de la future position en fonction de celle de pacman,
                # alors on utilise le coefficient propre au type de ghost
                elif x-1 >= 0 and x+1 < w_max and y-1 >= 0 and y+1 < h_max:
                    if walls[x+1][y] == 0:  # right
                        possible_move = possible_move + 1
                        if util.manhattanDistance((x, y), pacman_position) < util.manhattanDistance((x+1, y),
                                                                                                    pacman_position):
                            prob_near[0] = ghost_prob
                        else:
                            prob_near[0] = 1
                    if walls[x-1][y] == 0:  # left
                        possible_move = possible_move + 1
                        if util.manhattanDistance((x, y), pacman_position) < util.manhattanDistance((x-1, y),
                                                                                                    pacman_position):
                            prob_near[1] = ghost_prob
                        else:
                            prob_near[1] = 1
                    if walls[x][y-1] == 0:  # up
                        possible_move = possible_move + 1
                        if util.manhattanDistance((x, y), pacman_position) < util.manhattanDistance((x, y-1),
                                                                                                    pacman_position):
                            prob_near[2] = ghost_prob
                        else:
                            prob_near[2] = 1
                    if walls[x][y+1] == 0:  # down
                        possible_move = possible_move + 1
                        if util.manhattanDistance((x, y), pacman_position) < util.manhattanDistance((x, y+1),
                                                                                                    pacman_position):
                            prob_near[3] = ghost_prob
                        else:
                            prob_near[3] = 1

                    # On normalise
                    if sum(prob_near) != 0:
                        coeff_sum = 1 / sum(prob_near)

                        prob[x - 1, y, x, y] = coeff_sum * prob_near[1]  # left
                        prob[x + 1, y, x, y] = coeff_sum * prob_near[0]  # right
                        prob[x, y - 1, x, y] = coeff_sum * prob_near[2]  # up
                        prob[x, y + 1, x, y] = coeff_sum * prob_near[3]  # down
        return prob

    def _get_updated_belief(self, belief, evidences, pacman_position,
            ghosts_eaten):
        """
        Given a list of (noised) distances from pacman to ghosts,
        and the previous belief states before receiving the evidences,
        returns the updated list of belief states about ghosts positions

        Arguments:
        ----------
        - `belief`: A list of Z belief states at state x_{t-1}
          as N*M numpy mass probability matrices
          where N and M are respectively width and height
          of the maze layout and Z is the number of ghosts.
        - `evidences`: list of distances between
          pacman and ghosts at state x_{t}
          where 't' is the current time step
        - `pacman_position`: 2D coordinates position
          of pacman at state x_{t}
          where 't' is the current time step
        - `ghosts_eaten`: list of booleans indicating
          whether ghosts have been eaten or not

        Return:
        -------
        - A list of Z belief states at state x_{t}
          as N*M numpy mass probability matrices
          where N and M are respectively width and height
          of the maze layout and Z is the number of ghosts.

        N.B. : [0,0] is the bottom left corner of the maze.
               Matrices filled with zeros must be returned for eaten ghosts.
        """

        # XXX: Your code here

        w_max = self.walls.width
        h_max = self.walls.height
        walls = self.walls

        p_sum = self._get_transition_model(pacman_position)

        # On met à jour belief pour chaque ghost si il est en vie. Si il est mort, belief sera rempli de zéros
        for dg in range(0, len(ghosts_eaten)):
            new_belief = np.array(belief[dg], copy=True)
            if ghosts_eaten[dg] == 0:
                p1 = self._get_sensor_model(pacman_position, evidences[dg])
                for x in range(0, w_max):
                    for y in range(0, h_max):
                        belief_sum = 0

                        if walls[x][y] == 1:
                            belief_sum = 0

                        # On regarde si la case appartient au plateau
                        # Et on met à jour le belief grâce au transition model
                        if x-1 >= 0 and x+1 < w_max and y-1 >= 0 and y+1 < h_max:

                            if walls[x-1][y] == 0:
                                belief_sum = belief_sum + p_sum[x][y][x-1][y] * belief[dg][x-1][y]
                            if walls[x+1][y] == 0:
                                belief_sum = belief_sum + p_sum[x][y][x+1][y] * belief[dg][x+1][y]
                            if walls[x][y-1] == 0:
                                belief_sum = belief_sum + p_sum[x][y][x][y-1] * belief[dg][x][y-1]
                            if walls[x][y+1] == 0:
                                belief_sum = belief_sum + p_sum[x][y][x][y+1] * belief[dg][x][y+1]

                        # On pondère grâce au sensor model
                        p_f = p1[x][y] * belief_sum
                        new_belief[x][y] = p_f

                # On normalise le nouveau belief
                belief_total = sum(sum(new_belief))
                if belief_total != 0:
                    new_belief = new_belief/belief_total
                belief[dg] = np.array(new_belief, copy=True)
            else:
                dead = np.zeros((w_max, h_max))
                belief[dg] = np.array(dead, copy=True)

        # XXX: End of your code

        return belief

    def update_belief_state(self, evidences, pacman_position, ghosts_eaten):
        """
        Given a list of (noised) distances from pacman to ghosts,
        returns a list of belief states about ghosts positions

        Arguments:
        ----------
        - `evidences`: list of distances between
          pacman and ghosts at state x_{t}
          where 't' is the current time step
        - `pacman_position`: 2D coordinates position
          of pacman at state x_{t}
          where 't' is the current time step
        - `ghosts_eaten`: list of booleans indicating
          whether ghosts have been eaten or not

        Return:
        -------
        - A list of Z belief states at state x_{t}
          as N*M numpy mass probability matrices
          where N and M are respectively width and height
          of the maze layout and Z is the number of ghosts.

        XXX: DO NOT MODIFY THIS FUNCTION !!!
        Doing so will result in a 0 grade.
        """
        belief = self._get_updated_belief(self.beliefGhostStates, evidences,
                                          pacman_position, ghosts_eaten)
        self.beliefGhostStates = belief
        return belief

    def _get_evidence(self, state):
        """
        Computes noisy distances between pacman and ghosts.

        Arguments:
        ----------
        - `state`: The current game state s_t
                   where 't' is the current time step.
                   See FAQ and class `pacman.GameState`.


        Return:
        -------
        - A list of Z noised distances in real numbers
          where Z is the number of ghosts.

        XXX: DO NOT MODIFY THIS FUNCTION !!!
        Doing so will result in a 0 grade.
        """
        positions = state.getGhostPositions()
        pacman_position = state.getPacmanPosition()
        noisy_distances = []

        for pos in positions:
            true_distance = util.manhattanDistance(pos, pacman_position)
            noise = binom.rvs(self.n, self.p) - self.n*self.p
            noisy_distances.append(true_distance + noise)

        return noisy_distances

    def _record_metrics(self, belief_states, state):
        """
        Use this function to record your metrics
        related to true and belief states.
        Won't be part of specification grading.

        Arguments:
        ----------
        - `state`: The current game state s_t
                   where 't' is the current time step.
                   See FAQ and class `pacman.GameState`.
        - `belief_states`: A list of Z
           N*M numpy matrices of probabilities
           where N and M are respectively width and height
           of the maze layout and Z is the number of ghosts.

        N.B. : [0,0] is the bottom left corner of the maze
        """
        pass

    def get_action(self, state):
        """
        Given a pacman game state, returns a belief state.

        Arguments:
        ----------
        - `state`: the current game state.
                   See FAQ and class `pacman.GameState`.

        Return:
        -------
        - A belief state.
        """

        """
           XXX: DO NOT MODIFY THAT FUNCTION !!!
                Doing so will result in a 0 grade.
        """
        # Variables are specified in constructor.
        if self.beliefGhostStates is None:
            self.beliefGhostStates = state.getGhostBeliefStates()
        if self.walls is None:
            self.walls = state.getWalls()

        evidence = self._get_evidence(state)
        newBeliefStates = self.update_belief_state(evidence,
                                                   state.getPacmanPosition(),
                                                   state.data._eaten[1:])
        self._record_metrics(self.beliefGhostStates, state)

        return newBeliefStates, evidence
