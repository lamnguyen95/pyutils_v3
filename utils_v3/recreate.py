#!/usr/bin/env python3

# Copyright 2020 Lam Nguyen

import os, sys
import argparse, textwrap
import traceback

import shutil
from pathlib import Path
import datetime

import logging
logger = logging.getLogger(__name__)

import coloredlogs
coloredlogs.install(logger=logger)

import utils_v3.archive


DIRECTION='''
This script recreate directories/files
while keeping an archived version of each of them.

e.g:
    $ $0 exp/source
    $ tree exp
    exp
    |-- source
    |-- __archived__
    |   |-- 2020_06_02-03_09_26-615104-source
    ..
'''


def get_args():
    parser = argparse.ArgumentParser(
        description=textwrap.dedent(DIRECTION),
        formatter_class=argparse.RawDescriptionHelpFormatter
    )

    parser.add_argument('sources', type=str, nargs='+',
                        help='''All source items to be recreated''')

    args = parser.parse_args()
    return args


def recreate(source):

    try:
        if os.path.exists(source):
            if not os.path.isdir(source):
                return False

        utils_v3.archive(source)
        os.makedirs(source, exist_ok=False)
        logger.info('Recreated: {}'.format(source))

    except:
        logger.error(traceback.format_exc())
        return False

    return True


def main():
    args = get_args()
    Sources = args.sources

    for source in Sources:
        logger.info('Recreating: {}'.format(source))
        if not recreate(source):
            exit(1)


if __name__ == '__main__':
    main()
