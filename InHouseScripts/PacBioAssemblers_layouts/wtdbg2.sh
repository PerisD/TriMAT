#!/bin/bash
#SBATCH --account=XXX
#SBATCH --job-name="[STRAINNAME]-[ASSEMBLER]"
#SBATCH --chdir=[WORKINGDIRECTORY]
#SBATCH --ntasks=8
#SBATCH --mem=64GB
#SBATCH --time=64:00:00
#SBATCH --mail-type=ALL
#SBATCH --mail-user=XXX
#SBATCH --output=SLURM-outputs/Output_%j_%x.out
#SBATCH --error=SLURM-outputs/Output_%j_%x.err

source PATH2/.bashrc
module purge
module load Anaconda2/2019.03
source activate PATH2/conda_env/iWGS

PYTHONPATH=PATH2/conda_env/abyss/lib/python2.7/site-packages/:$PYTHONPATH
PYTHONPATH=PATH2/conda_env/iWGS/lib/python2.7/site-packages/:$PYTHONPATH
PYTHONPATH=PATH2/conda_env/masurca/lib/python2.7/site-packages/:$PYTHONPATH
export PYTHONPATH

PERL5LIB=PATH2/conda_env/iWGS/lib/site_perl/5.26.2:$PERL5LIB
PERL5LIB=PATH2/conda_env/iWGS/lib/site_perl/5.26.2/x86_64-linux-thread-multi:$PERL5LIB
PERL5LIB=PATH2/conda_env/mummer/lib/site_perl/5.26.2:$PERL5LIB
PERL5LIB=PATH2/conda_env/mummer/lib/site_perl/5.26.2/x86_64-linux-thread-multi:$PERL5LIB
PERL5LIB=PATH2/conda_env/sppIDer/lib/site_perl/5.26.2:$PERL5LIB
PERL5LIB=PATH2/conda_env/sppIDer/lib/site_perl/5.26.2/x86_64-linux-thread-multi:$PERL5LIB
PERL5LIB=PATH2/conda_env/abyss/lib/site_perl/5.26.2:$PERL5LIB
PERL5LIB=PATH2/conda_env/abyss/lib/site_perl/5.26.2/x86_64-linux-thread-multi:$PERL5LIB
export PERL5LIB

pwd; hostname; date

cd [ASSEMBLERDIR]

wtdbg2 [PACBIOREADS] \
-o [STRAINNAME] -t 8 -x rsII -g 50m
wtpoa-cns -t 8 -i [STRAINNAME].ctg.lay.gz -fo [STRAINNAME].ctg.fasta

date
