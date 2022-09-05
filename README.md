# Solidity Flatliner

Unfolds all local imports in a solidity file to generate a flat solidity file.


## Introduction
Manually combining all imports in a solidity file when verifying your contract source on [Etherscan](https://etherscan.io) is time-consuming and cumbersome. This tool automatically traverses the dependency graph of imports and combines them in the correct order, which is ready to be pasted into the contract verifier. 

> NOTE: This tool won't work with imports that are aliased (i.e. import "./foo.sol" as bar; )

## Features

- [x] support external library folder destination
- [x] support output folder name
- [x] auto remove redundant license place and solidity version code  
- [x] auto remove redundant contract / interface / abstract contract / library
- [x] added support safety line

## Installation

There are no requirements for this tool.

```
pip3 install solflatliner
```
or if you want to get the upgrade
```
sudo pip3 install solflatliner --upgrade
```

### Create bin file for easy execution
```
#!/Library/Frameworks/Python.framework/Versions/3.8/bin/python3.8
# -*- coding: utf-8 -*-
import re
import sys
from solflatliner.cmd import cli
if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw|\.exe)?$', '', sys.argv[0])
    sys.exit(cli())

```

## Usage

```
usage: solflatliner [-h] [-o *.sol] *.sol *.*.*

Unfolds all local imports in a solidity file to generate a flat solidity file.
Put the output file into out/ folders.

positional arguments:
  *.sol                 Target filename with imports
  *.*.*                 Solidity compiler version e.g. 0.4.24

optional arguments:
  -h, --help            Show this help message and exit
  -o *.sol, --output *.sol
                        Output filename (default: flat.sol)
  -f, --ofolder         The output folder (default: verify)
  -lib, --library       Selection of library folder from the execution path. (default: lib)
  -l, --license         The license identifier from https://spdx.org/licenses/ (default: AGPL-3.0)
```

### Example

```
solu contract-with-imports.sol 0.4.24
```
It will output `flat.sol` (default output filename) with solidity version `0.4.24` in `verify/` folder.

```
solflatliner contract-with-imports.sol 0.4.20 --output contract-flat.sol
```
It will output `contract-flat.sol` with solidity version `0.4.20` in `verify/` folder.


### License

MIT License (2022), Jun-You Liu, Heskemo
