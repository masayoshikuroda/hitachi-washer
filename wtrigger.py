# -*- coding: utf-8 -*-

import sys
from argparse import ArgumentParser

usage = 'Usage: python {} [-t threshold]'
argparser = ArgumentParser(usage=usage)
argparser.add_argument('-t', '--threshold', type=float, dest='threshold', default=40,        help='trigger threshold')
argparser.add_argument('-m', '--message',   type=str,   dest='message',   default='Trigger', help='itrigger message')
args = argparser.parse_args()

threshold = args.threshold
message = args.message

print >> sys.stderr, 'threashhold: ' + str(threshold)
print >> sys.stderr, 'message;     ' + message
while True:
	line = sys.stdin.readline()
	items = line.split()
	correl = float(items[0])
	if (correl < threshold):
		print(message)
