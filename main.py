#!/bin/env python
import argparse
import re
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta

from graphics import graphics


regex = re.compile(r'((?P<years>\d+?)y)|((?P<months>\d+?)m)|((?P<days>\d+?)d)|((?P<hours>\d+?)h)')

parser = argparse.ArgumentParser(description="A graphics generator for stack overflow questions.")

parser.add_argument('tags', type=str, help="Tag or coma-separated list of tags to look for (ex.: c,python,javascript).")
parser.add_argument('-f', '--fromdate', type=str, help="First date of the range.")
parser.add_argument('-t', '--todate', type=str, help="Second date of the range.")
parser.add_argument(
    '-s', '--step', type=str,
    help="The step in the format nt where n is a number and t a type [h, d, m, y] (ex.: Two days=2d)"
)
parser.add_argument('-S', '--site',
    type=str, default='stackoverflow',
    help="The stackexchange platform to look into"
)


def parse_step(step: str):
    params = regex.match(step).groupdict()
    if not params:
        return None
    for p in params:
        params[p] = 0 if params[p] is None else int(params[p])
    return relativedelta(**params)


def parse_date(sd: str):
    try:
        return datetime.strptime(sd, '%Y-%m-%d')
    except ValueError:
        return datetime.strptime(sd, '%Y-%m-%d %H:%M:%S')

if __name__ == '__main__':
    args = parser.parse_args()

    graphics({
        'tags': args.tags.split(','),
        'from': parse_date(args.fromdate),
        'to': parse_date(args.todate),
        'step': parse_step(args.step),
        'site': args.site
    })
