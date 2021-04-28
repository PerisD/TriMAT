#!/bin/bash
#SBATCH --account=XXX
#SBATCH --job-name="[STRAINNAME]-[ASSEMBLER]"
#SBATCH --chdir=[WORKINGDIRECTORY]
#SBATCH --ntasks=8
#SBATCH --mem=128GB
#SBATCH --time=64:00:00
#SBATCH --mail-type=ALL
#SBATCH --mail-user=XXX
#SBATCH --output=SLURM-outputs/Output_%j_%x.out
#SBATCH --error=SLURM-outputs/Output_%j_%x.err

source PATH2/.bashrc
module purge
module load Anaconda3/2019.03
source activate PATH2/conda_env/circlator

PYTHONPATH=PATH2/conda_env/circlator/lib/python3.6/site-packages/:$PYTHONPATH
export PYTHONPATH

pwd; hostname; date

cd [ASSEMBLERDIR]

canu -p [STRAINNAME] -d ./ genomeSize=50m -pacbio-raw [PACBIOREADS] useGrid=0 minReadLength=1000

date

