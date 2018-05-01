import sys
import string

import matplotlib.pyplot as pyplot

from analyze_book import *


def rank_freq(hist):
    freqs = hist.values()
    freqs.sort(reverse=True)
    rf = [(r+1, f) for r, f in enumerate(freqs)]
    return rf


def print_ranks(hist):
    for r, f in rank_freq(hist):
        print r, f


def plot_ranks(hist, scale='log'):
    t = rank_freq(hist)
    rs, fs = zip(*t)

    pyplot.clf()
    pyplot.xscale(scale)
    pyplot.yscale(scale)
    pyplot.title('Zipf plot')
    pyplot.xlabel('rank')
    pyplot.ylabel('frequency')
    pyplot.plot(rs, fs, 'r-')
    pyplot.show()


def main(name, filename='emma.txt', flag='plot', *args):
    hist = process_file(filename, skip_header=True)

    if flag == 'print':
        print_ranks(hist)
    elif flag == 'plot':
        plot_ranks(hist)
    else:
        print 'Usage: zipf.py filename [print|plot]'


if __name__ == '__main__':
    main(*sys.argv)
