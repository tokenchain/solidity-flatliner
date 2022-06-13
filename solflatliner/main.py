#!/usr/bin/env python3
import argparse
import os
import re
import sys
from os.path import exists

DESCRIPTION = """
Source Verification Unfolds.\n
Unfolds all local imports in a solidity file to generate a flat solidity file.\n
Put the output file into out/ folders.
"""


def parse_arguments():
    parser = argparse.ArgumentParser(description=DESCRIPTION, formatter_class=argparse.RawTextHelpFormatter)
    parser.add_argument("file", type=str, metavar="*.sol", help="target filename with imports")
    parser.add_argument("version", type=str, metavar="*.*.*", help="solidity compiler version e.g. 0.4.24")
    parser.add_argument("-o", "--output", type=str, metavar="*.sol", help="output filename (default: flat.sol)")
    parser.add_argument("-d", "--ofolder", type=str, metavar="*", help="output folder (default: verify)", default="verify")
    parser.add_argument("-lib", "--library", type=str, metavar="*", help="reference library folder (default: lib)", default="lib")
    args = parser.parse_args()
    return args


def is_sol_valid(infile, s):
    if ".sol" != infile[-4:]:
        print("{} file is not a solidity file!!!".format(s))
        sys.exit(-2)


def unfold_imports(library_folder: str, imports: list, infile: str, importline: str = ""):
    buffer = []

    if infile not in imports:

        found = exists(infile)

        if not found:
            if importline == "":
                print(f"There is no file found from the given path {infile}")
                sys.exit(-5)
            else:
                infile = os.path.join(library_folder, importline)

        try:
            with open(infile, "r+") as f:
                for line in f:
                    # Remove the pragma line in all imports
                    if "pragma" in line[:6]:
                        continue
                    # Remove the LICENSE line in all imports
                    if "//" in line[:2] and "SPDX-License-Identifier:" in line:
                        continue

                    # Read the imports
                    if "import" in line[:6]:
                        match = re.search(r".*[\'|\"](.*)[\'|\"]", line)
                        if match:
                            dirname = os.path.dirname(infile)
                            importline = match.group(1)
                            file = os.path.join(dirname, importline)
                            absfile = os.path.abspath(file)
                            buffer.append(unfold_imports(library_folder, imports, absfile, importline))
                            imports.append(absfile)
                        else:
                            print("There's syntax error of import in {}".format(infile))
                            sys.exit(-3)
                    else:
                        buffer.append(line)

        except FileNotFoundError:
            print(f"There is no file found from the given path {infile}")
            sys.exit(-5)

    return ''.join(buffer)


def main():
    # Read arguments
    args = parse_arguments()
    # Check if the solidity compiler version format is valid
    match = re.search(r"\d+\.\d+\.\d+", args.version)
    if not match:
        print("Compiler version is not a valid format")
        sys.exit(-1)
    # Check if the input solidity filename is valid
    is_sol_valid(args.file, "Input")
    dirname = os.path.dirname(os.path.abspath(args.file))
    basename = os.path.basename(os.path.abspath(args.file))
    # Check if the output solidity filename is valid
    if not args.output:
        args.output = basename[:-4] + "-flat.sol"
    is_sol_valid(args.output, "Output")
    # Make output folder
    OUTPUT_FOLDER = f"{args.ofolder}/"
    if not os.path.exists(OUTPUT_FOLDER):
        os.makedirs(OUTPUT_FOLDER)
    infile = args.file
    outfile = os.path.join(OUTPUT_FOLDER, args.output)
    # output file and input file
    imports = []
    with open(outfile, "w+") as f:
        f.write("pragma solidity ^{};\n".format(args.version))
        f.write("// SPDX-License-Identifier: agpl-3.0\n")
        f.write(unfold_imports(args.library, imports, os.path.abspath(infile)))

    print("🥡 Success! Output: {} in the {} folder".format(os.path.basename(outfile), OUTPUT_FOLDER))


if __name__ == "__main__":
    main()
