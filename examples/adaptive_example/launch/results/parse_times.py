import csv
import sys
import numpy as np
from scipy import signal as sig
from matplotlib import pyplot as plt


def parse_mean(t, t_min, t_max):
    t_other = t[t[:, 1] < t_min]
    t_contact = t[t[:, 1] >= t_min]
    t_contact = t_contact[t_contact[:, 1] <= t_max]
    t_contact_v = t_contact[1:, 0] - t_contact[:-1, 0]
    t_other_v = t_other[1:, 0] - t_other[:-1, 0]
    return (np.mean(t_contact_v), np.mean(t_other_v))


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

if(len(sys.argv) == 4):
    t_min = float(sys.argv[2])
    t_max = float(sys.argv[3])
    (mean_contact, mean_other) = parse_mean(t, t_min, t_max)
    print "Mean of Processing Time during Contact:", mean_contact
    print "Mean of Processing Time, not in Contact:", mean_other

plt.plot(t[1:, 1], sig.medfilt(t[1:, 0] - t[:-1, 0], 11))
plt.show()
