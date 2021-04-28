#############################
# General options           #
#############################
genome = [REFGENOME]
out_dir = [OUTPUTDIR]
threads = [CPUs]
memory = [MEMORY]

#############################
# Library options
#############################
[LIBRARYTEXT]

#############################
# Simulator options
#############################
pIRS.error_rate =
pIRS.error_profile =
pIRS.gc =
pIRS.gc_profile =
pIRS.indel =
pIRS.indel_profile =

ART.qual_shift1 =
ART.qual_shift2 =
ART.qual_profile1 =
ART.qual_profile2 =
ART.ins_rate1 =
ART.ins_rate2 =
ART.del_rate1 =
ART.del_rate2 =

PBSIM.model_qc = /cluster/home/davidper/software/programs/iWGS/tools/PBSIM/data/model_qc_clr.alyrata
PBSIM.ratio =
PBSIM.accuracy_max =
PBSIM.accuracy_min =
PBSIM.length_mean =
PBSIM.length_sd =
PBSIM.length_max =
PBSIM.length_min =

#############################
# Quality control options
#############################
QC =

Trimmomatic.trailing = 3
Trimmomatic.adapters =
Trimmomatic.minlen = 25

NextClip.adapter =
NextClip.minlen = 25

Correction.tool = Lighter
Correction.kmer =

#############################
# Assembly protocol options
#############################
[PROTOCOLTEXT]

#############################
# Assembler options
#############################
ABYSS.kmer =
ABYSS.option = "l=1 n=5 s=100"

ALLPATHS.ploidy = 2

CA.pbCNS =
CA.sensitive =

Canu.sensitive =

MaSuRCA.kmer =

Meraculous.kmer = 
Meraculous.diploid =

SPAdes.kmer =
SPAdes.multi-kmer =
SPAdes.option = "--only-assembler"

SOAPdenovo2.kmer =
SOAPdenovo2.option = "-F -R -E -w -u"

Velvet.kmer =
Velvet.option = "-exp_cov auto -scaffolding yes"

#############################
# Evaluation options
#############################
QUAST.eukaryote = 1
QUAST.gage = 0 #higher versions of quast does not support the --gage flag
QUAST.gene =

REAPR.libs =

#############################
# Executable options
#############################
bin.ART = /cluster/projects/nn9699k/Speciomics/Peris/conda_env/iWGS/bin/art_illumina
bin.pIRS = /cluster/projects/nn9699k/Speciomics/Peris/conda_env/sppIDer/bin/pirs
bin.PBSIM = /cluster/projects/nn9699k/Speciomics/Peris/conda_env/iWGS/bin/pbsim
bin.Trimmomatic = /cluster/projects/nn9699k/Speciomics/Peris/conda_env/iWGS/bin/trimmomatic
bin.NextClip = /cluster/home/davidper/software/programs/nextclip/bin/nextclip
#bin.Lighter = /home/GLBRCORG/pnavarro/software/Lighter-master/lighter
bin.Quake = /cluster/home/davidper/software/programs/Quake/bin/quake.py
bin.KmerGenie = /cluster/projects/nn9699k/Speciomics/Peris/conda_env/iWGS/bin/kmergenie
#bin.ABYSS = /cluster/projects/nn9699k/Speciomics/Peris/conda_env/abyss/bin/abyss-pe
bin.ALLPATHS = /cluster/projects/nn9699k/Speciomics/Peris/conda_env/iWGS/bin/RunAllPathsLG
bin.BLASR = /cluster/projects/nn9699k/Speciomics/Peris/conda_env/iWGS/bin/blasr
bin.PBcR = /cluster/projects/nn9699k/Speciomics/Peris/conda_env/iWGS/CA8/Linux-amd64/bin/PBcR
bin.PBDAGCON = /cluster/projects/nn9699k/Speciomics/Peris/conda_env/iWGS/bin/pbdagcon
bin.runCA = /cluster/projects/nn9699k/Speciomics/Peris/conda_env/iWGS/CA8/Linux-amd64/bin/runCA
bin.DISCOVAR = /cluster/projects/nn9699k/Speciomics/Peris/conda_env/iWGS/bin/DiscovarDeNovo
bin.MaSuRCA = /cluster/projects/nn9699k/Speciomics/Peris/conda_env/iWGS/bin/masurca
bin.Platanus = /cluster/home/davidper/software/programs/platanus-1.2.4/platanus
bin.SGA = /cluster/projects/nn9699k/Speciomics/Peris/conda_env/iWGS/bin/sga
bin.SOAPdenovo2 = /cluster/projects/nn9699k/Speciomics/Peris/conda_env/iWGS/bin/SOAPdenovo-127mer
bin.SPAdes = /cluster/projects/nn9699k/Speciomics/Peris/conda_env/iWGS/bin/spades.py
bin.dipSPAdes = /cluster/projects/nn9699k/Speciomics/Peris/conda_env/iWGS/bin/dipspades
bin.velveth = /cluster/projects/nn9699k/Speciomics/Peris/conda_env/iWGS/bin/velveth
bin.velvetg = /cluster/projects/nn9699k/Speciomics/Peris/conda_env/iWGS/bin/velvetg
bin.QUAST = /cluster/projects/nn9699k/Speciomics/Peris/conda_env/iWGS/bin/quast
#bin.REAPR = /home/GLBRCORG/pnavarro/software/REAPR/reapr
bin.bank-transact = /cluster/projects/nn9699k/Speciomics/Peris/conda_env/iWGS/bin/bank-transact
bin.BWA = /cluster/projects/nn9699k/Speciomics/Peris/conda_env/iWGS/bin/bwa
bin.SAMtools = /cluster/projects/nn9699k/Speciomics/Peris/conda_env/iWGS/bin/samtools/
#bin.FASTX = /opt/bifxapps/fastx/bin/fastx_reverse_complement
#bin.Metassembler = /home/GLBRCORG/pnavarro/software/Metassembler/bin/metassemble
#bin.FALCON = /cluster/projects/nn9699k/Speciomics/Peris/conda_env/iWGS/bin/fc_run
bin.Canu = /cluster/projects/nn9699k/Speciomics/Peris/conda_env/iWGS/bin/canu
#bin.Minia = /cluster/projects/nn9699k/Speciomics/Peris/conda_env/abyss/bin/minia
#bin.DBG2OLC = /home/GLBRCORG/pnavarro/software/
#bin.Meraculous = /home/GLBRCORG/jacek.kominek/software/meraculous/bin/run_meraculous.sh
#bin.Sparc = /home/GLBRCORG/pnavarro/software/
