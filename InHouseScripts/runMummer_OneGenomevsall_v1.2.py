#! /usr/bin/env python
#coding: utf-8

import sys,os
import glob
from subprocess import call
import argparse

helptext="""
This script will run nucmer an generate a comparison of your target assembly with all the genomes stored in the input folder
Remember EOL to be encoded in Unix
Authors: David Peris UW-Madison, Dept Genetics
"""

parser = argparse.ArgumentParser(description=helptext,formatter_class=argparse.RawTextHelpFormatter)
parser.add_argument("-i","--input", help="PATH to the folder where assemblies are stored", type = str, default = None)
parser.add_argument("-g","--genome", help="Is it nuclear or mtDNA", type = str, default = "nuclear")
parser.add_argument("-t","--target", help="Assembly name to compare to the rest of assemblies", type = str, default = None)
parser.add_argument("-M","--maxGap", help="maximum gap extension argument", type = str, default = "500")
parser.add_argument("-m","--minClus", help="minimum cluster match argument", type = str, default = "150")

parser.set_defaults()

args = parser.parse_args()

input_folder = args.input

list_of_assemblies = glob.glob(input_folder+'*.fas*')

#def move_files(job_name):
#	cmdA = 'mv '+job_name+'.* '+job_name+'/'
#	return cmdA

#def show_coords(job_name):
#	cmdB = 'show-coords -r '+job_name+'.delta'+' > '+job_name+'.coords'
#	return cmdB

comparisons_done = 0

reference_assembly_path = args.target
reference_assembly_name = reference_assembly_path.split('/')[-1]
reference_StrainName = reference_assembly_path.split('/')[-1].split('.')[0].split('_')[0]
counter = 0

while counter <= len(list_of_assemblies)-1:
	query_assembly_path = list_of_assemblies[counter]
	query_assembly_name = query_assembly_path.split('/')[-1]
	query_StrainName = query_assembly_path.split('/')[-1].split('.')[0].split('_')[0]
	job_name = reference_StrainName + '-' + query_StrainName
	new_folder = os.getcwd() + '/' + job_name
	if os.path.exists(new_folder):
		print "Folder %s is not necessart" % (new_folder)
	else:
		os.makedirs(new_folder)
	if args.genome == "nuclear":
		print " ".join(["nucmer","--maxgap="+args.maxGap,"--mincluster="+args.minClus,"--prefix="+job_name,reference_assembly_path,query_assembly_path])
		call(["nucmer","--maxgap="+args.maxGap,"--mincluster="+args.minClus,"--prefix="+job_name,reference_assembly_path,query_assembly_path])
		show_coords = 'show-coords -lT -r '+job_name+'.delta'+' > '+job_name+'.coords'
		print "show_coords:" + show_coords
		os.system(show_coords)
		print " ".join(["mummerplot","--png","--prefix="+job_name,"-R",reference_assembly_path,"-Q",query_assembly_path,"--filter",job_name+'.delta'])
		call(["mummerplot","--png","--prefix="+job_name,"-R",reference_assembly_path,"-Q",query_assembly_path,"--filter",job_name+'.delta'])
		print " ".join(["mummerplot","--png","--prefix="+job_name+"/"+job_name+"_sorted","--layout",job_name+'.delta'])#
		call(["mummerplot","--png","--prefix="+job_name+"/"+job_name+"_sorted","--layout",job_name+'.delta'])#
		print " ".join(["mummerplot","--postscript","--prefix="+job_name,"-R",reference_assembly_path,"-Q",query_assembly_path,"--filter",job_name+'.delta'])
		call(["mummerplot","--postscript","--prefix="+job_name,"-R",reference_assembly_path,"-Q",query_assembly_path,"--filter",job_name+'.delta'])
		move_files = 'mv '+job_name+'.* '+job_name+'/'
		print "move_files:" + move_files
		os.system(move_files)
		counter += 1
		comparisons_done += 1
	else:
		print " ".join(["nucmer","--maxgap=500","--mincluster=150","--prefix="+job_name,reference_assembly_path,query_assembly_path])
		call(["nucmer","--maxgap=500","--mincluster=150","--minmatch=10","--prefix="+job_name,reference_assembly_path,query_assembly_path])
		show_coords = 'show-coords -lT -r '+job_name+'.delta'+' > '+job_name+'.coords'
		print "show_coords:" + show_coords
		os.system(show_coords)
		print " ".join(["mummerplot","--png","--prefix="+job_name,"-R",reference_assembly_path,"-Q",query_assembly_path,"--filter",job_name+'.delta'])
		call(["mummerplot","--png","--prefix="+job_name,"-R",reference_assembly_path,"-Q",query_assembly_path,"--filter",job_name+'.delta'])
		print " ".join(["mummerplot","--png","--prefix="+job_name+"/"+job_name+"_sorted","--layout",job_name+'.delta'])#
		call(["mummerplot","--png","--prefix="+job_name+"/"+job_name+"_sorted","--layout",job_name+'.delta'])#
		print " ".join(["mummerplot","--postscript","--prefix="+job_name,"-R",reference_assembly_path,"-Q",query_assembly_path,"--filter",job_name+'.delta'])
		call(["mummerplot","--postscript","--prefix="+job_name,"-R",reference_assembly_path,"-Q",query_assembly_path,"--filter",job_name+'.delta'])
		move_files = 'mv '+job_name+'.* '+job_name+'/'
		print "move_files:" + move_files
		os.system(move_files)
		counter += 1
		comparisons_done += 1
	print "%i comparisons with %s has been done" % (counter,reference_StrainName)

print "Comparisons done! A total of %i has been done" % (comparisons_done)
