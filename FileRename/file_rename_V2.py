#!/usr/bin/env python

#Command line interface setup
import argparse
parser = argparse.ArgumentParser(description='Copies the file with a different name.')
parser.add_argument('infile', nargs='?', help='the name of the input file')
parser.add_argument('outfile', nargs='?', help='the new name of the file')
args = parser.parse_args()

#Changes name of the file
import os
os.rename(args.infile, args.outfile)