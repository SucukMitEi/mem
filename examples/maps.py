from mem import MEM
from mem.types import *

proc = MEM(pid=1)

for map in proc.maps:
	print(f"Map: {map}")

	if not map.read or "[" in map.path:
		continue

	print(f'\tPath: map.path')
	print(f'\tRights: {map.rights}')
	print(f"\tInt32: {proc.read(Int32, map.start)}")
	print(f"\tUInt32: {proc.read(UInt32, map.start)}")
	print(f"\tInt64: {proc.read(Int64, map.start)}")
	print(f"\tUInt64: {proc.read(UInt64, map.start)}")
	print(
		f"\tFirst 40 characters of string: {proc.read(String, map.start, 40)}")
	print(f"\tFirst 40 bytes: {proc.read(Bytes, map.start, 40).hex()}")

	print()
