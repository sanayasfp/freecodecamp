import copy
import random

class Hat:
  def __init__(self, **kwargs):
    if len(kwargs) == 0:
      raise ValueError('Hat must contain at least one ball')

    self.contents = []
    self.original_contents = copy.deepcopy(kwargs)
    self.fill_contents(**kwargs)

  def fill_contents(self, **kwargs):
    for color, quantity in kwargs.items():
      self.contents.extend([color] * quantity)

  def random_remove(self):
    return self.contents.pop(random.randint(0, len(self.contents) - 1))

  def draw(self, num_balls):
    balls = []

    if (num_balls > len(self.contents)):
      balls = self.contents
      self.contents = []
      return balls

    

    for _ in range(num_balls):
      balls.append(self.random_remove())

    return balls


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
  M = 0

  for _ in range(num_experiments):
    hat_copy = copy.deepcopy(hat)
    drawn_balls = hat_copy.draw(num_balls_drawn)
    E_OK = True

    for color, quantity in expected_balls.items():
      if drawn_balls.count(color) < quantity:
        E_OK = False
        break

    if E_OK:
      M += 1
  
  return M / num_experiments


if __name__ == "__main__":
  hat = Hat(black=6, red=4, green=3)
  probability = experiment(hat=hat,
                  expected_balls={"red":2,"green":1},
                  num_balls_drawn=5,
                  num_experiments=2000) 
  print("Probability:", probability) # Surrond 0.356
