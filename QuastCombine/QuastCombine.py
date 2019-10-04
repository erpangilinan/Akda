#!/usr/bin/env python3

class Result(): #Result Objects
	"""Each Result will have the following attributes:
		Default - Name, Num_contigs, Total_length, Largest_contig, N50, GCgraph
		Expanded - TL0, TL1k, TL5k, TL10k, TL25k, TL50k, NC0, NC1k, NC5k, NC10k, NC25k, NC50k, N75, L50, L75, GCper, graphNx, graphCL"""
		
	Coalition = [] #Repository of all Result objects
		
	def __init__(self, Name,
				Num_contigs, NC0, NC1k, NC5k, NC10k, NC25k, NC50k,
				Total_length, TL0, TL1k, TL5k, TL10k, TL25k, TL50k,
				Largest_contig, N50, N75, L50, L75, GCper,
				graphGC, graphNx, graphCL):
					
		#Primary Stats
		self.Name = Name
		self.Num_contigs = Num_contigs
		self.NC0 = NC0
		self.NC1k = NC1k
		self.NC5k = NC5k
		self.NC10k = NC10k
		self.NC25k = NC25k
		self.NC50k = NC50k
		self.Total_length = Total_length
		self.TL0 = TL0
		self.TL1k = TL1k
		self.TL5k = TL5k
		self.TL10k = TL10k
		self.TL25k = TL25k
		self.TL50k = TL50k
		self.Largest_contig = Largest_contig
		self.N50 = N50
		self.N75 = N75
		self.L50 = L50
		self.L75 = L75
		self.GCper = GCper
		self.graphGC = graphGC
		self.graphNx = graphNx
		self.graphCL = graphCL
		
		self.rank = 0
		
		self.N50tier = False
		self.L50tier = False
		self.Lengthtier = 0
		
		Result.Coalition.append(self)
		
	def __str__(self):
		return self.Name

def DataCollect(filename): #Data Mining Block
	"""Collects and collates data from Quast html file into Results objects"""
	###Get contents of infile
	file_stream = open(filename, "r", encoding="utf8")
	contents = file_stream.read()
	file_stream.close()

	###Get Data
	Num_contigs = StandardStringfind(contents, 100, "{\"values\":[", "],\"quality\":\"Equal\",\"isMain\":true,\"metricName\":\"# contigs\"}")
	NC0 = StandardStringfind(contents, 100, "{\"values\":[", "],\"quality\":\"Equal\",\"isMain\":false,\"metricName\":\"# contigs (>= 0 bp)\"}")
	NC1k = StandardStringfind(contents, 100, "{\"values\":[", "],\"quality\":\"Equal\",\"isMain\":false,\"metricName\":\"# contigs (>= 1000 bp)\"}")
	NC5k = StandardStringfind(contents, 100, "{\"values\":[", "],\"quality\":\"Equal\",\"isMain\":false,\"metricName\":\"# contigs (>= 5000 bp)\"}")
	NC10k = StandardStringfind(contents, 100, "{\"values\":[", "],\"quality\":\"Equal\",\"isMain\":false,\"metricName\":\"# contigs (>= 10000 bp)\"}")
	NC25k = StandardStringfind(contents, 100, "{\"values\":[", "],\"quality\":\"Equal\",\"isMain\":false,\"metricName\":\"# contigs (>= 25000 bp)\"}")
	NC50k = StandardStringfind(contents, 100, "{\"values\":[", "],\"quality\":\"Equal\",\"isMain\":false,\"metricName\":\"# contigs (>= 50000 bp)\"}")
	Total_length = StandardStringfind(contents, 100, "{\"values\":[", "],\"quality\":\"More is better\",\"isMain\":true,\"metricName\":\"Total length\"}")
	TL0 = StandardStringfind(contents, 100, "{\"values\":[", "],\"quality\":\"More is better\",\"isMain\":false,\"metricName\":\"Total length (>= 0 bp)\"}")
	TL1k = StandardStringfind(contents, 100, "{\"values\":[", "],\"quality\":\"More is better\",\"isMain\":true,\"metricName\":\"Total length (>= 1000 bp)\"}")
	TL5k = StandardStringfind(contents, 100, "{\"values\":[", "],\"quality\":\"More is better\",\"isMain\":false,\"metricName\":\"Total length (>= 5000 bp)\"}")
	TL10k = StandardStringfind(contents, 100, "{\"values\":[", "],\"quality\":\"More is better\",\"isMain\":true,\"metricName\":\"Total length (>= 10000 bp)\"}")
	TL25k = StandardStringfind(contents, 100, "{\"values\":[", "],\"quality\":\"More is better\",\"isMain\":false,\"metricName\":\"Total length (>= 25000 bp)\"}")
	TL50k = StandardStringfind(contents, 100, "{\"values\":[", "],\"quality\":\"More is better\",\"isMain\":true,\"metricName\":\"Total length (>= 50000 bp)\"}")
	Largest_contig = StandardStringfind(contents, 100, "{\"values\":[", "],\"quality\":\"More is better\",\"isMain\":true,\"metricName\":\"Largest contig\"}")
	N50 = StandardStringfind(contents, 100, "{\"values\":[", "],\"quality\":\"More is better\",\"isMain\":false,\"metricName\":\"N50\"}")
	N75 = StandardStringfind(contents, 100, "{\"values\":[", "],\"quality\":\"More is better\",\"isMain\":false,\"metricName\":\"N75\"}")
	L50 = StandardStringfind(contents, 100, "{\"values\":[", "],\"quality\":\"Less is better\",\"isMain\":false,\"metricName\":\"L50\"}")
	L75 = StandardStringfind(contents, 100, "{\"values\":[", "],\"quality\":\"Less is better\",\"isMain\":false,\"metricName\":\"L75\"}")
	GCper = StandardStringfind(contents, 100, "{\"values\":[\"", "\"],\"quality\":\"Equal\",\"isMain\":false,\"metricName\":\"GC (%)\"}")
	
	graphGC = StandardStringfind(contents, 1000, ".0,100.0],[", "]]],\"reference_index\":null,\"list_of_GC_contigs_distributions\":[[[")
	graphGC = StringtoIntList(graphGC, ',')
	graphGC = [graphGC, [float(x) for x in range(101)]]
	
	graphNx = StandardStringfind(contents, 1000000, "}\n            </div>\n            <div id=\'coord-nx-json\'>\n                {\"coord_y\":[[", "]}\n            </div>\n            <div id=\'coord-ngx-json\'>")
	graphNx = NumSpliter(CutEnd(graphNx, "]],\"filenames\":[\""), "]],\"coord_x\":[[")
	
	graphCL = StandardStringfind(contents, 1000000, "<div id=\"contigs-lengths-json\">\n                {\"lists_of_lengths\":[[", "]}\n            </div>\n            <div id=\'assemblies-lengths-json\'>")
	graphCL = StringtoIntList(CutEnd(graphCL, "]],\"filenames\":[\""), ",")
	graphCL = ListCulmination(graphCL)
	graphCL.insert(0, 0)
	graphCL = [graphCL, [x for x in range(len(graphCL))]]
	
	#store data in object
	data = Result(filename[:-5], Num_contigs, NC0, NC1k, NC5k, NC10k, NC25k, NC50k, Total_length, TL0, TL1k, TL5k, TL10k, TL25k, TL50k, Largest_contig, N50, N75, L50, L75, GCper, graphGC, graphNx, graphCL)
def StandardStringfind(fullstring, expectedsize, frontbracket, backbracket):
	"""Finds a substring from a larger string based on only the pre- and post- substrings"""
	data_enddigit = fullstring.rfind(backbracket)
	data = fullstring[(data_enddigit-expectedsize):data_enddigit]
	data_startdigit = data.rfind(frontbracket)
	data = data[data_startdigit+len(frontbracket):]
	
	return data
def StringtoIntList(rawstring, deliminator):
	"""Converts a string of numbers into a list of the corresponding integers"""

	rawlist = rawstring.split(deliminator)
	endlist = []
	for num in rawlist:
		num = int(num)
		endlist.append(num)
		
	return endlist
def StringtoFloatList(rawstring, deliminator):
	"""Converts a string of numbers into a list of the corresponding floats"""

	rawlist = rawstring.split(deliminator)
	endlist = []
	for num in rawlist:
		num = float(num)
		endlist.append(num)
		
	return endlist
def CutEnd(rawstring, remove):
	"""Removes the unwanted end of a string"""
	
	rawstring_enddigit = rawstring.rfind(remove)
	rawstring = rawstring[:rawstring_enddigit]
	
	return rawstring
def NumSpliter(rawstring, midstring):
	"""Seperates a string into two seperate substrings & converts them to the corresponding number type eg.(X & Y)"""
	
	substringlist = rawstring.split(midstring)
	
	counter = 0
	for substring in substringlist:
		if substring.count(".") > 0:
			holder = StringtoFloatList(substring, ",")
		else:
			holder = StringtoIntList(substring, ",")
			
		substringlist[counter] = holder
		counter += 1
		
	return substringlist
def ListCulmination(rawlist):
	"""Converts a list of integers to a culmination list (every element is replaced by the summation of that element and the former ones)"""
	holder = []
	total = 0
	for number in rawlist:
		total = total + number
		holder.append(total)
		
	return holder

def DataOut(): #Results Releasing Block
	"""Creates the collated results files"""
	#Set the parameters of the output
	settings = args.result
	Tablecontents = []
	Graphcontents = []
	if settings == "all":
		Tablecontents = ["Name", "Num_contigs", "NC0", "NC1k", "NC5k", "NC10k", "NC25k", "NC50k", "Total_length", "TL0", "TL1k", "TL5k", "TL10k", "TL25k", "TL50k", "Largest_contig",  "N50", "N75", "L50", "L75", "GCper"]
		Graphcontents = ["graphGC", "graphNx", "graphCL"]
	elif settings == "table":
		Tablecontents = ["Name", "Num_contigs", "NC0", "NC1k", "NC5k", "NC10k", "NC25k", "NC50k", "Total_length", "TL0", "TL1k", "TL5k", "TL10k", "TL25k", "TL50k", "Largest_contig",  "N50", "N75", "L50", "L75", "GCper"]
	elif settings == "graph":
		Graphcontents = ["graphGC", "graphNx", "graphCL"]
	elif settings == "default":
		Tablecontents = ["Name", "Num_contigs", "Total_length", "Largest_contig", "N50", "L50"]
		Graphcontents = ["graphGC"]
	
	if len(Tablecontents) != 0:
		CreateTable(Tablecontents)
	if len(Graphcontents) != 0:
		CreateGraph(Graphcontents)
def CreateTable(Tablecontents):
	"""Creates a table containing the parameters designated by user, and fromats it according to the length of the data"""	
	##Formatting table
	#find length of 1st column (parameter names) and creating the spacing format
	col1tab = 0
	for row in Tablecontents:
		
		row = ParameterNameConversion(row)
		
		if len(row) > col1tab:
			col1tab = len(row)
	formatstring = "a:<"+str(col1tab+1)+"b"

	#find length of other columns (length of longest data out) and creating the spacing format
	for data in Result.Coalition:
		tablength = 0
		for row in Tablecontents:
			if len(str(getattr(data, row))) > tablength:
				tablength = len(str(getattr(data, row)))
		formatstring = formatstring + "a:<"+str(tablength+4)+"b"
	formatstring = formatstring.replace("a","{")
	formatstring = formatstring.replace("b","}")
	
	##Creating the table
	#consolidating the data into a string
	finalout = ""
	for row in Tablecontents:
		outdata = []
		for data in Result.Coalition:
			outdata.append(getattr(data, row))
		
		renamerow = ParameterNameConversion(row)
		
		if args.quality != "none":
			finalout = CalcQuality(row, renamerow, finalout, formatstring, outdata)
		else:
			finalout = finalout + formatstring.format(renamerow, *outdata) + "\n"
	
	#Append Definitions to end if -d option is called
	if args.define:
		finalout = AppendDefinitions(Tablecontents, finalout)
	
	#Append calculated most optimal assembly if -q option is called
	if args.quality == "best" or args.quality == "rank":
		score = []
		names = []
		for data in Result.Coalition:
			names.append(data.Name)
			score.append(data.rank)
		
		out = [x for _,x in sorted(zip(score,names))]
		
		ranks = []
		if args.quality == "best":
			out.reverse()
			for assembler in names:
				ranks.append(out.index(assembler)+1)
			finalout = finalout + "\n" + formatstring.format("# of bests:", *score) + "\tMore is better\n"
			finalout = finalout + formatstring.format("Ranking:", *ranks) + "\n"
			finalout = finalout+"\nCalculated optimal assembly: "+out[0]+"\n"
		elif args.quality == "rank":
			for assembler in names:
				ranks.append(out.index(assembler)+1)
			finalout = finalout + "\n" + formatstring.format("Rank total:", *score) + "\tLess is better\n"
			finalout = finalout + formatstring.format("Ranking:", *ranks) + "\n"
			finalout = finalout+"\nCalculated optimal assembly: "+out[0]+"\n"
	elif args.quality == "tier":
		finalout = finalout +"\n"
		
		finalists = []
		winner = ""
		for data in Result.Coalition:
			if data.N50tier == True:
				finalout = finalout + "Highest N50: "+ str(data.Name) +"\n"
				if data not in finalists:
					finalists.append(data)
			if data.L50tier == True:
				finalout = finalout + "Lowest L50: "+ str(data.Name) +"\n"
				if data not in finalists:
					finalists.append(data)
					
		if len(finalists) == 1:
			winner = finalists[0]
			finalout = finalout+"Calculated optimal assembly: "+winner.Name+"\n"
		else:
			score = []
			names = []
			for data in finalists:
				names.append(data.Name)
				score.append(data.Total_length)
			
			out = [x for _,x in sorted(zip(score,names))]
			
			for data in Result.Coalition:
				if data.Name == out[-1]:
					winner = data
			finalout = finalout+"\nLongest Total_Length among these: "+winner.Name+"\nCalculated optimal assembly: "+winner.Name+"\n"
		if args.length != "":
			finalout = finalout+"Warning: "+winner.Name+" length is "+str(abs(float(args.length) - float(winner.Total_length)))+" from the expected"
	
	#create output text file based on the string
	file_stream = open("result.txt", "w+", encoding="utf8")
	file_stream.write(finalout)
	file_stream.close()
def ParameterNameConversion(parameter):
	"""conversion of parameter names into a more readable form for table"""
	
	parameter = parameter.replace("TL","Total_length >= ")
	parameter = parameter.replace("NC","Num_contigs >= ")
	parameter = parameter.replace("GCper","GC (%)")
	
	return parameter
def CalcQuality(parameter, title, finalout, formatstring, outdata):
	"""Appends the definition of high quality per parameter in the table to the end of each row and marks either the best performer or ranks all, per parameter"""
	
	#Prepare values for comparisson
	if args.mulcon != "":
		mulcon = []
		for element in args.mulcon:
			if element[-1] == ",":
				element = element[:-1]
			element = element.split(",")
			for value in element:
				value = value.replace(",","")
				mulcon.append(value)
		for num in range(6 - len(mulcon)):
			mulcon.append("")
	
	#Determine how to check for quality
	if str(DefinitionOfQuality(parameter)) == "Closer to expected":
		if parameter == "GCper" and args.gcper != "" and IsFloat(args.gcper):
			sorted = AbsoluteDistanceRank(ListofStringstoFloatList(outdata), float(args.gcper)) #Closest to Furthest
		elif parameter == "Num_contigs" and args.contig != "" and IsFloat(args.contig):
			sorted = AbsoluteDistanceRank(ListofStringstoFloatList(outdata), float(args.contig)) #Closest to Furthest
		elif parameter == "Total_length" and args.length != "" and IsFloat(args.length):
			sorted = AbsoluteDistanceRank(ListofStringstoFloatList(outdata), float(args.length)) #Closest to Furthest
		elif "NC" in parameter and args.mulcon != "":
			if parameter == "NC0" and mulcon[0] != "":
				sorted = AbsoluteDistanceRank(ListofStringstoFloatList(outdata), float(mulcon[0])) #Closest to Furthest
			elif parameter == "NC1k" and mulcon[1] != "":
				sorted = AbsoluteDistanceRank(ListofStringstoFloatList(outdata), float(mulcon[1])) #Closest to Furthest
			elif parameter == "NC5k" and mulcon[2] != "":
				sorted = AbsoluteDistanceRank(ListofStringstoFloatList(outdata), float(mulcon[2])) #Closest to Furthest
			elif parameter == "NC10k" and mulcon[3] != "":
				sorted = AbsoluteDistanceRank(ListofStringstoFloatList(outdata), float(mulcon[3])) #Closest to Furthest
			elif parameter == "NC25k" and mulcon[4] != "":
				sorted = AbsoluteDistanceRank(ListofStringstoFloatList(outdata), float(mulcon[4])) #Closest to Furthest
			elif parameter == "NC50k" and mulcon[5] != "":
				sorted = AbsoluteDistanceRank(ListofStringstoFloatList(outdata), float(mulcon[5])) #Closest to Furthest
			else:
				finalout = finalout + formatstring.format(title, *outdata) + "\t" + str(DefinitionOfQuality(parameter)) + ": Expected not given\n"
				return finalout
		else:
			finalout = finalout + formatstring.format(title, *outdata) + "\t" + str(DefinitionOfQuality(parameter)) + ": Expected not given\n"
			return finalout
	elif str(DefinitionOfQuality(parameter)) == "More is better":
		sorted = ListofStringstoFloatList(outdata)
		sorted.sort(reverse = True) #Descending
	elif str(DefinitionOfQuality(parameter)) == "Less is better":
		sorted = ListofStringstoFloatList(outdata)
		sorted.sort() #Ascending
	else:
		finalout = finalout + formatstring.format(title, *outdata) + "\n"
		return finalout
	
	#Actual ranking of the data
	rankdata = []
	if args.quality == "best":
		#Compare the data points among themselves: Mark only the highest
		leadcounter = 0
		for data in ListofStringstoFloatList(outdata):
			if data == sorted[0]:
				rankdata.append(">"+str(data))
				Result.Coalition[leadcounter].rank = Result.Coalition[leadcounter].rank + 1
			else:
				rankdata.append(str(data))
			leadcounter = leadcounter + 1
	elif args.quality == "rank":
		#Compare the data points among themselves: Mark each with a rank
		leadcounter = 0
		for data in outdata:
			rankdata.append(str(sorted.index(float(data))+1)+"-"+data)
			Result.Coalition[leadcounter].rank = Result.Coalition[leadcounter].rank + (sorted.index(float(data))+1)
			leadcounter = leadcounter + 1
	elif args.quality == "tier":
		leadcounter = 0
		for data in ListofStringstoFloatList(outdata):
			if data == sorted[0]:
				if parameter == "N50":
					Result.Coalition[leadcounter].N50tier = True
				elif parameter == "L50":
					Result.Coalition[leadcounter].L50tier = True
			leadcounter = leadcounter + 1
		rankdata = ListofStringstoFloatList(outdata)
	
	finalout = finalout + formatstring.format(title, *rankdata) + "\t" + str(DefinitionOfQuality(parameter)) + "\n"
	return finalout
def DefinitionOfQuality(parameter):
	"""Returns definition of high quality per parameter in the table to be appended to the end of each row"""
	
	descriptions = {
	"Name":"",
	"Num_contigs":"Less is better",
	"NC0":"Closer to expected",
	"NC1k":"Closer to expected",
	"NC5k":"Closer to expected",
	"NC10k":"Closer to expected",
	"NC25k":"Closer to expected",
	"NC50k":"Closer to expected",
	"Total_length":"More is better",
	"TL0":"More is better",
	"TL1k":"More is better",
	"TL5k":"More is better",
	"TL10k":"More is better",
	"TL25k":"More is better",
	"TL50k":"More is better",
	"Largest_contig":"More is better",
	"N50":"More is better",
	"N75":"More is better",
	"L50":"Less is better",
	"L75":"Less is better",
	"GCper":"Closer to expected",
	
	"graphCL":"Steeper better",
	"graphNx":"Higher better",
	"graphGC":"Single peak per species"
	}
	
	#If -l or -c are provided, will compare against the given
	if args.length != "":
		descriptions["Total_length"] = "Closer to expected"
	if args.contig != "":
		descriptions["Num_contigs"] = "Closer to expected"
	
	return descriptions[parameter]
def IsFloat(string):
	"""Checks if given string is a float or not"""
	try:
		float(string)
		return True
	except ValueError:
		return False
def AbsoluteDistanceRank(numlist, center):
	"""Arranges a list of numbers according to the absolute distance from a given number; Closest to Furthest"""
	absdist = []
	dictionary = {}
	for num in numlist:
		distance = abs(num - center)
		dictionary[num] = distance
		absdist.append(distance)
	absdist.sort()
	
	ranks = []
	for num in numlist:
		rank = absdist.index(dictionary[num]) + 1
		ranks.append(rank)
	
	out = [x for _,x in sorted(zip(ranks,numlist))]
	
	return out
def ListofStringstoFloatList(rawlist):
	"""Converts a list of string numbers into a list of the corresponding floats"""
	endlist = []
	for num in rawlist:
		num = float(num)
		endlist.append(num)
		
	return endlist
def AppendDefinitions(Tablecontents, finalout):
	"""Appends the definition of each parameter in the table to the end of the results text file"""
	
	descriptions = {
	"Num_contigs":"Num_contigs is the total number of contigs in the assembly.",
	"NC0":"# contigs (>= 0 bp)is the total number of contigs in the assembly that have size greater than or equal to 0 bp.",
	"Total_length":"Total_length is the total number of bases in the assembly.",
	"TL0":"Total length (>= 0 bp) is the total number of bases in the contigs having size greater than or equal to 0 bp.",
	"Largest_contig":"Largest_contig is the length of the longest contig in the assembly.",
	"N50":"N50 is the contig length such that using longer or equal length contigs produces half (50%) of the bases of the assembly.\n\tUsually there is no value that produces exactly 50%, so the technical definition is the maximum length x such that using contigs of length at least x accounts for at least 50% of the total assembly length.",
	"N75": "N75 is the contig length such that using longer or equal length contigs produces 75% of the bases of the assembly.\n\tUsually there is no value that produces exactly 75%, so the technical definition is the maximum length x such that using contigs of length at least x accounts for at least 75% of the total assembly length.",
	"L50": "L50 is the minimum number of contigs that produce half (50%) of the bases of the assembly.\n\tIn other words, it's the number of contigs of length at least N50.",
	"L75": "L75 is the minimum number of contigs that produce 75% of the bases of the assembly.\n\tIn other words, it's the number of contigs of length at least N75.",
	"GCper": "GC (%) is the total number of G and C nucleotides in the assembly, divided by the total length of the assembly.",
	
	"graphCL":"plot shows the growth of assembly contig lengths. On the x-axis, contigs are ordered from largest (contig #1) to smallest. The y-axis gives the size of the x largest contigs in the assembly.",
	"graphNx":"plot shows the Nx metric value as x varies from 0 to 100. Nx is the minimum contig length y such that using contigs of length at least y accounts for at least x% of the total assembly length.",
	"graphGC":"plot shows the distribution of GC percentage among the contigs, i.e., the total number of bases in contigs with such GC content. Typically, the distribution is approximately Gaussian. However, for some genomes it is not Gaussian. For assembly projects with contaminants, the GC distribution of the contaminants often differs from the reference genome and may give a superposition of multiple curves with different peaks."
	}
	
	for parameter in Tablecontents:
		if parameter in descriptions:
			finalout = finalout + "\n" + descriptions[parameter]
	
	return finalout	
def CreateGraph(Graphcontents):
	"""Creates a graph containing the parameters designated by user"""	
	#Creating a plot per data type
	for plot in Graphcontents:
		if plot == "graphGC":
			plotlabels = dict(type="graphGC", title="GC Content", xlabel="% GC", ylabel="# of contigs")
		elif plot == "graphNx":
			plotlabels = dict(type="graphNx", title="Nx", xlabel="Percent", ylabel="Contig length")
		elif plot == "graphCL":
			plotlabels = dict(type="graphCL", title="Cumulative length", xlabel="Contig Index", ylabel="Cumulative length")
		
		CombineGraph(plot, plotlabels)
def CombineGraph(datatype, plotlabels):
	"""Creates a collated graph using Matplotlib given the class attribute of a list of lists X & Y"""
	#Create the combine graph png
	from matplotlib import pyplot as plt
	
	#Plot data
	for data in Result.Coalition:
		list = getattr(data, datatype)
		plt.plot(list[1], list[0], label = getattr(data, "Name"))
	
	#Labels of Plot
	plt.title(plotlabels["title"])
	plt.xlabel(plotlabels["xlabel"])
	plt.ylabel(plotlabels["ylabel"])
	plt.legend()
	plt.grid(True)
	plt.tight_layout()

	#Save and close Plot
	plt.savefig(plotlabels["type"]+"_result.png")
	plt.close()
	

if __name__=="__main__":
	#User Input
	import argparse
	parser = argparse.ArgumentParser(description='Summarizes several QUAST html files into a single outputfile.', formatter_class=argparse.RawTextHelpFormatter)
	parser.add_argument('-r','--result', choices=['default', 'all', 'graph', 'table'], nargs ="?", default = "default", const = "all", help='''
	The results to be compiled.
	Options
	- "default": Name, Number of contigs,
		Total Length, Largest Contig,
		N50, GC graph
	- "graph": GC graph, Nx graph,
		Cumulative Length graph;
	- "table": Name,
		# contigs,
		# contigs (>= 0 bp),
		# contigs (>= 5 bp),
		# contigs (>= 1k bp),
		# contigs (>= 5k bp),
		# contigs (>= 10k bp),
		# contigs (>= 25k bp),
		# contigs (>= 50k bp),
		Total length,
		Total length (>= 0 bp),
		Total length (>= 5 bp),
		Total length (>= 1k bp),
		Total length (>= 5k bp),
		Total length (>= 10k bp),
		Total length (>= 25k bp),
		Total length (>= 50k bp),
		Largest contig,
		N50, N75, L50, L75
	-"all": table & graph''')
	parser.add_argument('-d','--define', action='store_true', help='''a definition of the catergory is appended to the results''')
	parser.add_argument('-q','--quality', choices=['best', 'rank', 'tier', 'none'], nargs ="?", default = "none", const = "tier", help='''
	definition and result of quality per catergory is marked
	Choice of showing the ranking per, just the best,
	or /'tier/' ranking: assemblies with top N50 and L50, tiebreaker total length''')
	parser.add_argument('-c','--contig', nargs='?', default = "", const = "", help='optional input of total expected number of contigs')
	parser.add_argument('-m','--mulcon', nargs='*', default = "", help='''
	optional input of expected number of contigs,
	comma delimit per category:
	NC0, NC1k, NC5k, NC10k, NC25k, NC50k
	to skip a category, leave blank''')
	parser.add_argument('-l','--length', nargs='?', default = "", const = "", help='optional input of expected length of genome')
	parser.add_argument('-g','--gcper', nargs='?', default = "", const = "", help='optional input of expected GC percent')
	parser.add_argument('infile', nargs='+', help='the names of the input QUAST html files')
	args = parser.parse_args()

	#Getting Data from files
	for filename in args.infile:
		DataCollect(filename)
		
	#Create the combined result files
	DataOut()