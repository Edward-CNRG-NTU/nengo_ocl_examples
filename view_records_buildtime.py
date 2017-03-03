#!/usr/bin/env python
import sys
try:
    import cPickle as pickle
except ImportError:
    import pickle
from collections import OrderedDict

by_name = OrderedDict()

for recfile in sys.argv[1:]:
    records = pickle.load(open(recfile, 'rb'))
    for rec in records:
        rec['filename'] = recfile
        by_name.setdefault(rec['name'], []).append(rec)

import matplotlib.pyplot as plt
nr = by_name.items()

# nr[1:1] = [('JavaNengo', None)]

for name, recs in nr:
    if name == 'JavaNengo':
        plt.plot([100, 200, 500], [9, 18, 45], '.-', markersize=30, label='JavaNengo')
        continue

    print(name.strip())
    if name.strip() == 'Tahiti':
        name = 'ATI Radeon HD 7970'
    if name.strip() == 'ref':
        name = 'NumPy Reference'
    if name.strip().startswith("Tesla"):
        name = 'NVidia ' + name.strip()
    if '5540' in name.strip():
        name = 'Intel Xeon E5540 @ 2.53GHz'
    if '2620' in name:
        name = 'Intel Xeon E5-2620 @ 2.00GHz'
    if 'Core' in name.strip():
        name = 'Intel Core i7-3770 @ 3.40GHz'

    oks = [rec for rec in recs if rec['status'] == 'ok']
    dims = [rec['dim'] for rec in oks]
    buildtimes = [rec['buildtime'] for rec in oks]
    filenames = [rec['filename'] for rec in oks]
    for dim, bt, fname in zip(dims, buildtimes, filenames):
        print('  %4d, %8.3f, %s' % (dim, bt, fname))
    plt.plot(dims, buildtimes, '.-', markersize=30, label=name.strip())
    # plt.semilogy(dims, buildtimes, '.-', markersize=30, label=name.strip())

plt.xlabel('n. dimensions convolved')
plt.ylabel('model build time (seconds)')
# plt.ylim(0, 20)
plt.legend(loc=2)
plt.show()
