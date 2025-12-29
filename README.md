# Q-Learning from Scratch (Model-Free Reinforcement Learning)

This repository contains a **from-scratch, modular implementation of Q-learning**,  
an **off-policy, model-free reinforcement learning** algorithm, implemented on a custom  
**GridWorld environment built without any pre-made RL libraries**.

The focus of this project is **algorithmic clarity, correct temporal logic, and the on-/off-policy distinction**,  
not performance optimization or framework usage.

---

## Why this project

Many reinforcement learning examples:

- rely on Gym or other pre-built environments  
- hide the learning loop behind abstractions  
- obscure the difference between behavior policies and target policies  

This project does the opposite:

- the environment is implemented manually  
- the Q-learning update is written explicitly  
- the behavior policy is separated from value learning  
- the training loop shows the full `(s, a, r, s')` transition logic  

The goal is to **understand off-policy, model-free control from first principles**.

---

## What Q-learning is (core idea)

Q-learning is an **off-policy temporal-difference control algorithm**.  
It learns the value of **the optimal action**, independent of the action actually taken by the agent.

At each step, Q-learning updates the value of the current state–action pair using  
the **maximum action-value in the next state**, assuming greedy behavior in the future.

This single detail is the defining difference between **Q-learning and SARSA**.

---

## Q-learning update rule

For a transition:

\[
(s, a) \;\rightarrow\; r \;\rightarrow\; s'
\]

the Q-learning update is:

\[
Q(s, a) \leftarrow Q(s, a) + \alpha
\Big[
r + \gamma \max_{a'} Q(s', a') - Q(s, a)
\Big]
\]

where:

- \( \alpha \in (0, 1] \) is the learning rate  
- \( \gamma \in [0, 1) \) is the discount factor  
- \( \max_{a'} Q(s', a') \) represents the greedy action-value estimate in the next state  

This update is **off-policy** because the target assumes greedy behavior,  
regardless of how the action \( a \) was actually selected.
---
