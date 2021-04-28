#!/usr/bin/env python
#coding: utf-8

import argparse
from subprocess import call
import os
import shutil

helptext="""
This script is to copy and/or trim illumina reads and prepare them for iWGS
iWGS will be run in a second step to assembly the genomes based on selected assemblers
Authors: David Peris UW-Madison, Dept Genetics
"""


parser = argparse.ArgumentParser(description=helptext,formatter_class=argparse.RawTextHelpFormatter)
parser.add_argument("-i","--input", help="A tab tabulated text file with StrainName, path to the reads, Coverage, Read Length", type = str, default = None)
parser.add_argument("-r","--reference", help="Assembly to compare our results", type = str, default = None)
parser.add_argument("-o","--output", help="output folder", type = str, default = None)
parser.add_argument("-a","--assemblers", help="A tab tabulated text file with the assemblers to use", type = str, default = None)
parser.add_argument("-t","--threads", help="Number of CPUs to be used", type = str, default = "1")
parser.add_argument("-m","--memory", help=" number of GBs of memory to use", type = str, default = "8")
parser.add_argument("-q","--quality", help="Start trimmomatic to improve the reads", type = str, default = "NO")
parser.add_argument("-s","--split", help="individual SLURM files", type = str, default = "NO")
parser.add_argument("-l","--layoutFolder", help="Folder where we stored the iWGS layouts", type = str, default = None)
parser.add_argument("-T","--TimeRun", help="Time to run, format HH:MM:SS", type = str, default = "02:00:00")

parser.set_defaults()

args = parser.parse_args()

working_directory = os.getcwd() + "/"

if not os.path.exists("SLURM-outputs/"):
	os.makedirs("SLURM-outputs/")

if args.quality == "YES":
	print '##STEP with trimmomatic'
	readfile = open(args.input, 'r')
	if not os.path.exists("trimmomatic-SEoutput/"):
		os.makedirs("trimmomatic-SEoutput/")
	if not os.path.exists(args.output+"/"):
		os.makedirs(args.output+"/")
	if not os.path.exists(args.output+"/libraries"):
		os.makedirs(args.output+"/libraries/")
	if not os.path.exists("SLURM-outputs/"):
		os.makedirs("SLURM-outputs/")
	print "=======================Trimmomatic step========================"
	for line in readfile:
		library = "PE"
		StrainName = line.split('\t')[0]
		StrainFolder = args.output+"/libraries/"+StrainName+"/"
		if not os.path.exists(StrainFolder):
			os.makedirs(StrainFolder)
		reads = line.split('\t')[1]
		Read1 = reads.replace('_*.','_1.')
		Read2 = reads.replace('_*.','_2.')
		if not os.path.isfile(Read2):
			library = "SE"
		if library == "PE":
			cmdTrim = 'trimmomatic ' + library
			cmdTrim += ' -threads ' + args.threads + ' -phred33 -trimlog analytics.txt ' + Read1 + ' ' + Read2
			cmdTrim += ' ' + working_directory + StrainFolder + StrainName + "_1.fq " + working_directory + "trimmomatic-SEoutput/" + StrainName + "_1tm-se.fq "
			cmdTrim += working_directory + StrainFolder + StrainName + "_2.fq " + working_directory + "trimmomatic-SEoutput/" + StrainName + "_2tm-se.fq "
			cmdTrim += 'ILLUMINACLIP:/cluster/home/davidper/conda_env/iWGS/share/trimmomatic-0.36-6/adapters/TruSeq2-PE.fa:2:30:10 TRAILING:3 MINLEN:25'
			print cmdTrim
			os.system(cmdTrim)
		elif library == "SE":
			cmdTrim = 'trimmomatic ' + library
			cmdTrim += ' -threads ' + args.threads + ' -phred33 -trimlog analytics.txt ' + Read1 + ' '
			cmdTrim += ' ' + working_directory + StrainFolder + StrainName + ".fq "
			cmdTrim += 'ILLUMINACLIP:/cluster/home/davidper/conda_env/iWGS/share/trimmomatic-0.36-6/adapters/TruSeq2-PE.fa:2:30:10 TRAILING:3 MINLEN:25'
			print cmdTrim
			os.system(cmdTrim)
	readfile.close()
else:
	readfile = open(args.input, 'r')
	if not os.path.exists(args.output+"/"):
		os.makedirs(args.output+"/")
	if not os.path.exists(args.output+"/libraries"):
		os.makedirs(args.output+"/libraries/")
	print "=======================NO Trimmomatic step========================"
	for line in readfile:
		library = "PE"
		StrainName = line.split('\t')[0]
		StrainFolder = args.output+"/libraries/"+StrainName+"/"
		if not os.path.exists(StrainFolder):
			os.makedirs(StrainFolder)
		reads = line.split('\t')[1]
		Read1 = reads.replace('_*.','_1.')
		Read2 = reads.replace('_*.','_2.')
		if not os.path.isfile(Read2):
			library = "SE"
		if library == "PE":
			if not os.path.isfile(args.output+"/libraries/"+StrainName+"/"+StrainName + "_1.fq"):
				shutil.copy(Read1,args.output+"/libraries/"+StrainName+"/"+StrainName + "_1.fq")
			if not os.path.isfile(args.output+"/libraries/"+StrainName+"/"+StrainName + "_2.fq"):
				shutil.copy(Read2,args.output+"/libraries/"+StrainName+"/"+StrainName + "_2.fq")
		elif library == "SE":
			if not os.path.isfile(args.output+"/libraries/"+StrainName+"/"+StrainName + ".fq"):
				shutil.copy(Read1,args.output+"/libraries/"+StrainName+"/"+StrainName + ".fq")
	readfile.close()

readfile = open(args.input, 'r')
sbatchFile = open("01_sbatchSerial.sh",'w')
sbatchFile.write("#!usr/bin/env sh\n")
SLURMText = ""
if args.split == "YES": 
	for line in readfile:
		library = "PE"
		StrainName = line.split('\t')[0]
		os.system("cp " + args.layoutFolder + "iWGS_control.ctl ./" + StrainName + "_iWGS.ctl")
		os.system("cp " + args.layoutFolder + "iWGS_SLURM.sh ./" + StrainName + "_SLURM.sh")
		reads = line.split('\t')[1]
		Coverage = str(int(float(line.split('\t')[2])))
		Length = line.split('\t')[3]
		if int(float(Length)) <= 100:
			InsertSize = 190
			StDev = 8
		elif 100 < int(float(Length)) <= 150:
			InsertSize = 280
			StDev = 10
		elif int(float(Length)) >150:
			InsertSize = 470
			StDev = 40
		Read1 = reads.replace('_*.','_1.')
		Read2 = reads.replace('_*.','_2.')
		if not os.path.isfile(Read2):
			library = "SE"
			LibraryText = 'library = '+StrainName+','+library+','+Coverage+','+Length.strip()+'\\n'
		else:
			LibraryText = 'library = '+StrainName+','+library+','+Coverage+','+Length.strip()+','+str(InsertSize)+','+str(StDev)+'\\n'
		modifyRef1 = "sed -i 's|\[REFGENOME\]|" + args.reference + "|g' " + StrainName + "_iWGS.ctl"
		os.system(modifyRef1)
		modifyOutput1 = "sed -i 's|\[OUTPUTDIR\]|" + args.output + "|g' " + StrainName + "_iWGS.ctl"
		os.system(modifyOutput1)
		modifyCPU1 = "sed -i 's|\[CPUs\]|" + args.threads + "|g' " + StrainName + "_iWGS.ctl"
		os.system(modifyCPU1)
		modifyMem1 = "sed -i 's|\[MEMORY\]|" + args.memory + "|g' " + StrainName + "_iWGS.ctl"
		os.system(modifyMem1)
		modifyLib1 = "sed -i 's|\[LIBRARYTEXT\]|" + LibraryText + "|g' " + StrainName + "_iWGS.ctl"
		os.system(modifyLib1)
		modifyText2 = "sed -i 's|\[STRAINNAME\]|" + StrainName + "|g' " + StrainName + "_SLURM.sh"
		os.system(modifyText2)
		SlurmText = "/cluster/home/davidper/software/programs/iWGS/iWGS -s " + StrainName + "_iWGS.ctl --Real"
		modifySlurm2 = "sed -i 's|\[SLURMTEXT\]|" + SlurmText + "|g' " + StrainName + "_SLURM.sh"
		os.system(modifySlurm2)
		assemblerFile = open(args.assemblers,'r')
		ProtocolText = ""
		for protocol in assemblerFile:
			protocol = protocol.split('\t')
			if protocol[1].strip() == "YES":
				assembler = protocol[0]
				ProtocolText += 'protocol = '+StrainName+assembler[0:2]+','+assembler+','+StrainName+'\\n'
		modifyProt1 = "sed -i 's|\[PROTOCOLTEXT\]|" + ProtocolText + "|g' " + StrainName + "_iWGS.ctl"
		os.system(modifyProt1)
		assemblerFile.close()
		sbatchFile.write("sbatch " + StrainName + "_SLURM.sh\n")
else:
	LibraryText = ""
	ProtocolText = ""
	os.system("cp " + args.layoutFolder + "iWGS_control.ctl ./AllStrains_iWGS.ctl")
	os.system("cp " + args.layoutFolder + "iWGS_SLURM.sh ./AllStrains_SLURM.sh")
	sbatchFile.write("sbatch AllStrains_SLURM.sh")
	for line in readfile:
		library = "PE"
		StrainName = line.split('\t')[0]
		reads = line.split('\t')[1]
		Coverage = str(int(float(line.split('\t')[2])))
		Length = line.split('\t')[3]
		if int(float(Length)) <= 100:
			InsertSize = 190
			StDev = 8
		elif 100 < int(float(Length)) <= 150:
			InsertSize = 280
			StDev = 10
		elif int(float(Length)) >150:
			InsertSize = 470
			StDev = 40
		Read1 = reads.replace('_*.','_1.')
		Read2 = reads.replace('_*.','_2.')
		if not os.path.isfile(Read2):
			library = "SE"
			LibraryText += 'library = '+StrainName+','+library+','+Coverage+','+Length.strip()+'\\n'
		else:
			LibraryText += 'library = '+StrainName+','+library+','+Coverage+','+Length.strip()+','+str(InsertSize)+','+str(StDev)+'\\n'
		assemblerFile = open(args.assemblers,'r')
		for protocol in assemblerFile:
			protocol = protocol.split('\t')
			if protocol[1].strip() == "YES":
				assembler = protocol[0]
				ProtocolText += 'protocol = '+StrainName+assembler[0:2]+','+assembler+','+StrainName+'\\n'
		assemblerFile.close()
	modifyRef1 = "sed -i 's|\[REFGENOME\]|" + args.reference + "|g' " + StrainName + "_iWGS.ctl"
	os.system(modifyRef1)
	modifyOutput1 = "sed -i 's|\[OUTPUTDIR\]|" + args.output + "|g' AllStrains_iWGS.ctl"
	os.system(modifyOutput1)
	modifyCPU1 = "sed -i 's|\[CPUs\]|" + args.threads + "|g' AllStrains_iWGS.ctl"
	os.system(modifyCPU1)
	modifyMem1 = "sed -i 's|\[MEMORY\]|" + args.memory + "|g' AllStrains_iWGS.ctl"
	os.system(modifyMem1)
	modifyLib1 = "sed -i 's|\[LIBRARYTEXT\]|" + LibraryText + "|g' AllStrains_iWGS.ctl"
	os.system(modifyLib1)
	modifyProt1 = "sed -i 's|\[PROTOCOLTEXT\]|" + ProtocolText + "|g' AllStrains_iWGS.ctl"
	os.system(modifyProt1)
	modifyText2 = "sed -i 's|\[STRAINNAME\]|AllStrains|g' AllStrains_SLURM.sh"
	os.system(modifyText2)
	SlurmText = "/cluster/home/davidper/software/programs/iWGS/iWGS -s AllStrains_iWGS.ctl --Real"
	modifySlurm2 = "sed -i 's|\[SLURMTEXT\]|" + SlurmText + "|g' AllStrains_SLURM.sh"
	os.system(modifySlurm2)
readfile.close()
sbatchFile.close()

os.system("sed -i 's|\[TIME\]|" + args.TimeRun + "|g' " + "*_SLURM.sh")
os.system("sed -i 's|\[CPUs\]|" + args.threads + "|g' " + "*_SLURM.sh")
os.system("sed -i 's|\[MEMORY\]|" + args.memory + "|g' " + "*_SLURM.sh")
os.system("sed -i 's|\[WORKINGDIR\]|" + os.getcwd() + "|g' " + "*_SLURM.sh")

print "Done!"