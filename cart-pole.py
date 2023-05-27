import time
import gymnasium as gym
import random

qtable = []
for _ in range(420):
    qtable.append([[0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0]])


# , render_mode="human"
env = gym.make('CartPole-v1')
observation, info = env.reset(seed=42)
print("Baslangic")

epsilon = 0.725
eps_reduce_factor = 0.04
max_iteration = 1000000

ang_vel_up_limit = .5
ang_vel_low_limit = -.5


x_upper_limit = 1.4
x_lower_limit = -1.4

estart = time.time()
steps = []
for _ in range(max_iteration):

    if _ % 100000 == 0:
        epsilon -= eps_reduce_factor
        print("Episode =", _, ", epsilon = ", epsilon)

    # take random action
    if random.random() < epsilon:
        action = env.action_space.sample()
        steps.append([observation[2], action, observation[3], observation[0]])
    # use knowledge
    else:
        if observation[0] > x_upper_limit:
            if observation[3] > ang_vel_up_limit:
                if qtable[round(observation[2] * 1000 + 200)][2][6] > qtable[round(observation[2] * 1000 + 200)][2][7]:
                    action = 0
                else:
                    action = 1
            elif observation[3] > 0:
                if qtable[round(observation[2] * 1000 + 200)][2][4] > qtable[round(observation[2] * 1000 + 200)][2][5]:
                    action = 0
                else:
                    action = 1
            elif observation[3] > ang_vel_low_limit:
                if qtable[round(observation[2] * 1000 + 200)][2][2] > qtable[round(observation[2] * 1000 + 200)][2][3]:
                    action = 0
                else:
                    action = 1
            else:
                if qtable[round(observation[2] * 1000 + 200)][2][0] > qtable[round(observation[2] * 1000 + 200)][2][1]:
                    action = 0
                else:
                    action = 1
        elif observation[0] < x_lower_limit:
            if observation[3] > ang_vel_up_limit:
                if qtable[round(observation[2] * 1000 + 200)][0][6] > qtable[round(observation[2] * 1000 + 200)][0][7]:
                    action = 0
                else:
                    action = 1
            elif observation[3] > 0:
                if qtable[round(observation[2] * 1000 + 200)][0][4] > qtable[round(observation[2] * 1000 + 200)][0][5]:
                    action = 0
                else:
                    action = 1
            elif observation[3] > ang_vel_low_limit:
                if qtable[round(observation[2] * 1000 + 200)][0][2] > qtable[round(observation[2] * 1000 + 200)][0][3]:
                    action = 0
                else:
                    action = 1
            else:
                if qtable[round(observation[2] * 1000 + 200)][0][0] > qtable[round(observation[2] * 1000 + 200)][0][1]:
                    action = 0
                else:
                    action = 1
        else:
            if observation[3] > ang_vel_up_limit:
                if qtable[round(observation[2] * 1000 + 200)][1][6] > qtable[round(observation[2] * 1000 + 200)][1][7]:
                    action = 0
                else:
                    action = 1
            elif observation[3] > 0:
                if qtable[round(observation[2] * 1000 + 200)][1][4] > qtable[round(observation[2] * 1000 + 200)][1][5]:
                    action = 0
                else:
                    action = 1
            elif observation[3] > ang_vel_low_limit:
                if qtable[round(observation[2] * 1000 + 200)][1][2] > qtable[round(observation[2] * 1000 + 200)][1][3]:
                    action = 0
                else:
                    action = 1
            else:
                if qtable[round(observation[2] * 1000 + 200)][1][0] > qtable[round(observation[2] * 1000 + 200)][1][1]:
                    action = 0
                else:
                    action = 1
        steps.append([observation[2], action, observation[3], observation[0]])

    observation, reward, terminated, truncated, info = env.step(action)
    #  not (-1 < obs[2] < 1) or not (-2.4 < obs[0][0] < 2.4)
    if terminated or truncated:
        observation, info = env.reset()
        end = time.time()
        reward = end - estart
        estart = end
        reward_factor = 1
        punishment_factor = .8
        for i in range(round(len(steps))):
            # print(steps[-1-i])
            if steps[i][3] > x_upper_limit:
                if steps[i][2] > ang_vel_up_limit:
                    qtable[round(steps[i][0] * 1000 + 200)][2][steps[i][1] + 6] += reward * reward_factor
                elif steps[i][2] > 0:
                    qtable[round(steps[i][0] * 1000 + 200)][2][steps[i][1] + 4] += reward * reward_factor
                elif steps[i][2] > ang_vel_low_limit:
                    qtable[round(steps[i][0] * 1000 + 200)][2][steps[i][1] + 2] += reward * reward_factor
                else:
                    qtable[round(steps[i][0] * 1000 + 200)][2][steps[i][1]] += reward * reward_factor
            elif steps[i][3] < x_lower_limit:
                if steps[i][2] > ang_vel_up_limit:
                    qtable[round(steps[i][0] * 1000 + 200)][0][steps[i][1] + 6] += reward * reward_factor
                elif steps[i][2] > 0:
                    qtable[round(steps[i][0] * 1000 + 200)][0][steps[i][1] + 4] += reward * reward_factor
                elif steps[i][2] > ang_vel_low_limit:
                    qtable[round(steps[i][0] * 1000 + 200)][0][steps[i][1] + 2] += reward * reward_factor
                else:
                    qtable[round(steps[i][0] * 1000 + 200)][0][steps[i][1]] += reward * reward_factor
            else:
                if steps[i][2] > ang_vel_up_limit:
                    qtable[round(steps[i][0] * 1000 + 200)][1][steps[i][1] + 6] += reward * reward_factor
                elif steps[i][2] > 0:
                    qtable[round(steps[i][0] * 1000 + 200)][1][steps[i][1] + 4] += reward * reward_factor
                elif steps[i][2] > ang_vel_low_limit:
                    qtable[round(steps[i][0] * 1000 + 200)][1][steps[i][1] + 2] += reward * reward_factor
                else:
                    qtable[round(steps[i][0] * 1000 + 200)][1][steps[i][1]] += reward * reward_factor

            if steps[i][3] > x_upper_limit:
                if steps[-1 - i][2] > ang_vel_up_limit:
                    qtable[round(steps[-1 - i][0] * 1000 + 200)][2][steps[-1 - i][1] + 6] -= punishment_factor
                elif steps[-1 - i][2] > 0:
                    qtable[round(steps[-1 - i][0] * 1000 + 200)][2][steps[-1 - i][1] + 4] -= punishment_factor
                elif steps[-1 - i][2] > ang_vel_low_limit:
                    qtable[round(steps[-1 - i][0] * 1000 + 200)][2][steps[-1 - i][1] + 2] -= punishment_factor
                else:
                    qtable[round(steps[-1 - i][0] * 1000 + 200)][2][steps[-1 - i][1]] -= punishment_factor
            elif steps[i][3] < x_lower_limit:
                if steps[-1 - i][2] > ang_vel_up_limit:
                    qtable[round(steps[-1 - i][0] * 1000 + 200)][0][steps[-1 - i][1] + 6] -= punishment_factor
                elif steps[-1 - i][2] > 0:
                    qtable[round(steps[-1 - i][0] * 1000 + 200)][0][steps[-1 - i][1] + 4] -= punishment_factor
                elif steps[-1 - i][2] > ang_vel_low_limit:
                    qtable[round(steps[-1 - i][0] * 1000 + 200)][0][steps[-1 - i][1] + 2] -= punishment_factor
                else:
                    qtable[round(steps[-1 - i][0] * 1000 + 200)][0][steps[-1 - i][1]] -= punishment_factor
            else:
                if steps[-1 - i][2] > ang_vel_up_limit:
                    qtable[round(steps[-1 - i][0] * 1000 + 200)][1][steps[-1 - i][1] + 6] -= punishment_factor
                elif steps[-1 - i][2] > 0:
                    qtable[round(steps[-1 - i][0] * 1000 + 200)][1][steps[-1 - i][1] + 4] -= punishment_factor
                elif steps[-1 - i][2] > ang_vel_low_limit:
                    qtable[round(steps[-1 - i][0] * 1000 + 200)][1][steps[-1 - i][1] + 2] -= punishment_factor
                else:
                    qtable[round(steps[-1 - i][0] * 1000 + 200)][1][steps[-1 - i][1]] -= punishment_factor


            reward_factor *= 0.8*(epsilon)/0.69
            punishment_factor *= 0.4*(epsilon)/0.69

        steps.clear()

print("BITTI")
for i in range(420):
    print((i - 200) / 100, qtable[i])
    # print(qtable[i*2], " ", qtable[i*2+1])

env = gym.make('CartPole-v1', render_mode="human")
env.reset()
start = time.time()
counter = 0
times = []
while counter < 10:
    if observation[0] > x_upper_limit:
        if observation[3] > ang_vel_up_limit:
            if qtable[round(observation[2] * 1000 + 200)][2][6] > qtable[round(observation[2] * 1000 + 200)][2][7]:
                action = 0
            else:
                action = 1
        elif observation[3] > 0:
            if qtable[round(observation[2] * 1000 + 200)][2][4] > qtable[round(observation[2] * 1000 + 200)][2][5]:
                action = 0
            else:
                action = 1
        elif observation[3] > ang_vel_low_limit:
            if qtable[round(observation[2] * 1000 + 200)][2][2] > qtable[round(observation[2] * 1000 + 200)][2][3]:
                action = 0
            else:
                action = 1
        else:
            if qtable[round(observation[2] * 1000 + 200)][2][0] > qtable[round(observation[2] * 1000 + 200)][2][1]:
                action = 0
            else:
                action = 1
    elif observation[0] < x_lower_limit:
        if observation[3] > ang_vel_up_limit:
            if qtable[round(observation[2] * 1000 + 200)][0][6] > qtable[round(observation[2] * 1000 + 200)][0][7]:
                action = 0
            else:
                action = 1
        elif observation[3] > 0:
            if qtable[round(observation[2] * 1000 + 200)][0][4] > qtable[round(observation[2] * 1000 + 200)][0][5]:
                action = 0
            else:
                action = 1
        elif observation[3] > ang_vel_low_limit:
            if qtable[round(observation[2] * 1000 + 200)][0][2] > qtable[round(observation[2] * 1000 + 200)][0][3]:
                action = 0
            else:
                action = 1
        else:
            if qtable[round(observation[2] * 1000 + 200)][0][0] > qtable[round(observation[2] * 1000 + 200)][0][1]:
                action = 0
            else:
                action = 1
    else:
        if observation[3] > ang_vel_up_limit:
            if qtable[round(observation[2] * 1000 + 200)][1][6] > qtable[round(observation[2] * 1000 + 200)][1][7]:
                action = 0
            else:
                action = 1
        elif observation[3] > 0:
            if qtable[round(observation[2] * 1000 + 200)][1][4] > qtable[round(observation[2] * 1000 + 200)][1][5]:
                action = 0
            else:
                action = 1
        elif observation[3] > ang_vel_low_limit:
            if qtable[round(observation[2] * 1000 + 200)][1][2] > qtable[round(observation[2] * 1000 + 200)][1][3]:
                action = 0
            else:
                action = 1
        else:
            if qtable[round(observation[2] * 1000 + 200)][1][0] > qtable[round(observation[2] * 1000 + 200)][1][1]:
                action = 0
            else:
                action = 1
    observation, reward, terminated, truncated, info = env.step(action)
    #if terminated or truncated:
    if not (-0.20943951 < observation[2] < 0.20943951) or not (-2.4 < observation[0] < 2.4):
        observation, info = env.reset()
        end = time.time()
        counter += 1
        times.append(end - start)
        start = end
print(times)
print(sum(times) / len(times))
env.close()