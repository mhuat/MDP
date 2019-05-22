# Miguel Hernandez
# MDP 0.01
# CSC370
# Jan/20/2019

import numpy as ql

# Deliverable for Pt.1
print("The person off the street")

# ASCII Art&Title
print("""     
         __
 _(\    |@@|
(__/\__ \--/ __
   \___|----|  |   __
       \ }{ /\ )_ / _|
       /\__/\ \__O (__   *********Welcome to the Markov Decision Process Tool!*********
      (--/\--)    \__/
      _)(  )(_
     `---''---`)
     """)
# Summary of Program.
print("""\nThis program's purpose is to :\n
Understand the Markov Decision Process by allowing you to interact with an AI while playing a game. 
Display the thought process behind each decision. """)


# If we get to design the AI application, I'll:
# Create a Grid.
# Allow AI to:
# Render initial values.
# Store values.
# Use stored values to create a path.
# Store path and match the


def main():
    R = ql.matrix([[0, 0, 0, 0, 1, 0],
                   [0, 0, 0, 1, 0, 1]
                   [0, 0, 100, 1, 0, 0]
                   [0, 1, 1, 0, 1, 0]
                   [1, 0, 0, 1, 0, 0]
                   [0, 1, 0, 0, 0, 0]])
    print("The Variable R is a Type", type(R), "variable and holds the value", R, "End of Line...")


main()

# Notes GEt to "C" in A-F, starting from F in MDP.
# Q is the learning matrix which rewards are learned / stored
# Here we are creating a 6 by 6 matrix
Q = ql.matrix(ql.zeros([6, 6]))

# Gamma : penalty or uncertainty for learning
# if the value is 1, the rewards would be too high
# The system understands the scale
gamma = 0.8
# print("The Variable gamma is a type", type(gamma),"variable and holds the value", gamma,"End Of Line...")

# agent_s_state. The agent the name of the system calculating
# s is the state the agent is going from and s' the state it's going to
# States can be random or chosen as long as they are not determined
agent_s_state = 1


# print("The Variable agent_s_state is a type", type(agent_s_state),
# "variable and holds the value", agent_s_state, "End Of Line...")
# The possible "a" actions in a given state
# All possible actions in the environment


def possible_actions(state: object) -> object:
    print("The Variable state is a type", type(state), "variable and holds the value #", state, "End of Line...")
    current_state_row = R[state,]
    # print("The Variable current_state_row is a type", type(current_state_row),"# variable and holds the value",
    # current_state_row, "End of Line..." )
    possible_act: object = ql.where(current_state_row > 0)[1]
    # print("The Variable possible_act is a type", type(possible_act),"variable and holds the value", possible_act,
    # "End Of Line...")
    return possible_act


# Get available actions in the current state
PossibleAction = possible_actions(agent_s_state)


# Create a random choice given the tools below
def action_choice(available_actions_range):
    if sum(PossibleAction) > 0:
        next_action = int(ql.random.choice(PossibleAction, 1))
    if sum(PossibleAction) <= 0:
        next_action = int(ql.random.choice(5, 1))
    return next_action


# Sample next action to be performed
# Calling the action_choice function
action = action_choice(PossibleAction)


def reward(current_state, action, gamma):
    Max_State = ql.where(Q[action,] == ql.max(Q[action,]))[1]

    if Max_State.shape[0] > 1:
        Max_State = int(ql.random.choice(Max_State, size == 1))
    else:
        Max_State = int(Max_State)
    MaxValue = Q[action, Max_State]

    Q[current_state, action] = R[current_state, action] + gamme * MaxValue


reward(agent_s_state, action, gamma)
# Sets random
for i in range(50000):
    current_state = ql.random.randint(0, int(Q.shape[0]))
    PossibleAction = possible_actions(current_state)
    action = action_choice(PossibleAction)
    reward(current_state, action, gamma)

print("Q :")
print(Q)

# Norm of Q
print("Normed Q:")
print(Q / ql.max(Q) * 100)
