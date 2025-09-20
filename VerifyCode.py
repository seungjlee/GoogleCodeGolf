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

sys.path.append("/kaggle/input/google-code-golf-2025/code_golf_utils")
from code_golf_utils import load_examples # noqa: E0401

CODE_PATH = "./Code/"
SAMPLES = 400

if "ipykernel" not in sys.argv[0]:
    if len(sys.argv) > 1:
        CODE_PATH = sys.argv[1]
    if len(sys.argv) > 2:
        SAMPLES = int(sys.argv[2])

# %%
def simple_verify_program(task_path, examples, task_number=None):
    # Use unique module name to avoid conflicts between threads
    task_name = f"task_with_imports_{task_number}_{id(task_path)}" if task_number else "task_with_imports"
    spec = importlib.util.spec_from_file_location(task_name, task_path)
    if spec is None:
        print("Error: Unable to import task.py.")
        return
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    if not hasattr(module, "p"):
        print("Error: Unable to locate function p() in task.py.")
        return
    program = getattr(module, "p")
    if not callable(program):
        print("Error: Function p() in task.py is not callable.")
        return

    def verify(example_subset):
        right, wrong, expected, error = 0, 0, None, ""
        for example in example_subset:
            example_copy = copy.deepcopy(example)
            try:
                result = program(example_copy["input"])
                result = json.dumps(result)
                result = result.replace("true", "1").replace("false", "0")
                unsafe_chars = re.compile(r"[^0-9,\[\]\s\.]")
                if unsafe_chars.search(result):
                    raise ValueError(f"Invalid output from user code: {result[:500]}")
                result = json.loads(result)
                user_output = np.array(result)
                label_output = np.array(example_copy["output"])
                if np.array_equal(user_output, label_output):
                    right += 1
                else:
                    expected = copy.deepcopy(example)
                    wrong += 1
            except:
                error = traceback.format_exc()
                wrong += 1
                #if error: print(f"Error: {error}")
        return right, wrong, expected

    arc_agi_right, arc_agi_wrong, arc_agi_expected = verify(examples["train"] + examples["test"])
    arc_gen_right, arc_gen_wrong, arc_gen_expected = verify(examples["arc-gen"])
    #print(f"Results on ARC-AGI examples: {arc_agi_right} pass, {arc_agi_wrong} fail")
    #print(f"Results on ARC-GEN examples: {arc_gen_right} pass, {arc_gen_wrong} fail")
    return arc_agi_right, arc_agi_wrong, arc_gen_right, arc_gen_wrong

# %%
def verify_single_task(task_number):
    """Verify a single task and return the task number if it fails"""
    try:
        task_path = f"{CODE_PATH}/task{task_number:03d}.py"
        examples = load_examples(task_number)
        agi_right, agi_wrong, agen_right, gen_wrong = simple_verify_program(task_path, examples, task_number)

        if agi_wrong + gen_wrong > 0:
            return task_number
        return None
    except Exception as e:
        # Return task number if there's any error (treat as failure)
        return task_number

failures = []

# pqdm version (clean parallel processing with progress bar)
results = pqdm(range(1, SAMPLES + 1), verify_single_task, n_jobs=4, desc="Verifying tasks")
failures = [result for result in results if result is not None]
failures.sort()

# ProcessPoolExecutor version for comparison
# with ProcessPoolExecutor(max_workers=4) as executor:
#     futures = [executor.submit(verify_single_task, task_num) for task_num in range(1, SAMPLES + 1)]
#     for future in tqdm(as_completed(futures), total=len(futures), desc="Verifying tasks"):
#         result = future.result()
#         if result is not None:
#             failures.append(result)
#     failures.sort()

# torch.multiprocessing version
# with Pool(processes=4) as pool:
#     results = list(tqdm(pool.imap(verify_single_task, range(1, SAMPLES + 1)), total=SAMPLES, desc="Verifying tasks"))
#     failures = [result for result in results if result is not None]
#     failures.sort()

# Single-threaded version for comparison
# for task_num in tqdm(range(1, SAMPLES + 1), desc="Verifying tasks"):
#     result = verify_single_task(task_num)
#     if result is not None:
#         failures.append(result)

print(f"Failures: {failures}")

# %%
