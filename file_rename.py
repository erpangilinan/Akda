#!/usr/bin/env python

#Command line interface setup
import argparse
parser = argparse.ArgumentParser(description='Copies the file with a different name.')
parser.add_argument('infile', nargs='?', help='the name of the input file')
parser.add_argument('outfile', nargs='?', help='the new name of the file')
args = parser.parse_args()

#Get contents of infile
file_stream = open(args.infile, "r")
contents = file_stream.read()
file_stream.close()

#Create the new outfile
file_stream = open(args.outfile, "w+")
file_stream.write(contents)
file_stream.close()