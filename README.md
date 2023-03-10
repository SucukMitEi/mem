# mem

mem is a Python module for reading and writing process memory with Python on Linux.

## Installation instructions

* From a release:
    * Download a release from GitHub 
    * Install the module: `sudo pip install /path/to/release.zip`

* Latest version:
    * Clone the repository: `git clone https://github.com/SucukMitEi/mem`
    * Install the module: `sudo pip install /path/to/mem`



## Example

This is an example how to use the `mem` module.

It opens a process with the process id `12345`
or with the name `process`, reads a 32 bit
integer at address `0x7fffffff` and prints the
result.

```python
from mem import MEM # base class for reading and writing memory
from mem.types import * # required

# open a process

# by process id
proc = MEM(12345)

# by name
proc = MEM.fromName("process") # by name

#  read value
value = proc.read(Int32, 0x7fffffff)

# print value
print(value)
```

# Data types

For reading and writing memory, you need to specify the data type. Here are the data types:
- Int32
- UInt32
- Int64
- UInt64
- Float (coming soon)
- Double (coming soon)
- String
- Bytes

## Running

Run the file with `sudo python3 myfile.py`

## License

This module is licensed under the [MIT](https://choosealicense.com/licenses/mit/) license.
