# Initialize parameters and Q-values
alpha = 0.5
gamma = 1.0
Q = {
    's0': {'b': 0, 'c': 0},
    's1': {'b': 0, 'c': 0},
    's2': {'b': 0, 'c': 0},
    's3': {'b': 0, 'c': 0}
}
reward = {
    's0': {'b': 0, 'c': 0},
    's1': {'b': 0, 'c': 0},
    's2': {'b': 1, 'c': 1},
    's3': {'b': 0, 'c': 0}
}
transitions = {
    's0': {'b': 's1', 'c': 's2'},
    's1': {'b': 's0', 'c': 's0'},
    's2': {'b': 's3', 'c': 's3'},
    's3': {'b': 's3', 'c': 's3'}
}

# Simulate Q-learning for 100 encounters of s0
current_state = 's0'
encounters_s0 = 0
while encounters_s0 < 100:
    if current_state == 's0':
        encounters_s0 += 1
    # Select action based on current Q-values
    action = 'b' if Q[current_state]['b'] >= Q[current_state]['c'] else 'c'
    
    # Update Q-value based on taken action
    next_state = transitions[current_state][action]
    Q[current_state][action] = (1 - alpha) * Q[current_state][action] + alpha * (
        reward[current_state][action] + gamma * max(Q[next_state].values())
    )
    
    # Transition to the next state
    current_state = next_state
    
    # If we have completed 10 steps, reset to s0
    if encounters_s0 % 10 == 0:
        current_state = 's0'

# Return the Q-values and the selected action for s0 on the hundredth encounter
print(Q['s0'], action)
