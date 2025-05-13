from car_env import CarEnv
import time

# Pokreni okruzenje sa prikazom
env = CarEnv(render_mode="human")

# Resetuj da generise novu stazu i centar
obs, _ = env.reset()
env.render()
# Pokazi stazu na ekranu 10 sekundi
time.sleep(10)

env.close()
