#! /usr/bin/env python
#coding: utf-8

import argparse
import os
import shutil as st

helptext="""
This script will generate SLURM fastANI.sh to run fastANI serially and finally parse the outputs to generate the phylogenetic tree
Authors: David Peris IATA-CSIC
"""

parser = argparse.ArgumentParser(description=helptext,formatter_class=argparse.RawTextHelpFormatter)
parser.add_argument("-t","--threads", help="Number of CPUs to be used", type = str, default = "16")
parser.add_argument("-i","--input", help="list with all the assemblies to parse", type = str, default = None)
parser.add_argument("-o","--output", help="Folder to run the sbatch files", type = str, default = None)
parser.add_argument("-l","--layouts", help="Folder where SLURM fastANI.sh layout is stored", type = str, default = None)
parser.add_argument("-L","--fragLen", help="Fset the fragLen for calculations", type = str, default = "NA")


parser.set_defaults()

args = parser.parse_args()

if not os.path.exists(args.output):
	os.makedirs(args.output)
if not os.path.exists(args.output + "/SLURM-outputs/"):
	os.makedirs(args.output + "/SLURM-outputs/")

assemblies_list = open(args.input,'r')
st.copy(args.input,args.output+"/"+args.input)

AllFastANIs = open(args.output + "/BashFastANIs.sh",'w')
for iAssembly in assemblies_list:
	StrainName = iAssembly.split('/')[-1].split('.')[0]
	New_fastANI = args.output + "/fastANI-" + StrainName + ".sh"
	cp_cmd = "cp " + args.layouts + "fastANI.sh " + New_fastANI
	print cp_cmd
	os.system(cp_cmd)
	fastani_cmd = "fastANI -q  " + iAssembly.strip() + " --rl " +  args.input + " -t " + args.threads + " -o " + StrainName + "vsAll.txt"
	if args.fragLen != "NA":
		fastani_cmd += " --fragLen " + args.fragLen
	modifyFASTANICMD = "sed -i 's|\[FASTANICMD\]|" + fastani_cmd + "|g' " + New_fastANI
	print modifyFASTANICMD
	os.system(modifyFASTANICMD)
	modifyStrainName = "sed -i 's|\[STRAINNAME\]|" + StrainName + "|g' " + New_fastANI
	print modifyStrainName
	os.system(modifyStrainName)
	modifyOUTPUTDIR = "sed -i 's|\[OUTPUTDIR\]|" + os.getcwd() + "/" + args.output + "/" + "|g' " + New_fastANI
	print modifyOUTPUTDIR
	os.system(modifyOUTPUTDIR)
	AllFastANIs.write("sbatch fastANI-" + StrainName + ".sh\n")

AllFastANIs.close()
print "Done!" 
