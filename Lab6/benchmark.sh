#!/bin/bash

# GlusterFS Benchmark Script
# Tests small files (number of accesses/s) and large files (read speed MB/s)

MOUNT_POINT="/mnt/glusterfs"
RESULTS_FILE="benchmark_results.txt"

echo "GlusterFS Benchmark Results" > $RESULTS_FILE
echo "============================" >> $RESULTS_FILE
echo "" >> $RESULTS_FILE

# Test 1: Small files - Number of accesses per second
echo "Test 1: Small File Access Performance" >> $RESULTS_FILE
echo "--------------------------------------" >> $RESULTS_FILE

for num_servers in 1 2 3; do
    echo "Testing with $num_servers server(s)..." >> $RESULTS_FILE
    
    # Create 1000 small files
    start_time=$(date +%s.%N)
    for i in {1..1000}; do
        echo "test" > $MOUNT_POINT/small_$i.txt
    done
    end_time=$(date +%s.%N)
    
    duration=$(echo "$end_time - $start_time" | bc)
    accesses_per_sec=$(echo "1000 / $duration" | bc -l)
    
    echo "  Servers: $num_servers, Accesses/s: $accesses_per_sec" >> $RESULTS_FILE
    
    # Cleanup
    rm -f $MOUNT_POINT/small_*.txt
done

echo "" >> $RESULTS_FILE

# Test 2: Large files - Read speed (MB/s)
echo "Test 2: Large File Read Performance" >> $RESULTS_FILE
echo "------------------------------------" >> $RESULTS_FILE

# Create a 100MB test file
dd if=/dev/zero of=$MOUNT_POINT/large_file.dat bs=1M count=100 2>/dev/null

for num_servers in 1 2 3; do
    echo "Testing with $num_servers server(s)..." >> $RESULTS_FILE
    
    # Clear cache
    sudo sh -c 'echo 3 > /proc/sys/vm/drop_caches'
    
    # Read the file and measure speed
    start_time=$(date +%s.%N)
    dd if=$MOUNT_POINT/large_file.dat of=/dev/null bs=1M 2>/dev/null
    end_time=$(date +%s.%N)
    
    duration=$(echo "$end_time - $start_time" | bc)
    speed_mbs=$(echo "100 / $duration" | bc -l)
    
    echo "  Servers: $num_servers, Speed: $speed_mbs MB/s" >> $RESULTS_FILE
done

# Cleanup
rm -f $MOUNT_POINT/large_file.dat

echo "" >> $RESULTS_FILE
echo "Benchmark completed!" >> $RESULTS_FILE

cat $RESULTS_FILE
