from stable_baselines3 import PPO
from stable_baselines3.common.monitor import Monitor
from stable_baselines3.common.env_checker import check_env
from car_env import CarEnv

# Kreiranje okruzenja
env = CarEnv(render_mode=None)
check_env(env)

# Monitoring okruzenja
env = Monitor(env)

# PPO model
model = PPO(
    "MlpPolicy",
    env,
    verbose=1,
    tensorboard_log="./ppo_car_tensorboard_v4/"
)

# Treniranje
model.learn(total_timesteps=250_000)

# vanje modelaCu
model.save("ppo_car_agent_v4")
env.close()
