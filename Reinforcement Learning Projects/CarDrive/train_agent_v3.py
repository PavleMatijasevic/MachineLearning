from stable_baselines3 import PPO
from stable_baselines3.common.monitor import Monitor
from stable_baselines3.common.env_checker import check_env
from car_env import CarEnv

# Kreiranje okruženja
env = CarEnv(render_mode=None)
check_env(env)  # Provera kompatibilnosti (pokreće se samo jednom)

# Monitoring za praćenje rezultata
env = Monitor(env)

# Kreiranje PPO modela
model = PPO(
    "MlpPolicy",
    env,
    verbose=1,
    tensorboard_log="./ppo_car_tensorboard_v3/"
)

# Treniranje
model.learn(total_timesteps=200_000)

# Čuvanje modela
model.save("ppo_car_agent_v3")
env.close()
