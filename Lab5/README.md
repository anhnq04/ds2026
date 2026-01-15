# Lab 5 - The Longest Path with MapReduce

## Overview
Find the longest file path(s) from multiple input files using MapReduce paradigm.

## Files
- `longest_path.py` - MapReduce implementation
- `paths1.txt` - Sample paths file 1
- `paths2.txt` - Sample paths file 2
- `05.longest.path.tex` - LaTeX report

## Requirements
- Python 3.x
- multiprocessing (built-in)
- glob (built-in)

## How to Run

### Basic Usage
```bash
python longest_path.py paths1.txt
```

### Multiple Files
```bash
python longest_path.py paths1.txt paths2.txt
```

### Using Glob Pattern
```bash
python longest_path.py paths*.txt
```

## Generate Input Files

### On Linux/Mac
```bash
find / > my_paths.txt 2>/dev/null
```

### On Windows
```bash
dir /s /b C:\ > my_paths.txt
```

## Expected Output
```
Longest Path(s) - Length: 67
============================================================
/home/user/downloads/very/long/nested/directory/structure/file.txt
```

## How It Works

1. **Map Phase**: Each path is mapped to (path, length)
2. **Reduce Phase**: Find maximum length and filter all paths with that length
3. **Output**: Display all longest paths

## Algorithm
- **Mapper**: `(path) -> (path, len(path))`
- **Reducer**: `Find max(lengths) -> Filter paths with max length`
- **Time Complexity**: O(N) where N = number of paths
- **Space Complexity**: O(N)

## Features
- ✅ Parallel processing with multiprocessing
- ✅ Support multiple input files
- ✅ Glob pattern support
- ✅ Handles millions of paths efficiently
- ✅ Simple and clean implementation
