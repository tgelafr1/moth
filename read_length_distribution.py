import numpy as np
import sys

import matplotlib as mpl
mpl.use('Agg')
import matplotlib.pyplot as plt

filename = sys.argv[1]

read_lengths = []

with open(filename) as f:
	for line in f:
		read_length, occurances = line.split(' ')
		read_length, occurances = int(read_length), int(occurances)
		read_lengths.append(read_length)

max_length = np.max(read_lengths)

lens = np.zeros(max_length + 1)

with open(filename) as f:
        for line in f:
                read_length, occurances = line.split(' ')
                read_length, occurances = int(read_length), int(occurances)
                lens[read_length] += occurances


bins = int(sys.argv[2])
max_read = int(sys.argv[3])

plt.hist(np.arange(len(lens)), bins=bins, weights=lens, range=(0, max_read))

max_read

plt.savefig(sys.argv[4])
