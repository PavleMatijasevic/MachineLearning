from stable_baselines3 import PPO
from car_env import CarEnv

env = CarEnv(render_mode="human")
model = PPO.load("ppo_car_agent")

obs, _ = env.reset()
done = False

while not done:
    action, _states = model.predict(obs, deterministic=True)
    obs, reward, terminated, truncated, _ = env.step(action)
    done = terminated or truncated
env.close()
