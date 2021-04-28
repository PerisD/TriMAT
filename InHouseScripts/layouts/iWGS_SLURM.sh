#!/bin/bash
#SBATCH --account=nn9699k
#SBATCH --job-name="iWGS-[STRAINNAME]"
#SBATCH --chdir=[WORKINGDIR]
#SBATCH --ntasks=[CPUs]
#SBATCH --mem=[MEMORY]GB
#SBATCH --time=[TIME]
#SBATCH --mail-type=ALL
#SBATCH --mail-user=david.perisnavarro@gmail.com
#SBATCH --output=SLURM-outputs/Output_%j_%x.out
#SBATCH --error=SLURM-outputs/Output_%j_%x.err

source /cluster/home/davidper/.bashrc
module purge
module load Anaconda2/2019.03
source activate /cluster/projects/nn9699k/Speciomics/Peris/conda_env/iWGS

PYTHONPATH=/cluster/projects/nn9699k/Speciomics/Peris/conda_env/abyss/lib/python2.7/site-packages/:$PYTHONPATH
PYTHONPATH=/cluster/projects/nn9699k/Speciomics/Peris/conda_env/iWGS/lib/python2.7/site-packages/:$PYTHONPATH
PYTHONPATH=/cluster/projects/nn9699k/Speciomics/Peris/conda_env/masurca/lib/python2.7/site-packages/:$PYTHONPATH
export PYTHONPATH


pwd; hostname; date

cd [WORKINGDIR]

[SLURMTEXT]

date


