## Large-scale fungal strain sequencing unravels the molecular diversity in mating loci maintained by long-term balancing selection

Assemblies, MATA/MATB regions and source data from Peris et al 2022

**Authors**: David Peris, Dabao Sun Lu, Vilde Bruhn Kinneberg, Ine-Susanne Methlie, Malin Stapnes Dahl, Timothy Y. James, Håvard Kauserud, Inger Skrede

**Journal**: [Plos Genetics 18(3): e1010097](https://doi.org/10.1371/journal.pgen.1010097 "Plos Genetics")

**Year**: 2022

**Abstract**: Balancing selection, an evolutionary force that retains genetic diversity, has been detected in multiple genes and organisms, such as the sexual mating loci in fungi. However, to quantify the strength of balancing selection and define the mating-related genes require a large number of strains. In tetrapolar basidiomycete fungi, sexual type is determined by two unlinked loci, MATA and MATB. Genes in both loci define mating type identity, control successful mating and completion of the life cycle. These loci are usually highly diverse. Previous studies have speculated, based on culture crosses, that species of the non-model genus Trichaptum (Hymenochaetales, Basidiomycota) possess a tetrapolar mating system, with multiple alleles. Here, we sequenced a hundred and eighty strains of three Trichaptum species. We characterized the chromosomal location of MATA and MATB, the molecular structure of MAT regions and their allelic richness. The sequencing effort was sufficient to molecularly characterize multiple MAT alleles segregating before the speciation event of Trichaptum species. Analyses suggested that long-term balancing selection has generated trans-species polymorphisms. Mating sequences were classified in different allelic classes based on an amino acid identity (AAI) threshold supported by phylogenetics. 17,550 mating types were predicted based on the allelic classes. In vitro crosses allowed us to support the degree of allelic divergence needed for successful mating. Even with the high amount of divergence, key amino acids in functional domains are conserved. We conclude that the genetic diversity of mating loci in Trichaptum is due to long-term balancing selection, with limited recombination and duplication activity. The large number of sequenced strains highlighted the importance of sequencing multiple individuals from different species to detect the mating-related genes, the mechanisms generating diversity and the evolutionary forces maintaining them. 

This repository, linked to the TriMAT [Github Repository](https://github.com/PerisD/TriMAT "TriMAT Repository"), contains some of the raw data used to generate Figures and Tables in this publication. Additional raw data can be found in dryad repository DOI: 

**[MAT dryad repository](https://doi.org/10.5061/dryad.fxpnvx0t4 "MAT dryad")**

### Assemblies

Assemblies generated using PacBio and Illumina reads

Specimen|Species|ENA Accession no.
-------|-------|------
TA10106M1|*T. abietinum*|[GCA_910574555](XXX "GCA_910574555")
TF100210M3|*T. fuscoviolaceum*|[GCA_910574455](XXX "GCA_910574455")

[178 SPAdes assemblies generated using Illumina reads](https://doi.org/10.5061/dryad.fxpnvx0t4 "Additional assemblies")

[L15831](https://mycocosm.jgi.doe.gov/Triab1_1/Triab1_1.home.html "L15831 downloaded from JGI")

### Crossing pictures

To test compatible and incompatible MAT alleles we performed crosses and we took pictures to check the generation of clamp connections.

[Macroscopic](https://doi.org/10.5061/dryad.fxpnvx0t4 "Macroscopic pictures of trichaptum crosses")

[Microscopic](https://doi.org/10.5061/dryad.fxpnvx0t4 "Pictures taken under the microscope of the contact zone during trichaptum crosses")

### MATA and MATB regions

MATA and MATB regions were assembled and annotated to extract individual genes and make multiple sequence alignments to perform multiple analyses.

[MATA](https://doi.org/10.5061/dryad.fxpnvx0t4 "MATA regions containing homeodomain genes")

[MATB](https://doi.org/10.5061/dryad.fxpnvx0t4 "MATB regions containing pheromone receptors and pheromones")

[IndividualGeneAlignments](https://doi.org/10.5061/dryad.fxpnvx0t4 "Trimmed individual gene alignments")

### Source data

Raw data used to generate Figures 1-8 and S1-13 in [MAT dryad repository](https://doi.org/10.5061/dryad.fxpnvx0t4 "MAT dryad")

File | Figure | Description
-----|--------|-------------
BUSCO-MAT genes|Figures 1 & S1B|*BUSCO annotation statistics and location on TA10106M1 genome*
dxy|Figure 8|*Absolute divergence statitstic for BUSCO and MAT genes*
Fst|Figure 8|*Relative divergence statitstic for BUSCO and MAT genes*
MKT|Figure 8|*Multilocus Hudson–Kreitman–Aguadé (HKA) test performed with HKAdirect 0.7b*
PAML|Figure 8 and S9|*Average number of synonymous substitutions per synonymous sites (dS) and non-synonymous substitutions per non-synonymous sites (dN) for BUSCO and MAT genes*
pi|Figure 8|*Nucleotide diversity values for BUSCO and MAT genes*
Tajima's D|Figure 8|*Tajima's D values for BUSCO and MAT genes*
IQTree|Figure 7, S1B & S5|*IQTree log files with information to replicate the phylogenetic reconstruction represented in [iTOL](http://itol.embl.de/shared/Peris_D "iTOL"). Dataset to color specimens by species designation can be found at [iTOLColors](https://github.com/PerisD/TriMAT/blob/main/MATregions/Layout_MATpaper_spp.txt "Dataset")*
ANI|Figure 1B, S1A|*Converted Average Nucleotide Identity (ANI) used for reconstructing a Neighbour-Joining tree*

### Supplementary Figure S13

Supplementary [Figure S13](https://journals.plos.org/plosgenetics/article/file?type=supplementary&id=10.1371/journal.pgen.1010097.s013 "Fig S13") was generated using the proteins retrieved from JGI genomes:
1. 1KFG: Fomitiporia mediterranea, Onnia scaura, Phellinidium ferrugineofuscum, Phellinus igniarius, Phellinus viticola, Resinicium bicolor, Sidera vulgaris, Porodaedalea chrysoloma, Porodaedalea niemelaei.

    1.1 Phellopilus nigrolimiatatus: [Sønstebø et al. 2022](https://doi.org/10.1111/mec.16369 "Sønstebø et al 2022") "Population genomics of a forest fungus reveals high gene flow and climate adaptation signatures," Mol Ecol 31, 1963-1979

We are grateful to Francis Martin, Sundy Maurice, Otto Miettinen, Joseph W Spatafora, 1KFG and the 'Metatranscriptomics of Forest Soil Ecosystems' consortia for access to unpublished genome data. The genome sequence data were produced by the US Department of Energy Joint Genome Institute in collaboration with the user community.

2. Published genomes:
    
    3.1 Rickenella fibula: [Korotkin et al. 2018](https://doi.org/10.1002/ajb2.1183 "Korotkin et al 2018") "Stable isotope analyses reveal previously unknown trophic mode diversity in the Hymenochaetales," Am J Bot 105, 1869-1887
    
    3.2 Rickenella mellea: [Krizsán et al. 2019](https://www.sciencedirect.com/science/article/pii/S0168165615300407 "Krizsán et al 2019") "Transcriptomic atlas of mushroom development reveals conserved genes behind complex multicellularity in fungi," Proc. Natl. Acad. Sci. U. S. A. 116, 7409-7418
    
    3.3 Schizopora paradoxa: [Min et al. 2015](https://doi.org/10.1073/pnas.1817822116 "Min et al 2015") "Genome sequence of a white rot fungus Schizopora paradoxa KUC8140 for wood decay and mycoremediation," J. Biotechnol 211, 42-43

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
###### mecat2 configuration file
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
##### Translate nucleotides to amino acids with MEGA/Geneious or using the translate.py script
```
python translate.py -nt [GENENAME]_CDS_trimal.fas -aa [GENENAME]_aa_trimal.fas
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
