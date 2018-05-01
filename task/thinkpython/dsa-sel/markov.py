import sys
import string
import random


suffix_dict = {} 
pre = ()          


def process_file(filename, order=2):

    fp = open(filename)
    skip__header(fp)

    for line in fp:
        for word in line.rstrip().split():
            process_word(word, order)


def skip_header(fp):
    for line in fp:
        if line.startswith('*END*THE SMALL PRINT!'):
            break


def process_word(word, order=2):
    global pre
    if len(pre) < order:
        pre = pre + (word,)
        return

    try:
        suffix_dict[pre].append(word)
    except KeyError:

        suffix_dict[pre] = [word]

    pre = shift(pre, word)


def random_text(n=100):
    start = random.choice(suffix_dict.keys())
    
    for i in range(n):
        suffixes = suffix_dict.get(start, None)
        if suffixes == None:
            random_text(n-i)
            return

        word = random.choice(suffixes)
        print word,
        start = shift(start, word)


def shift(t, word):
    return t[1:] + (word,)


def main(name, filename='', n=100, order=2, *args):
    try:
        n = int(n)
        order = int(order)
    except:
        print 'Usage: randomtext.py filename [# of words] [prefix length]'
    else: 
        process_file(filename, order)
        random_text(n)


if __name__ == '__main__':
    main(*sys.argv)
