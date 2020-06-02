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


DIRECTION='''
This script archives directories/files

e.g:
    $ $0 exp/source
    $ tree exp
    exp
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
                        help='''All source items to be archived''')

    args = parser.parse_args()
    return args


def archive(source):
    try:
        timestamp = datetime.datetime.now().strftime('%Y_%m_%d-%H_%M_%S-%f')

        if not os.path.exists(source):
            logger.info('Skipping')
            return True

        source = os.path.abspath(source)

        target = os.path.join(
            Path(source).parent,
            '__archived__',
            timestamp + '-' + Path(source).name,
        )

        if os.path.exists(target):
            logger.info('Skipping')
            return True

        os.makedirs(Path(target).parent, exist_ok=True)
        shutil.move(source, target)
        logger.info('Archived: {} --moved-> {}'.format(source, target))

    except:
        logger.error(traceback.format_exc())
        return False

    return True


def main():
    args = get_args()
    Sources = args.sources

    for source in Sources:
        logger.info('Archiving: {}'.format(source))
        if not archive(source):
            exit(1)


if __name__ == '__main__':
    main()
