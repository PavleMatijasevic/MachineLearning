from stable_baselines3 import PPO
from car_env import CarEnv
import matplotlib.pyplot as plt

# Učitaj trenirani model
model = PPO.load("ppo_car_agent_v4")

# Inicijalizuj okruženje bez prikaza
env = CarEnv(render_mode=None)

obs, _ = env.reset()
done = False

# Beleži pozicije auta i nagrade
positions = []
rewards = []

while not done:
    action, _states = model.predict(obs, deterministic=True)
    obs, reward, terminated, truncated, _ = env.step(action)
    positions.append((env.car_x, env.car_y))
    rewards.append(reward)
    done = terminated or truncated

env.close()

# Prikazivanje putanje kretanja
x_coords = [p[0] for p in positions]
y_coords = [p[1] for p in positions]

plt.figure(figsize=(8, 6))
plt.plot(x_coords, y_coords, marker='o', linewidth=1, markersize=2, label="Putanja auta")
plt.gca().invert_yaxis()  # PyGame ima (0,0) gore-levo, kao i ovde
plt.title("Putanja kretanja auta kroz stazu")
plt.xlabel("X")
plt.ylabel("Y")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()
