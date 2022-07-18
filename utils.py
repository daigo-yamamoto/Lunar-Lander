import numpy as np

def reward_engineering(state, action, reward, next_state, done):
    """
    Makes reward engineering to allow faster training in the Mountain Car environment.

    :param state: state.
    :type state: NumPy array with dimension (1, 2).
    :param action: action.
    :type action: int.
    :param reward: original reward.
    :type reward: float.
    :param next_state: next state.
    :type next_state: NumPy array with dimension (1, 2).
    :param done: if the simulation is over after this experience.
    :type done: bool.
    :return: modified reward for faster training.
    :rtype: float.
    """
    dt = state[0] ** 2 + state[1] ** 2
    dt = np.sqrt(dt)
    dt1 = next_state[0] ** 2 + next_state[1] ** 2
    dt1 = np.sqrt(dt1)
    vt = state[2] ** 2 + state[3] ** 2
    vt = np.sqrt(vt)
    vt1 = next_state[2] ** 2 + next_state[3] ** 2
    vt1 = np.sqrt(vt1)
    omegat = state[5]
    omegat1 = next_state[5]
    algum_toque = state[6] or state[7]
    toque_junto = state[6] and state[7]
    reward += 2*(dt - dt1) + 2*(vt - vt1) - 2*(np.abs(omegat - omegat1)) + 10*toque_junto + 2*algum_toque
    if done:
        reward += 100

    return reward


