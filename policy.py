import numpy as np

def epsilon_greedy_behaviour_policy(q_values_of_that_state, epsilon):

    ## epsilon based---exploration
    if np.random.rand() < epsilon:
        return  np.random.randint(len(q_values_of_that_state))

    ## greedy-policy
    else:
        max_q = max(q_values_of_that_state)
        best_actions = np.where(q_values_of_that_state==max_q)[0]
        return np.random.choice(best_actions)
    
    