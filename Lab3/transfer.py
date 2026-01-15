from mpi4py import MPI
import sys

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

if rank == 0:
    # Master process
    if len(sys.argv) < 2:
        print("Usage: mpiexec -n 2 python transfer.py <filename>")
        sys.exit(1)
    
    filename = sys.argv[1]
    try:
        with open(filename, 'rb') as f:
            data = f.read()
        print(f"[Rank 0] Sending file: {filename} ({len(data)} bytes)")
        comm.send({'filename': filename, 'data': data}, dest=1)
        print(f"[Rank 0] File sent successfully!")
    except FileNotFoundError:
        print(f"[Rank 0] Error: File {filename} not found!")
        comm.send(None, dest=1)
else:
    # Worker process
    msg = comm.recv(source=0)
    if msg:
        filename = msg['filename']
        data = msg['data']
        output = f"received_{filename}"
        with open(output, 'wb') as f:
            f.write(data)
        print(f"[Rank 1] File received and saved as: {output} ({len(data)} bytes)")
    else:
        print(f"[Rank 1] No file received")
