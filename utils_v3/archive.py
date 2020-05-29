#!/usr/bin/env python3

# Copyright 2020 Lam Nguyen

import os, sys
import argparse, textwrap

import shutil
import datetime

import logging
logger = logging.getLogger(__name__)

import  coloredlogs
coloredlogs.install(logger=logger)


DIRECTION='''
This script runs archive a directory / a file
by adding timestamp suffix to its name

##  EXAMPLE(s):
    $ $0 /data/kaldi_data
    CWD    | /data
    Before | kaldi_data
    After  | [2020.20.02][09_30_00]__kaldi_data

    $ $0 /data/kaldi_data/utt2spk
    CWD    | /data/kaldi_data/
    Before | utt2spk
    After  | [2020.20.02][09_30_00]__utt2spk
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


def main():
    args = get_args()
    Sources = args.sources

    for source in Sources:
        time = datetime.datetime.now().strftime('%Y_%m_%d-%H_%M_%S-%f')
        logger.info('archiving source: {}'.format(source))
        logger.info('time: {}'.format(time))


if __name__ == '__main__':
    main()
