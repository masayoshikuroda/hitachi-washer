import sys
import math

freq_min = 220.0
freq_max = 3520.0

correl_file = 'wcorrel.pitch'

def load_pitch(fname):
	array = []
	for line in open(fname, 'r'):
		array.append(float(line))
	return array

def root_mean_square_error(a1, a2):
	ms = 0
	for i in range(len(a1)):
		ms += (a1[i] - a2[i]) ** 2
	return math.sqrt(ms/len(a1))


freq_correct = load_pitch(correl_file)
freq_sample = [0] * len(freq_correct)
print >> sys.stderr, 'loaded: ' + correl_file

for line in sys.stdin:
	items = line.split()
	freq = float(items[0])
	freq = freq if freq >= freq_min else 0
	freq = freq if freq <= freq_max else 0
	freq_sample.append(freq)
	freq_sample.pop(0)
	print(root_mean_square_error(freq_correct, freq_sample))