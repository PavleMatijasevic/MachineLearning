from stable_baselines3 import PPO
from car_env import CarEnv

# Učitaj trenirani model
model = PPO.load("ppo_car_agent_v4")

# Inicijalizuj okruženje sa prikazom
env = CarEnv(render_mode="human")

obs, _ = env.reset()
done = False

while not done:
    action, _states = model.predict(obs, deterministic=True)
    obs, reward, terminated, truncated, _ = env.step(action)
    done = terminated or truncated

env.close()
