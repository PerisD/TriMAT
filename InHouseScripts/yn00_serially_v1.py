#! /usr/bin/env python
#coding: utf-8

import argparse
import os
import shutil as sh
import re

helptext="""
This script will run yn00 serially for each fasta file and it will extract the Yang and Nielse 2000 method
Authors: David Peris IATA-CSIC
"""

parser = argparse.ArgumentParser(description=helptext,formatter_class=argparse.RawTextHelpFormatter)
parser.add_argument("-l","--layout", help="Folder where the layout is stored", type = str, default = None)
parser.add_argument("-i","--input", help="list with all the paths to the fasta files", type = str, default = None)
parser.add_argument("-c","--convert2Phylyp", help="if you want to convert the file to phylyp format, default NO", type = str, default = "NO")
parser.add_argument("-o","--outputFolder", help="where to run yn00 and store the outputs", type = str, default = None)


parser.set_defaults()

args = parser.parse_args()

layout_file = args.layout + "yn00_layout.ctl"
input_list = args.input

if not os.path.exists(args.outputFolder+"/"):
	os.makedirs(args.outputFolder+"/")

for iFile in open(input_list,'r'):
	iFile = iFile.strip()
	GeneName = iFile.split('/')[-1].split('.')[0].split('_')[0]
	if args.convert2Phylyp == "YES":
		fasta2phy_cmd = "perl ~/software/scripts/SAGA/Fasta2Phylip.pl " + iFile #MODIFY THE PATH IF NECESSARY
		print fasta2phy_cmd
		os.system(fasta2phy_cmd)
		changeName_cmd = "mv " + iFile.split('/')[-1].strip() + ".phy " +  GeneName + ".phy"
		iFile = os.getcwd() + "/" +  GeneName + ".phy"
	sh.copy(iFile, args.outputFolder + "/" + GeneName + ".phy")
	sh.copy(layout_file, args.outputFolder + "/" + GeneName+"_yn00.ctl")
	modifyPhylipFile = "sed -i 's|\[PHYLIPFILE\]|" + args.outputFolder + "/" + GeneName + ".phy" + "|g' " + GeneName+"_yn00.ctl"
	print modifyPhylipFile
	os.system(modifyPhylipFile)
	modifyOutputFile = "sed -i 's|\[OUTPUTFILE\]|" + GeneName + "_yn00.txt" + "|g' " + GeneName+"_yn00.ctl"
	print modifyOutputFile
	os.system(modifyOutputFile)
	yn00Run_cmd = "yn00 " + GeneName+"_yn00.ctl"
	print yn00Run_cmd
	os.system(yn00Run_cmd)

	list_seq = []
	fasta_temp = open(iFile.strip(),'r')
	fasta_temp.next()
	for iLine in fasta_temp:
		SeqName = iLine.split(" ")[0]
		list_seq.append(SeqName)
	print(len(list_seq))
	ynFile_temp = open(GeneName + "_yn00.txt",'r')
	dSdNFile_temp = open(GeneName + "_YangNielse2000method.txt",'w')
	starts_data = "OFF"
	startsTable = "OFF"
	counter = 0
	for iLine in ynFile_temp:
		if "(B)" in iLine:
			starts_data = "ON"
		if "(C)" in iLine:
			starts_data = "OFF"
		if starts_data == "ON":
			if "seq. seq." in iLine:
				counter = 0
				iLine = re.sub(' +', '\t', iLine) + "\tGeneName"
				indices = [0,1,2,3,4,5,6,7,9,10,12,13]
				iLine = iLine.split('\t')
				iLine = [iLine[i] for i in indices]
				iLine[8] = "dN_SE"
				iLine[10] = "dS_SE"
				iLine = '\t'.join(iLine)
				dSdNFile_temp.write(iLine+"\n")
				startsTable = "ON"
			if startsTable == "ON":
				if len(iLine) > 1 and counter >= 1:
					iLine = re.sub(' +', '\t', iLine)
					iLine = iLine.split('\t')[1:]
					#print iLine
					StrainName1 = iLine[0]
					StrainName2 = iLine[1]
					StrainName1 = list_seq[int(StrainName1)-1]
					StrainName2 = list_seq[int(StrainName2)-1]
					iLine[0] = StrainName1
					iLine[1] = StrainName2
					iLine[-1] = iLine[-1].strip()
					iLine.append(GeneName)
					indices = [0,1,2,3,4,5,6,7,9,10,12,13]
					iLine = [iLine[i] for i in indices]
					iLine = '\t'.join(iLine)
					dSdNFile_temp.write(iLine+"\n")
		counter += 1
	ynFile_temp.close()
	dSdNFile_temp.close()

print "Done!"