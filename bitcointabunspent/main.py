#!/usr/bin/env python

import sys
import argparse


def main(args=sys.argv[1:]):
    """
    Tabulate listunspent to show balance per address.
    """
    opts = parse_args(args)
    raise NotImplementedError('main')


def parse_args(args):
    p = argparse.ArgumentParser(description=main.__doc__)
    return p.parse_args(args)


if __name__ == '__main__':
    main()
