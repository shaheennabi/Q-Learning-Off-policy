import numpy as np



class Agent:
    def __init__(self, rows, cols, num_actions):
        self.rows = rows
        self.cols = cols
        self.num_actions = num_actions
        self.q_values = np.zeros((rows, cols, num_actions))


    







