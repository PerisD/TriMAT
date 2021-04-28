#! /usr/bin/env python
#coding: utf-8

import os
import argparse
import glob

helptext="""
This script will run MAFFT and pal2nal based on a list of fasta names
"""

parser = argparse.ArgumentParser(description=helptext,formatter_class=argparse.RawTextHelpFormatter)
parser.add_argument("-i","--fasta2Parse", help="list of genes stored in a csv, such as Genes_in_All_100.csv used in pull_busco", type = str, default = None)
parser.add_argument("-t","--threads", help="number of threads", type = str, default = "4")
parser.add_argument("-s","--storedFolder", help="Folder where no aligned fastas are stored", type = str, default = None)


args = parser.parse_args()

if not os.path.exists("genes_aligned/"):
		os.makedirs("genes_aligned/")

if not os.path.exists("genes_trimmed/"):
		os.makedirs("genes_trimmed/")

fasta_files = open(args.fasta2Parse,'r')
next(fasta_files)
counter1= 0
for iLine in fasta_files:
	counter1 +=1
fasta_files.close()

fasta_files = open(args.fasta2Parse,'r')
next(fasta_files)

counter = 0
for iFasta in fasta_files:
	counter += 1
	iFasta = iFasta.split(',')[0]
	print iFasta + ": " + str(counter) + " of " + str(counter1)
	mafft_cmd = "mafft --maxiterate 1000 --thread " + args.threads + " --genafpair " + args.storedFolder + iFasta + "_aa.fas > genes_aligned/" + iFasta + "_aa_aln.fas"
	print mafft_cmd
	os.system(mafft_cmd)
	pal2nal_cmd = "pal2nal.pl genes_aligned/" + iFasta + "_aa_aln.fas " + args.storedFolder + iFasta + "_nt.fas -codontable 1 -output fasta > genes_aligned/" + iFasta + "_nt_aln.fas"
	print pal2nal_cmd
	os.system(pal2nal_cmd)
	trimal_fasta_cmd = "trimal -in genes_aligned/" + iFasta + "_nt_aln.fas -out genes_trimmed/" + iFasta + "_nt_tr.fas -fasta -gt 1 -block 3"
	trimal_phylip_cmd = "trimal -in genes_aligned/" + iFasta + "_nt_aln.fas -out genes_trimmed/" + iFasta + "_nt_tr.phy -phylip_paml -gt 1 -block 3"
	print trimal_fasta_cmd
	print trimal_phylip_cmd
	os.system(trimal_fasta_cmd)
	os.system(trimal_phylip_cmd)

print "Done alignment and trimming!\nNow checking length"

phylyp_files = glob.glob("genes_trimmed/*.phy")

info_phylyp = open("phylypTrimmed_length.txt",'w')
info_phylyp.write('\t'.join(["BUSCO_ID","Nspecimens","Length"])+"\n")
counter1=0
for iPhylyp in phylyp_files:
	counter1 += 1
	PhylypName = iPhylyp.split('/')[-1].split(".")[0].split("_")[0]
	print(PhylypName + ": " + str(counter1) + " of " + str(len(phylyp_files)))
	temp_file = open(iPhylyp,'r')
	iLine = temp_file.next()
	temp_file.close()
	info_phylyp.write('\t'.join([PhylypName,iLine.split(" ")[1],iLine.split(" ")[2]]))
info_phylyp.close()