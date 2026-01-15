from multiprocessing import Pool

def mapper(line):
    """Map function: emit (path, length) for each path"""
    path = line.strip()
    return (path, len(path))

def reducer(path_lengths):
    """Reduce function: find maximum length"""
    return max(path_lengths, key=lambda x: x[1])

def mapreduce_longest_path(input_files, num_workers=4):
    """MapReduce to find longest path(s)"""
    all_lines = []
    
    # Read all input files
    for input_file in input_files:
        try:
            with open(input_file, 'r') as f:
                all_lines.extend(f.readlines())
        except FileNotFoundError:
            print(f"Warning: {input_file} not found, skipping...")
    
    # Map phase (parallel)
    with Pool(num_workers) as pool:
        mapped = pool.map(mapper, all_lines)
    
    # Reduce phase: find max length
    if not mapped:
        return None, 0
    
    max_length = max(mapped, key=lambda x: x[1])[1]
    
    # Find all paths with max length
    longest_paths = [path for path, length in mapped if length == max_length]
    
    return longest_paths, max_length

if __name__ == "__main__":
    import sys
    import glob
    
    if len(sys.argv) < 2:
        print("Usage: python longest_path.py <input_file1> [input_file2] ...")
        print("   or: python longest_path.py 'pattern*.txt'")
        sys.exit(1)
    
    # Support glob patterns
    input_files = []
    for arg in sys.argv[1:]:
        files = glob.glob(arg)
        if files:
            input_files.extend(files)
        else:
            input_files.append(arg)
    
    longest_paths, max_length = mapreduce_longest_path(input_files)
    
    if longest_paths:
        print(f"Longest Path(s) - Length: {max_length}")
        print("=" * 60)
        for path in longest_paths:
            print(path)
    else:
        print("No paths found!")
