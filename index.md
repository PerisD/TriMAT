## Title

Assemblies, XXX regions and source data from XXX et al YYY

**Authors**: 

**Journal**:

**Year**:

**Abstract**:

<div style="text-align:center"><img src="https://sismo.app/wp-content/uploads/2019/02/under-construction-gif-11.gif" width="250"/></div>

### Assemblies

Assemblies generated using PacBio and Illumina reads

Specimen |Species| Nuclear
-------|-------|---|------
TA10106M1|*T. abietinum*|[NGENOME](LLL.tar.gz "NGENOME")
TF100210M3|*T. fuscoviolaceum*|[NGENOME](LLL.tar.gz "NGENOME")

[Additional assemblies](LLL.tar.gz "178 SPAdes assemblies generated using Illumina reads")

[L15831](https://mycocosm.jgi.doe.gov/Triab1_1/Triab1_1.home.html "L15831 downloaded from JGI")

### Crossing pictures

To test compatible and incompatible MAT alleles we performed crosses and we took pictures to check the generation of clamp connections.

[Macroscopic](LLL.tar.gz "Macroscopic pictures of trichaptum crosses")

[Microscopic](LLL.tar.gz "Pictures taken under the microscope of the contact zone during trichaptum crosses")

### MATA and MATB regions

MATA and MATB regions were assembled and annotated to extract individual genes and make multiple sequence alignments to perform multiple analyses.

[MATA](LLL.zip "MATA regions containing homeodomain genes")

[MATB](LLL.zip "MATB regions containing pheromone receptors and pheromones")

[IndividualGeneAlignments](LLL.zip "Trimmed individual gene alignments")

### Source data

Raw data used to generate Figures XXX-YYY

Description | File | Figure
------------|------|-------
*BUSCO annotation statistics and location on TA10106M1 genome*|[BUSCO-MAT genes](LLL/BUSCO_MAT_info.csv "BUSCO-MAT genes")|Figure XXX
*Absolute divergence statitstic for BUSCO and MAT genes*|[dxy](LLL/dxy.csv "dxy")|Figure XXX
*Relative divergence statitstic for BUSCO and MAT genes*|[Fst](LLL/Fst.csv "Fst")|Figure XXX
*Multilocus Hudson–Kreitman–Aguadé (HKA) test performed with HKAdirect 0.7b*|[MKT](LLL/MKT.csv "MKT")|Figure XXX
*Average number of synonymous substitutions per synonymous sites (dS) and non-synonymous substitutions per non-synonymous sites (dN) for BUSCO and MAT genes*|[PAML](LLL/paml.csv "PAML")|Figure XXX
*Nucleotide diversity values for BUSCO and MAT genes*|[pi](LLL/pi.csv "pi")|Figure XXX
*Tajima's D values for BUSCO and MAT genes*|[Tajima's D](LLL/tajimaD.csv "Tajima's D")|Figure XXX
*IQTree log files with information to replicate the phylogenetic reconstruction*|[IQTree](LLL/IQTree_logFiles.tar.gz "IQTree")|Figure XXX
*Converted Average Nucleotide Identity (ANI) used for reconstructing a Neighbour-Joining tree*|[ANI](LLL/AllvsAll_distances.meg "ANI")|Figure XXX

### Used command lines

#### ILLUMINA trimming
```
[READ]: read name
trim_galore -q 30 --fastqc -o ./ --paired [READ]_1.fastq.gz [READ]_2.fastq.gz
```
#### GENOME ASSEMBLY
```
[PATH2PacBio]: path to your PacBio reads
[ASSEMBLYNAME]: name of your assembly output
[PATH2ASSEMBLY]: path to your assembly file
[PATH2Illumina]: path to your Illumina reads
[PATH2OUTPUTDIRECTORY]: path to store the output files
[ORGANISMNAME]: the name of your organism of study
[REFASSEMBLY]: genome assembly used as reference
[FOLDERWITHASSEMBLY]: folder containing assembly or assemblies
[GENENAME]: name of the gene
[FOLDERwithLayouts]: contains layouts that will be processed by the scripts to generate the necessary input files to run a program.
```
##### Flye 2.6
```
flye --pacbio-raw [PATH2PacBio].fastq.gz --out-dir [PATH2OUTPUTDIRECTORY] --genome-size 40m --threads 8 -i 2
```
##### Canu 1.9
```
canu -p [ASSEMBLYNAME] -d [PATH2OUTPUTDIRECTORY] genomeSize=40.00m -pacbio-raw [PATH2PacBio].fastq.gz useGrid=0 minReadLength=1000
```
##### MECAT2
```
mecat.pl correct [config_file].txt
mecat.pl assemble [config_file].txt
```
- mecat2 configuration file
```
PROJECT=[ASSEMBLYNAME]
RAWREADS=[PATH2PacBio].fastq
GENOME_SIZE=47260000
THREADS=8
MIN_READ_LENGTH=1000
CNS_OVLP_OPTIONS=""
CNS_OPTIONS="-r 0.6 -a 1000 -c 4 -l 2000"
CNS_OUTPUT_COVERAGE=40
TRIM_OVLP_OPTIONS="-B"
ASM_OVLP_OPTIONS="-n 100 -z 10 -b 2000 -e 0.5 -j 1 -u 0 -a 400"
FSA_OL_FILTER_OPTIONS="--max_overhang=-1 --min_identity=-1"
FSA_ASSEMBLE_OPTIONS=""
USE_GRID=false
GRID_NODE=0
CLEANUP=0
```
##### SMARTdenovo 1.0.0
```
smartdenovo.pl -p [ASSEMBLYNAME] -t 8 -c 1 [PATH2PacBio].fastq > [ASSEMBLYNAME].mak
make -f TF100210M3.mak
```
##### wtdbg2 2.5
```
wtdbg2 -i [PATH2PacBio].fastq -o [ASSEMBLYNAME] -t 8 -x rsII -g 50m
wtpoa-cns -t 8 -i [ASSEMBLYNAME].ctg.lay.gz -fo [ASSEMBLYNAME].ctg.fasta
```
##### Consensus quality by polca
```
polca.sh -a [PATH2ASSEMBLY].fasta -r '[PATH2Illumina]_1.fastq.gz [PATH2Illumina]_2.fastq.gz' -t 16 -m 1G
```
##### Assembly quality by quast 5.0.2
```
quast -t 16 -o [PATH2OUTPUTDIRECTORY] --fungus -l [ASSEMBLYNAME] [PATH2ASSEMBLY]
```
##### PacBio assembly correction using HyPo
```
minimap2 --MD -ax sr -t 16 [PATH2ASSEMBLY] [PATH2Illumina]_1.fq.gz [PATH2Illumina]_2.fq.gz | samtools view -Sb > [ORGANISMNAME]_mapped-sr.bam
samtools sort -@ 16 -o [ORGANISMNAME]_mapped-sr.sorted.bam [ORGANISMNAME]_mapped-sr.bam
minimap2 --MD -ax map-pb -t 16 [PATH2ASSEMBLY][PATH2PacBio].fastq.gz \
| samtools view -Sb > [ORGANISMNAME]_mapped-lg.bam
samtools sort -@ 16 -o [ORGANISMNAME]_mapped-lg.sorted.bam [ORGANISMNAME]_mapped-lg.bam
samtools index [ORGANISMNAME]_mapped-lg.sorted.bam
echo -e "[PATH2Illumina]_1.fq.gz\n[PATH2Illumina]_2.fq.gz" > il_names.txt
hypo -d [PATH2ASSEMBLY].fasta -r @il_names.txt -s 12m -c 83 -b [ORGANISMNAME]_mapped-sr.sorted.bam -B [ORGANISMNAME]_mapped-lg.sorted.bam -p 10 -t 16 -o [ASSEMBLYNAME].CorrectedAssembly.fasta
```
##### RaGOO ultrascaffolding
```
./ragoo.py [PATH2ASSEMBLY] [REFASSEMBLY] -g 10000 -C -s
```
##### Mummer 3.23 genome comparison (inhome python script runMummer_OneGenomevsall_v1.2.py
```
runMummer_OneGenomevsall_v1.2.py -i [FOLDERWITHASSEMBLY] -t [REFASSEMBLY].fasta
```
##### Genome assembly completeness using BUSCO 4.1.2
```
busco -i [PATH2ASSEMBLY] -o [ORGANISMNAME] -l agaricomycetes_odb10 -m geno -c 16
```
##### Genome annotation with MAKER20
```
XXX																	XXX									XXX
```
#### Gene alignments
##### Gene identification in mating regions from Illumina assemblies
```
interproscan.sh -appl pfam,coils -iprlookup -pa -t p -i [STRAINNAME]_[AAfromFGENESH].fas -f tsv -T ./ -dp -o [STRAINNAME]_iprscan
```
##### Amino acid sequence alignment
```
mafft --maxiterate 1000 --genafpair [GENENAME]_aa_NoAligned.fas > [GENENAME]_aa_aln.fas
```
##### Back translation to nucleotides
```
pal2nal.pl [GENENAME]_aa_aln.fas [GENENAME]_CDS_NoAligned.fas -codontable 1 -output fasta > [GENENAME]_CDS_aln.fas
```
##### Removal of codons with gaps
```
trimal -in [GENENAME]_CDS_aln.fasta -out [GENENAME]_CDS_trimal.fas -fasta -gt 1 -block 3
```
#### Species tree reconstruction
##### Maximum-Likelihood individual phylogenetic trees
```
iqtree -s [GENENAME]_CDS_trimal.fas -B 1000 -wbt -T 2 -seed 225494
```
##### Species tree reconstruction using a coalescent model
```
cat *.treefile > BUSCO_ML_best.trees
java -jar astral.5.7.4.jar -s 692 -i BUSCO_ML_best.trees -o Trichaptum_species_pp.tre 2> astral_out.log
```
##### Species tree branch support
```
iqtree -t Trichaptum_species_pp.tre --gcf BUSCO_ML_best.trees --prefix gene_concordance
```
#### Gene statistics
##### Synonymous and nonsynonymous substitution rates
```
python yn00_serially_v1.py -l [FOLDERwithLayouts] -i list_fasta4PAML.txt -c NO -o .
```
### Contact

[<img src="https://www.uv.es/perisnav/Index/twitter-logo.png" width="50"/>](https://linktr.ee/PerisD)
