#!/usr/bin/python3
# pylint: disable=missing-function-docstring
# pylint: disable=missing-module-docstring
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# %%
import copy
import importlib.util
import json
import re
import sys
import traceback
# from concurrent.futures import ProcessPoolExecutor, as_completed

import numpy as np
# from torch.multiprocessing import Pool
# from tqdm.auto import tqdm
from pqdm.processes import pqdm
from zlib import compress, compressobj, Z_BEST_COMPRESSION, Z_DEFAULT_STRATEGY, Z_FILTERED, Z_HUFFMAN_ONLY
import zopfli.zlib

sys.path.append("/kaggle/input/google-code-golf-2025/code_golf_utils")
from code_golf_utils import load_examples # noqa: E0401

CODE_PATH = "./Code"
SAMPLES = 400
START_TASK = 1
END_TASK = 400

if "ipykernel" not in sys.argv[0]:
    if len(sys.argv) > 1:
        CODE_PATH = sys.argv[1]
    if len(sys.argv) > 2:
        START_TASK = int(sys.argv[2])
    if len(sys.argv) > 3:
        END_TASK = int(sys.argv[3])
    else:
        # If only one task number given, verify just that task
        if len(sys.argv) > 2:
            END_TASK = START_TASK

    SAMPLES = END_TASK - START_TASK + 1

# %%
def zip_src(src):
    # Try different compression strategies to find the best one
    strategies = [Z_DEFAULT_STRATEGY, Z_FILTERED, Z_HUFFMAN_ONLY]
    best_compressed = None
    best_size = float('inf')

    for strategy in strategies:
        compressor = compressobj(level=Z_BEST_COMPRESSION, strategy=strategy)
        compressed = compressor.compress(src) + compressor.flush()
        if len(compressed) <= best_size:
            best_size = len(compressed)
            best_compressed = compressed

    # Fallback: try simple compress with max level
    simple_compressed = compress(src, Z_BEST_COMPRESSION)
    if len(simple_compressed) <= best_size:
        best_size = len(simple_compressed)
        best_compressed = simple_compressed

    # Try zopfli compression for potentially better compression
    try:
        zopfli_compressed = zopfli.zlib.compress(src)
        if len(zopfli_compressed) <= best_size:
            best_size = len(zopfli_compressed)
            best_compressed = zopfli_compressed
    except Exception:
        # If zopfli fails for any reason, continue with the best result so far
        pass

    # Try deflate compression
    # try:
    #     deflate_compressed = deflate.deflate_compress(src)
    #     if len(deflate_compressed) <= best_size:
    #         best_size = len(deflate_compressed)
    #         best_compressed = deflate_compressed
    # except Exception:
    #     # If deflate fails for any reason, continue with the best result so far
    #     pass

    # We prefer that compressed source not end in a quotation mark
    while best_compressed[-1] == ord('"'):
        src += b"#"
        # Recompress with the best strategy found
        compressor = compressobj(level=Z_BEST_COMPRESSION, strategy=Z_DEFAULT_STRATEGY)
        best_compressed = compressor.compress(src) + compressor.flush()

    def sanitize(b_in):
        """Clean up problematic bytes in compressed b-string"""
        # Use list comprehension for better performance
        result = []
        for b in b_in:
            if b == 0:
                result.extend(b"\\x00")
            elif b == ord("\r"):
                result.extend(b"\\r")
            elif b == ord("\\"):
                result.extend(b"\\\\")
            else:
                result.append(b)
        return bytes(result)

    compressed = sanitize(best_compressed)

    delim = b'"""' if ord("\n") in compressed or ord('"') in compressed else b'"'

    return b"#coding:L1\nimport zlib\nexec(zlib.decompress(bytes(" + \
        delim + compressed + delim + \
        b',"L1")))'

# %%
def zip_single_task(task_number):
    try:
        task_path = f"{CODE_PATH}/task{task_number:03d}.py"
        src = open(task_path, 'rb').read()
        return len(zip_src(src))
    except Exception as e:
        # Return None if there's any error (treat as failure)
        print(f"Error compressing task {task_number}: {e}")
        traceback.print_exc()
        return None

if __name__ == "__main__":
    zipped_lengths = {}

    # Single-threaded version for safety
    from tqdm import tqdm
    for task_num in tqdm(range(START_TASK, END_TASK + 1), desc="Compressing tasks"):
        result = zip_single_task(task_num)
        if result is not None:
            zipped_lengths[task_num] = result

    # torch.multiprocessing version
    # with Pool(processes=4) as pool:
    #     results = list(tqdm(pool.imap(zip_single_task, range(1, SAMPLES + 1)), total=SAMPLES, desc="Compressing tasks"))
    #     zipped_lengths = [result for result in results if result is not None]
    #     zipped_lengths = dict(zip(range(1, SAMPLES + 1), zipped_lengths))

    # Single-threaded version for comparison
    # for task_num in tqdm(range(1, SAMPLES + 1), desc="Compressing tasks"):
    #     result = zip_single_task(task_num)
    #     if result is not None:
    #         zipped_lengths[task_num] = result

    # Sort by descending length
    zipped_lengths = dict(sorted(zipped_lengths.items(), key=lambda item: item[1], reverse=True))

    print(f"Problem-to-length dictionary: {zipped_lengths}")

# %%
