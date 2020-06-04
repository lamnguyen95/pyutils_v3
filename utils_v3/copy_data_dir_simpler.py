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

# internal
import utils_v3.archive


DIRECTION='''
This script copy directory along with its 1st-level files

e.g:
    $ $0 exp/source exp/target
'''


def get_args():
    parser = argparse.ArgumentParser(
        description=textwrap.dedent(DIRECTION),
        formatter_class=argparse.RawDescriptionHelpFormatter
    )

    parser.add_argument('source_dir', type=str,
                        help='''Source dir to be copied''')

    parser.add_argument('target_dir', type=str,
                        help='''Target dir to be recreated''')

    args = parser.parse_args()
    return args


def copy_data_dir_simpler(source_dir, target_dir):
    try:
        if not os.path.exists(source_dir):
            return False

        if not os.path.isdir(source_dir):
            return False

        if os.path.isdir(target_dir):
            utils_v3.archive(target_dir)

        shutil.copytree(source_dir, target_dir)

        logger.info(source_dir)
        logger.info(' |')
        logger.info(' | (copied)')
        logger.info(' |')
        logger.info(' v')
        logger.info(target_dir)

    except:
        logger.error(traceback.format_exc())
        return False 

    return True


def main():
    args = get_args()
    source_dir = args.source_dir
    target_dir = args.target_dir

    if not copy_data_dir_simpler(source_dir, target_dir):
        exit(1)

if __name__ == '__main__':
    main()
