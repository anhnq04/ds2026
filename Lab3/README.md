# MPI File Transfer - Lab 3

## Installation

Install mpi4py (requires MPI implementation):

```bash
# Ubuntu/Debian
sudo apt-get install mpich
pip install mpi4py

# Or use OpenMPI
sudo apt-get install openmpi-bin openmpi-common libopenmpi-dev
pip install mpi4py
```

## Usage

Run with 2 processes (rank 0 = sender, rank 1 = receiver):

```bash
mpiexec -n 2 python transfer.py test.txt
```

## How it works

- **Rank 0** (Master): Reads file and sends to rank 1
- **Rank 1** (Worker): Receives file and saves as `received_<filename>`
