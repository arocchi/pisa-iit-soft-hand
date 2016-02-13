import csv
import sys
import numpy as np
from scipy import signal as sig
from matplotlib import pyplot as plt


def parse_t(f):
    reader = csv.reader(f, delimiter=" ")
    t = False
    for row in reader:
        t_real = float(row[0])
        t_sim = float(row[1])
        row_array = np.array([[t_real, t_sim]])
        if type(t) is np.ndarray:
            t = np.vstack((t, row_array))
        else:
            t = row_array
    return t

fn = sys.argv[1]
f = open(fn, 'r')
t = parse_t(f)

plt.plot(t[1:, 1], sig.medfilt(t[1:, 0] - t[:-1, 0], 11))
plt.show()
