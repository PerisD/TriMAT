#!/usr/bin/env python
#coding: utf-8

import pandas as pd
import os
import shutil
import argparse
import re

helptext="""
This script is to generate all SLURM scripts to run the different PacBio assemblers
Python 3 script
Authors: David Peris UiO, Department of Biosciences
"""

parser = argparse.ArgumentParser(description=helptext,formatter_class=argparse.RawTextHelpFormatter)
parser.add_argument("-i","--input", help="A tab tabulated text file with StrainName and PacBio original compressed file, multiple reads are seaparated by ;, ie. FILENAME.gz", type = str, default = None)
parser.add_argument("-a","--assemblers", help="A tab tabulated text file with the assemblers to be run", type = str, default = None)
parser.add_argument("-f","--folderLayout", help="The path to the folder where all layouts are stored", type = str, default = None)
parser.add_argument("-r","--outputReads", help="Folder where to create the strain folder to store uncompressed PacBio fastq reads", type = str, default = None)
parser.add_argument("-q","--fastQCFolder", help="Folder where to save the fastqc outputs", type = str, default = None)
parser.add_argument("-d","--DeCompress", help="Folder where to save the fastqc outputs", type = str, default = "YES")

parser.set_defaults()

args = parser.parse_args()

#Create a list with the assemblers to be used
assemblersdf = pd.read_csv(args.assemblers, sep='\t', header = None)
assemblers2run = assemblersdf.loc[assemblersdf[1] == "YES", 0].tolist()

generatordir = os.getcwd() + "/"

if not os.path.exists(os.getcwd()+"/SLURM-Outputs/"):
	os.makedirs(os.getcwd()+"/SLURM-Outputs/")

fastqc_folder = generatordir + args.fastQCFolder+"/"
if not os.path.exists(fastqc_folder):
	os.makedirs(fastqc_folder)


#Loop to go through the list of strains and generate folders and files
list_strains = open(args.input,'r')
shutil.copy(args.folderLayout+"fastqc.sh",os.getcwd()+"/01_FastQC.sh")
print("sed -i 's|\[WORKINGDIRECTORY\]|" +  os.getcwd()+"/|g' " + os.getcwd() + "/01_FastQC.sh")
os.system("sed -i 's|\[WORKINGDIRECTORY\]|" +  os.getcwd()+"/|g' " + os.getcwd() + "/01_FastQC.sh")
new_FastQCbatchScript = open(os.getcwd() + "/01_FastQC.sh","a+")
fastq_cmd = ""

for iLine in list_strains:
	MECAT2_Multiple = "NO"
	wtdbg2_Multiple = "NO"
	StrainName = iLine.split('\t')[0]
	StrainFolder = StrainName+'/'
	#Folder to be used in Step 2
	if not os.path.exists(StrainFolder):
		os.makedirs(StrainFolder)
	if args.DeCompress == "YES":
		if not os.path.exists(args.outputReads+StrainFolder):
			os.makedirs(args.outputReads+StrainFolder)
	StrainANDReads = open(StrainFolder+StrainName+"_reads.txt","w")
	StrainANDReads.write(iLine.strip())
	StrainANDReads.close()

	PacBioReads = iLine.split('\t')[1]
	if ";" in PacBioReads:
		MECAT2_Multiple = "YES"
		wtdbg2_Multiple = "YES"
		multiple_reads = PacBioReads.split(";")
		counter = 1
		PacBioReads = []
		for iPacBioReads in multiple_reads:
			#Step to extract the files from the original folder
			if args.DeCompress == "YES":
				if not os.path.isfile(args.outputReads+StrainFolder+StrainName+"_"+str(counter)+".fastq"):
					temp_folder_decompress = args.outputReads+StrainFolder+StrainName+"_"+str(counter)+"/"
					if not os.path.exists(temp_folder_decompress):
						os.makedirs(temp_folder_decompress)
					print("tar zxvf "+iPacBioReads+" -C "+temp_folder_decompress+" *.fastq")
					os.system("tar zxvf "+iPacBioReads+" -C "+temp_folder_decompress+" *.fastq")
					print("find "+temp_folder_decompress+" -name '*.fastq' -exec mv {} "+args.outputReads+StrainFolder+StrainName+"_"+str(counter)+".fastq"+"\;")
					os.system("find "+args.outputReads+" -name '*.fastq' -exec mv {} "+args.outputReads+StrainFolder+StrainName+".fastq"+"\;")
					print("rm -r "+temp_folder_decompress)
					os.system("rm -r "+temp_folder_decompress)
				PacBioReads_temp = args.outputReads+StrainFolder+StrainName+"_"+str(counter)+".fastq"
				PacBioReads.append(PacBioReads_temp)
			else:
				PacBioReads_temp = iPacBioReads
				PacBioReads.append(PacBioReads_temp)
				#Step to generate the batch file to fastQC the reads (Step 1)
			fastq_cmd += "fastqc -o " + fastqc_folder + " -f fastq -t 8 " + PacBioReads_temp + "\n"
			counter += 1
		multiple_reads = PacBioReads #Now we put the new PATH names
		PacBioReads = ' '.join(PacBioReads)
	else:
		#Step to extract the files from the original folder
		if args.DeCompress == "YES":
			if not os.path.isfile(args.outputReads+StrainFolder+StrainName+".fastq"):
				print("tar zxvf "+PacBioReads+" -C "+args.outputReads+StrainFolder+" *.fastq")
				os.system("tar zxvf "+PacBioReads+" -C "+args.outputReads+StrainFolder+" *.fastq")
				print("find "+args.outputReads+StrainFolder+" -name '*.fastq' -exec mv {} "+args.outputReads+StrainFolder+StrainName+".fastq"+"\;")
				os.system("find "+args.outputReads+StrainFolder+" -name '*.fastq' -exec mv {} "+args.outputReads+StrainFolder+StrainName+".fastq"+"\;")
				print("rm -r "+args.outputReads+StrainFolder+"*/")
				os.system("rm -r "+args.outputReads+StrainFolder+"*/")
			PacBioReads = args.outputReads+StrainFolder+StrainName+".fastq"
		#Step to generate the batch file to fastQC the reads (Step 1)
		else:
			fastq_cmd += "fastqc -o " + fastqc_folder + " -f fastq -t 8 " + PacBioReads + "\n"

#Folder to be used in Step 3
	AssemblerFolders = StrainFolder + "raw_assemblies/"
	if not os.path.exists(AssemblerFolders):
		os.makedirs(AssemblerFolders)
	if not os.path.exists(AssemblerFolders + "final_rawAssemblies/"):
		os.makedirs(AssemblerFolders + "final_rawAssemblies/")
	SLURMFolder = StrainFolder + "SLURM-outputs/"
	if not os.path.exists(SLURMFolder):
		os.makedirs(SLURMFolder)
	new_AssemblybatchScript = open(StrainFolder+"02_AssemblySLURMbatch.sh", "w")
	#The mvbatchScript and quast will consider all assemblies were successfully completed - PLEASE check it is true
	mvbatchScript = open(StrainFolder+"03_mvbatchScript.sh", "w")
	shutil.copy(args.folderLayout+"quast.sh",StrainFolder+"04_quast.sh")
	#File to run all Assembly sbatch files in one click
	RawAssemblyNames = ""
	RawAssemblyPATH = ""
	for iAssembly in assemblers2run:
		new_AssemblybatchScript.write("sbatch " + iAssembly + ".sh\n")
		if not os.path.exists(AssemblerFolders+iAssembly+'/'):
			os.makedirs(AssemblerFolders+iAssembly+'/')
		RawAssemblyNames += StrainName + iAssembly + ","
		RawAssemblyPATH += "raw_assemblies/final_rawAssemblies/" + StrainName + "_" + iAssembly + ".fasta "
		shutil.copy(args.folderLayout+iAssembly+'.sh',StrainFolder+iAssembly+'.sh')
		sed_STRAINNAME1 = "sed -i 's|\[STRAINNAME\]|" +  StrainName + "|g' " + StrainFolder+iAssembly + ".sh"
		#print(sed_STRAINNAME1)
		os.system(sed_STRAINNAME1)
		sed_ASSEMBLER = "sed -i 's|\[ASSEMBLER\]|" +  iAssembly + "|g' " + StrainFolder+iAssembly + ".sh"
		#print(sed_ASSEMBLER)
		os.system(sed_ASSEMBLER)
		sed_WORKINGDIRECTORY = "sed -i 's|\[WORKINGDIRECTORY\]|" + generatordir + StrainFolder + "|g' " + StrainFolder+iAssembly + ".sh"
		#print(sed_WORKINGDIRECTORY)
		os.system(sed_WORKINGDIRECTORY)
		sed_WORKINGDIRECTORY = "sed -i 's|\[WORKINGDIRECTORY\]|" + generatordir + StrainFolder + "|g' " + StrainFolder + "04_quast.sh"
		os.system(sed_WORKINGDIRECTORY)
		sed_ASSEMBLERDIR = "sed -i 's|\[ASSEMBLERDIR\]|" +  generatordir + AssemblerFolders + iAssembly +"/" + "|g' " + StrainFolder+iAssembly + ".sh"
		#print(sed_ASSEMBLERDIR)
		os.system(sed_ASSEMBLERDIR)

		if iAssembly == "mecat2":
			PacBioInfo_Included = "FALSE"
			MecatPacBio = PacBioReads
			if MECAT2_Multiple == "YES":
				mecat2_MultipleReads = open(AssemblerFolders+iAssembly+"/mecat2_MultipleReads.txt","w")
				for iPacBioReads in multiple_reads:
					mecat2_MultipleReads.write(iPacBioReads.strip()+"\n")
				MecatPacBio = os.getcwd() + "/" + AssemblerFolders+iAssembly+"/mecat2_MultipleReads.txt"
			shutil.copy(args.folderLayout+'mecat2_config_file.txt',AssemblerFolders+iAssembly+"/"+StrainName+'_config_file.txt')
			sed_STRAINNAME2 = "sed -i 's|\[STRAINNAME\]|" +  StrainName + "|g' " + AssemblerFolders+iAssembly+"/"+StrainName+"_config_file.txt"
			#print(sed_STRAINNAME2)
			os.system(sed_STRAINNAME2)
			sed_PacBioReads1 = "sed -i 's|\[PACBIOREADS\]|" +  MecatPacBio + "|g' " + AssemblerFolders+iAssembly+"/"+StrainName+"_config_file.txt"
			#print(sed_PacBioReads1)
			os.system(sed_PacBioReads1)
			mvbatchScript.write("cp raw_assemblies/" + iAssembly+"/"+StrainName + "/4-fsa/contigs.fasta raw_assemblies/final_rawAssemblies/" + \
			StrainName + "_" + iAssembly + ".fasta\n")
		if iAssembly == "canu":
			mvbatchScript.write("cp raw_assemblies/" + iAssembly+"/"+StrainName + ".contigs.fasta raw_assemblies/final_rawAssemblies/" + \
			StrainName + "_" + iAssembly + ".fasta\n")
		if iAssembly == "flye":
			mvbatchScript.write("cp raw_assemblies/" + iAssembly+"/assembly.fasta raw_assemblies/final_rawAssemblies/" + \
			StrainName + "_" + iAssembly + ".fasta\n")
		if iAssembly == "smartdenovo":
			mvbatchScript.write("cp raw_assemblies/" + iAssembly+"/"+StrainName + ".dmo.cns raw_assemblies/final_rawAssemblies/" + \
			StrainName + "_" + iAssembly + ".fasta\n")
		if iAssembly == "wtdbg2":
			mvbatchScript.write("cp raw_assemblies/" + iAssembly+"/"+StrainName + ".ctg.fasta raw_assemblies/final_rawAssemblies/" + \
			StrainName + "_" + iAssembly + ".fasta\n")
			if wtdbg2_Multiple == "YES":
				wtdbg2Reads_cm = []
				for iPacBioReads in multiple_reads:
					wtdbg2Reads_cm.append('-i '+iPacBioReads)
				' '.join(wtdbg2Reads_cm)
			else:
				wtdbg2Reads_cm = '-i ' + PacBioReads
			sed_PacBioReads2 = "sed -i 's|\[PACBIOREADS\]|" +  PacBioReads + "|g' " + StrainFolder+iAssembly + ".sh"
			#print(sed_PacBioReads3)
			os.system(sed_PacBioReads2)

		sed_PacBioReads3 = "sed -i 's|\[PACBIOREADS\]|" +  PacBioReads + "|g' " + StrainFolder+iAssembly + ".sh"
		#print(sed_PacBioReads3)
		os.system(sed_PacBioReads3)

	if not os.path.exists(AssemblerFolders+"quast_report/"):
		os.makedirs(AssemblerFolders+"quast_report/")
	new_AssemblybatchScript.close()
	quast_cmd = "quast -t 16 -o raw_assemblies/quast_report/ --fungus -l " + RawAssemblyNames[:-1] + " "
	quast_cmd += RawAssemblyPATH[:-1]
	sed_QUASTCMD = "sed -i 's|\[QUASTCMD\]|" + quast_cmd + "|g' " + StrainFolder +  "04_quast.sh"
	#print(sed_QUASTCMD)
	os.system(sed_QUASTCMD)
	mvbatchScript.close()

new_FastQCbatchScript.write(fastq_cmd)
new_FastQCbatchScript.write("\ndate\n")
new_FastQCbatchScript.close()

print("Done!")