# Lab 6 - GlusterFS Distributed File System

## Overview
Set up and benchmark GlusterFS distributed replicated volume across multiple nodes.

## Files
- `SETUP.md` - Detailed installation and setup guide
- `benchmark.sh` - Performance benchmark script
- `06.glusterfs.tex` - LaTeX report

## Requirements
- Ubuntu/Debian Linux
- Multiple machines (minimum 2, recommended 3)
- Network connectivity between machines
- Root/sudo access

## Quick Start

### 1. Install GlusterFS (on all nodes)
```bash
sudo apt-get update
sudo apt-get install -y glusterfs-server
sudo systemctl start glusterd
sudo systemctl enable glusterd
```

### 2. Create Trusted Pool (on node1)
```bash
sudo gluster peer probe node2
sudo gluster peer probe node3
sudo gluster peer status
```

### 3. Create Volume (on node1)
```bash
# Create brick directories on all nodes first
sudo mkdir -p /data/brick1/gv0

# Create replicated volume
sudo gluster volume create gv0 replica 2 \
    node1:/data/brick1/gv0 \
    node2:/data/brick1/gv0 \
    node3:/data/brick1/gv0 \
    force

# Start volume
sudo gluster volume start gv0
```

### 4. Mount Volume (on all nodes)
```bash
sudo mkdir -p /mnt/glusterfs
sudo mount -t glusterfs node1:/gv0 /mnt/glusterfs
```

### 5. Run Benchmarks
```bash
chmod +x benchmark.sh
./benchmark.sh
```

## Benchmarks

### Small Files Test
- Creates 1000 small files
- Measures accesses per second
- Tests with 1, 2, 3 servers

### Large Files Test
- Creates 100MB test file
- Measures read speed (MB/s)
- Tests with 1, 2, 3 servers

## Expected Performance

| Servers | Small Files (acc/s) | Large Files (MB/s) |
|---------|--------------------|--------------------|
| 1       | ~500               | ~50                |
| 2       | ~800               | ~80                |
| 3       | ~1200              | ~120               |

## Architecture
- **Replication**: 2 copies of each file
- **Distribution**: Data distributed across 3 nodes
- **Fault Tolerance**: Can survive 1 node failure
- **Access**: Standard POSIX interface via FUSE

## Troubleshooting

### Peer probe fails
```bash
# Check firewall
sudo ufw allow 24007/tcp
sudo ufw allow 24008/tcp
sudo ufw allow 49152:49251/tcp
```

### Volume won't start
```bash
# Check brick directories exist
ls -la /data/brick1/gv0

# Check volume status
sudo gluster volume status gv0
```

### Mount fails
```bash
# Install client package
sudo apt-get install glusterfs-client

# Check volume is started
sudo gluster volume info gv0
```

## Features
- ✅ Distributed storage across multiple nodes
- ✅ Data replication for fault tolerance
- ✅ Parallel I/O for better performance
- ✅ Transparent POSIX interface
- ✅ Easy to scale by adding more nodes
