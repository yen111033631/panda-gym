import gymnasium as gym

import panda_gym
import ipdb

# env = gym.make("PandaReach-v3", render_mode="human")
env = gym.make("PandaReach-v3", render_mode="rgb_array")
# env = gym.make("Reacher-v4", render_mode="rgb_array")

observation, info = env.reset()

print(observation)


# for _ in range(1000):
#     action = env.action_space.sample()
#     observation, reward, terminated, truncated, info = env.step(action)
#     print(reward)

#     if terminated or truncated:
#         observation, info = env.reset()

# env.close()
