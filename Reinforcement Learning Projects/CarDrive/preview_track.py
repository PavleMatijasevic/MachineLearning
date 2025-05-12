from car_env import CarEnv
import time

# Pokreni okruženje sa prikazom
env = CarEnv(render_mode="human")

# Resetuj da generiše novu stazu i centar
obs, _ = env.reset()
env.render()
# Pokaži stazu na ekranu 5 sekundi
time.sleep(10)

env.close()
