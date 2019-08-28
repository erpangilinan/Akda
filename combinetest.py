#!/usr/bin/env python3

import argparse
parser = argparse.ArgumentParser(description='Summarizes several QUAST html files into a single outputfile.')
parser.add_argument('infile', nargs='+', help='the names of the input quast html files')
args = parser.parse_args()

for filename in args.infile:
	#Get contents of infile
	file_stream = open(filename, "r", encoding="utf8")
	contents = file_stream.read()
	file_stream.close()

	#Get Data
	contigs_enddigit = contents.rfind("],\"quality\":\"Equal\",\"isMain\":true,\"metricName\":\"# contigs\"}")
	Num_contigs = contents[(contigs_enddigit-100):contigs_enddigit]
	contigs_startdigit = Num_contigs.rfind("{\"values\":[")
	Num_contigs = Num_contigs[contigs_startdigit+11:]

	len_enddigit = contents.rfind("],\"quality\":\"More is better\",\"isMain\":true,\"metricName\":\"Total length\"}")
	Total_length = contents[(len_enddigit-100):len_enddigit]
	len_startdigit = Total_length.rfind("{\"values\":[")
	Total_length = Total_length[len_startdigit+11:]

	lar_enddigit = contents.rfind("],\"quality\":\"More is better\",\"isMain\":true,\"metricName\":\"Largest contig\"}")
	Largest_contig = contents[(lar_enddigit-100):lar_enddigit]
	lar_startdigit = Largest_contig.rfind("{\"values\":[")
	Largest_contig = Largest_contig[lar_startdigit+11:]

	N50_enddigit = contents.rfind("],\"quality\":\"More is better\",\"isMain\":false,\"metricName\":\"N50\"}")
	N50 = contents[(N50_enddigit-100):N50_enddigit]
	N50_startdigit = N50.rfind("{\"values\":[")
	N50 = N50[N50_startdigit+11:]

	print(filename[:-5], Num_contigs, Total_length, Largest_contig, N50)
