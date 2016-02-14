import numpy.linalg
import numpy.random


# by default, move the hand by 0.05m in a random direction. If the
# experiment is in the custom_pert dict, use that value
DEFAULT_SHAKING_PERT = 0.05
custom_pert = {}


def get_shake_perturbation():
    print "shaking object"
    shake_pert = DEFAULT_SHAKING_PERT

    random_dist = (numpy.random.random_sample(3) - 0.5)
    random_dist /= numpy.linalg.norm(random_dist)
    random_dist *= shake_pert

    return random_dist
