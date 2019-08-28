#!/usr/bin/env python3

import argparse
parser = argparse.ArgumentParser(description='Summarizes several QUAST html files into a single outputfile.')
parser.add_argument('infile', nargs='+', help='the names of the input quast html files')
args = parser.parse_args()

class Result(): #Result Block
	"""Each Result will have the following attributes:
		Name, Num_contigs, Total_length, Largest_contig, N50, GC_Content"""
		
	Coalition = [] #Repository of all Result objects
		
	def __init__(self, Name, Num_contigs, Total_length, Largest_contig, N50):
		#Primary Stats
		self.Name = Name
		self.Num_contigs = Num_contigs
		self.Total_length = Total_length
		self.Largest_contig = Largest_contig
		self.N50 = N50
		
		Result.Coalition.append(self)
		
	def __str__(self):
		return self.Name

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
	
	data = Result(filename[:-5], Num_contigs, Total_length, Largest_contig, N50)

finalout = ""

for data in Result.Coalition:
	finalout = finalout+data.Name+"\t"+data.Num_contigs+"\t"+data.Total_length+"\t"+data.Largest_contig+"\t"+data.N50+"\n"

#Create the new outfile
file_stream = open("result.txt", "w+", encoding="utf8")
file_stream.write(finalout)
file_stream.close()