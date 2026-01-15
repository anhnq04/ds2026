# GlusterFS Setup Guide

## Installation on Ubuntu

```bash
# Install GlusterFS server
sudo apt-get update
sudo apt-get install -y glusterfs-server

# Start GlusterFS service
sudo systemctl start glusterd
sudo systemctl enable glusterd
sudo systemctl status glusterd
```

## Create Trusted Pool

Assuming you have 3 nodes: node1, node2, node3

```bash
# On node1, add other nodes to the pool
sudo gluster peer probe node2
sudo gluster peer probe node3

# Check peer status
sudo gluster peer status
```

## Create Distributed Replicated Volume

```bash
# Create directories for bricks on each node
sudo mkdir -p /data/brick1/gv0

# Create volume (replicated across 2 nodes, distributed across 3)
sudo gluster volume create gv0 replica 2 \
    node1:/data/brick1/gv0 \
    node2:/data/brick1/gv0 \
    node3:/data/brick1/gv0 \
    force

# Start the volume
sudo gluster volume start gv0

# Check volume info
sudo gluster volume info gv0
```

## Mount the Volume

```bash
# Create mount point
sudo mkdir -p /mnt/glusterfs

# Mount the volume
sudo mount -t glusterfs node1:/gv0 /mnt/glusterfs

# Verify mount
df -h | grep glusterfs

# Auto-mount on boot (add to /etc/fstab)
echo "node1:/gv0 /mnt/glusterfs glusterfs defaults,_netdev 0 0" | sudo tee -a /etc/fstab
```

## Test the Volume

```bash
# Create test file
echo "Hello GlusterFS" | sudo tee /mnt/glusterfs/test.txt

# Check on other nodes
cat /mnt/glusterfs/test.txt
```
