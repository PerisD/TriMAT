#!/bin/bash
#SBATCH --account=XXX
#SBATCH --job-name="fastqc"
#SBATCH --chdir=[WORKINGDIRECTORY]
#SBATCH --ntasks=8
#SBATCH --mem=28GB
#SBATCH --time=12:00:00
#SBATCH --mail-type=ALL
#SBATCH --mail-user=XXX
#SBATCH --output=SLURM-Outputs/Output_%j_%x.out
#SBATCH --error=SLURM-Outputs/Output_%j_%x.err

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

cd [WORKINGDIRECTORY]
