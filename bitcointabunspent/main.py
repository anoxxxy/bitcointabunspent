import sys
import argparse
import json
from decimal import Decimal


def main(args=sys.argv[1:]):
    """
    Tabulate listunspent to show balance per address.
    """
    opts = parse_args(args)

    with sys.stdin as f:
        tab = tabulate_input(f)

    rows = [(addr, total, utxos) for (addr, (total, utxos)) in tab.iteritems()]
    rows.sort(key={
        'address': lambda t: t[0],
        'amount': lambda t: t[1],
        'utxos': lambda t: t[2],
    }[opts.SORT])

    if opts.JSON:
        display_json(rows)
    else:
        display_text(rows)


def parse_args(args):
    p = argparse.ArgumentParser(description=main.__doc__)
    p.add_argument(
        '--json',
        dest='JSON',
        action='store_true',
        default=False,
        help='Display output in JSON format rather than plain text.',
    )
    p.add_argument(
        '--sort',
        dest='SORT',
        choices=['amount', 'address', 'utxos'],
        default='amount',
        help='Sort output by the given value.',
    )
    return p.parse_args(args)


def tabulate_input(f):
    unspents = json.load(f, parse_float=Decimal)

    tab = {}  # { addr -> (total, utxos) }
    for unspent in unspents:
        addr = unspent['address']
        amount = unspent['amount']
        (total, utxos) = tab.get(addr, (Decimal(0), 0))
        tab[addr] = (total + amount, utxos + 1)
    return tab


def display_json(rows):
    json.dump(
        rows,
        sys.stdout,
        indent=2,
    )


def display_text(rows):
    total = Decimal(0)
    for (addr, amount, utxos) in rows:
        print '{} {} ({})'.format(addr, amount, utxos)
        total += amount
    print 'Total: {}'.format(total)
