# -*- coding: utf-8 -*-

import sys

threshold = 10
message = '洗濯が完了しました。'

for line in sys.stdin:
	items = line.split()
	correl = float(items[0])
	if (correl < threshold):
		print(message)
