from multiprocessing import Pool
from collections import defaultdict
import re

def mapper(line):
    """Map function: emit (word, 1) for each word in line"""
    words = re.findall(r'\b\w+\b', line.lower())
    return [(word, 1) for word in words]

def reducer(word_counts):
    """Reduce function: sum all counts for a word"""
    word, counts = word_counts
    return (word, sum(counts))

def mapreduce(input_file, num_workers=4):
    """Simple MapReduce framework"""
    # Read input
    with open(input_file, 'r') as f:
        lines = f.readlines()
    
    # Map phase (parallel)
    with Pool(num_workers) as pool:
        mapped = pool.map(mapper, lines)
    
    # Flatten results
    flat_mapped = [item for sublist in mapped for item in sublist]
    
    # Shuffle & Sort phase
    shuffled = defaultdict(list)
    for word, count in flat_mapped:
        shuffled[word].append(count)
    
    # Reduce phase (parallel)
    with Pool(num_workers) as pool:
        results = pool.map(reducer, shuffled.items())
    
    return dict(results)

if __name__ == "__main__":
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: python wordcount.py <input_file>")
        sys.exit(1)
    
    input_file = sys.argv[1]
    results = mapreduce(input_file)
    
    # Sort by count (descending)
    sorted_results = sorted(results.items(), key=lambda x: x[1], reverse=True)
    
    print("Word Count Results:")
    print("-" * 40)
    for word, count in sorted_results:
        print(f"{word}: {count}")
