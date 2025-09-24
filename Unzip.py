# %%
import zlib
import re

# %%
DATA_DIR = "./Code"
LIST = [11, 25, 34, 40, 51, 62, 68, 88, 118, 121, 122, 133, 134, 139, 145, 147, 148, 157, 159, 168, 182, 196, 204, 207, 216, 234, 237, 242, 244, 338, 350, 355, 361, 363, 397]

# For each file in LIST, unzip the code in exec(zlib.decompress(code_bytes))
for i in LIST:
    file_name = f"{DATA_DIR}/task{i:03d}.py"
    output_name = f"{DATA_DIR}/task{i:03d}.py"

    # Read with UTF-8 encoding
    with open(file_name, 'r', encoding='utf-8') as f:
        content = f.read()

    print("Successfully read with UTF-8 encoding")

    # Look for any zlib.decompress call
    pattern = r"zlib\.decompress.+"

    match = re.search(pattern, content, re.DOTALL)
    if match:
        full_match = match.group(0)

        # Remove the last parenthesis to get the argument
        if full_match.endswith(')'):
            # eval(match[0][:-1]).decode() - evaluate and decode in one step
            decompressed_code = eval(full_match[:-1]).decode()
            print(f"Successfully decompressed and decoded {len(decompressed_code)} characters")
        else:
            decompressed_code = None
    else:
        #print("Could not find zlib.decompress call")
        decompressed_code = None

    if decompressed_code:
        # Write to output file
        with open(output_name, 'w', encoding='utf-8') as f:
            f.write(decompressed_code)
        print(f"Decompressed code written to {output_name}")
    else:
        print(f"Skipped {file_name}")

# %%
