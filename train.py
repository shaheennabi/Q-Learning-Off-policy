import numpy as np
from env import Environment
from agent import Agent
from policy import  epsilon_greedy_behaviour_policy


def train_qlearning(iterations, rows, cols, num_actions, epsilon, gamma, alpha):
    env = Environment(rows=rows, cols=cols)
    agent = Agent(rows, cols, num_actions)

    for _ in range(iterations):
        state = env.reset()
        done = False

        while not done:
            action = epsilon_greedy_behaviour_policy(agent.q_values[state], epsilon)
            next_state, reward, done = env.step(action)
            
            ## off-policy update -- target policy
            target = reward + gamma * np.max(agent.q_values[next_state])
            td_error = target - agent.q_values[state][action]
            agent.q_values[state][action] += td_error * alpha

            state = next_state

    return agent 
    


