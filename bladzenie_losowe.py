import matplotlib.pyplot as plt
from random import choice


class RandomWalk():
    def __init__(self, num_pts=6000):
        self.num_pts = num_pts
        self.x_val = [0]
        self.y_val = [0]

    def walk(self):
        while len(self.x_val) < self.num_pts:
            x_dir = choice([-1, 1])
            x_dist = choice([0, 1, 2, 3, 4])
            y_dir = choice([-1, 1])
            y_dist = choice([0, 1, 2, 3, 4])
            x_step = x_dir * x_dist
            y_step = y_dir * y_dist
            if x_step == 0 and y_step == 0:
                continue
            x_next = self.x_val[-1] + x_step
            y_next = self.y_val[-1] + y_step
            self.x_val.append(x_next)
            self.y_val.append(y_next)


rw = RandomWalk()
rw.walk()
idx_pts = list(range(rw.num_pts))
plt.scatter(rw.x_val, rw.y_val, c=idx_pts, s=10)
plt.scatter(rw.x_val[0], rw.y_val[0], c='red', s=40)
plt.scatter(rw.x_val[-1], rw.y_val[-1], c='blue', s=40)
plt.show()