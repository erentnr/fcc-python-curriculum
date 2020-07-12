import copy
import random
# Consider using the modules imported above.

class Hat:

    def __init__(self, **kwargs):
        self.contents = []
        for k,v in kwargs.items():
            for i in range(v):
                self.contents.append(k)

    def draw(self, num):
        drawn_balls = []
        rand_range = len(self.contents) - 1
        for i in range(num):
            random_num = random.randint(0, rand_range)
            drawn_balls.append(self.contents.pop(random_num))
            rand_range = rand_range - 1
        drawn_balls.sort()
        return drawn_balls

    def reset(self, hat_copy):
        self.contents.clear()
        self.contents.extend(hat_copy)


def compare_lists(a, b):
    for i in a:
        if i in b:
            b.remove(i)
    if len(b) == 0:
        return True
    return False

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):

    new_hat = copy.deepcopy(hat.contents)
    expected_balls_list = []
    N = num_experiments
    M = 0
    for k,v in expected_balls.items():
        for i in range(v):
            expected_balls_list.append(k)
    if num_balls_drawn < len(hat.contents):
        new_ball_list = copy.deepcopy(expected_balls_list)
        for j in range(num_experiments):
            drawn_balls = hat.draw(num_balls_drawn)
            compared = compare_lists(drawn_balls, new_ball_list)
            if compared:
                M = M + 1
            new_ball_list = copy.deepcopy(expected_balls_list)
            hat.reset(new_hat)
        probability = M/N
    else:
        probability = 1.0

    return probability
