from stable_baselines3 import PPO
from stable_baselines3.common.env_checker import check_env
from stable_baselines3.common.monitor import Monitor
from car_env import CarEnv
import gymnasium as gym

# Inicijalizacija okruzenja
env = CarEnv(render_mode=None)
check_env(env)  # Provera kompatibilnosti sa Gym interfejsom

# Wrap za pracenje rezultata
env = Monitor(env)

# Kreiranje PPO modela
model = PPO("MlpPolicy", env, verbose=1, tensorboard_log="./ppo_car_tensorboard/")

model.learn(total_timesteps=100_000)

model.save("ppo_car_agent")
env.close()
