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
bin.ART = PATH2bin/art_illumina
bin.pIRS = PATH2bin/pirs
bin.PBSIM = PATH2bin/pbsim
bin.Trimmomatic = PATH2bin/trimmomatic
bin.NextClip = PATH2bin/nextclip
#bin.Lighter = PATH2bin/lighter
bin.Quake = PATH2bin/quake.py
bin.KmerGenie = PATH2bin/kmergenie
#bin.ABYSS = PATH2bin/abyss-pe
bin.ALLPATHS = PATH2bin/RunAllPathsLG
bin.BLASR = PATH2bin/blasr
bin.PBcR = PATH2bin/PBcR
bin.PBDAGCON = PATH2bin/pbdagcon
bin.runCA = PATH2bin/runCA
bin.DISCOVAR = PATH2bin/DiscovarDeNovo
bin.MaSuRCA = PATH2bin/masurca
bin.Platanus = PATH2bin/platanus
bin.SGA = PATH2bin/sga
bin.SOAPdenovo2 = PATH2bin/SOAPdenovo-127mer
bin.SPAdes = PATH2bin/spades.py
bin.dipSPAdes = PATH2bin/dipspades
bin.velveth = PATH2bin/velveth
bin.velvetg = PATH2bin/velvetg
bin.QUAST = PATH2bin/quast
#bin.REAPR = PATH2bin/reapr
bin.bank-transact = PATH2bin/bank-transact
bin.BWA = PATH2bin/bwa
bin.SAMtools = PATH2bin/samtools/
#bin.FASTX = PATH2bin/fastx_reverse_complement
#bin.Metassembler = PATH2bin/metassemble
#bin.FALCON = PATH2bin/fc_run
bin.Canu = PATH2bin/canu
#bin.Minia = PATH2bin/minia
#bin.DBG2OLC = XXX
#bin.Meraculous = PATH2bin/run_meraculous.sh
#bin.Sparc = XXX
