from struct import pack, unpack
from typing import List

from psutil import process_iter

from .consts import EXPRESSION
from .types import *


class ProcessNotFound(Exception):
	pass


class Map:
	def __init__(self, range_, rights, path):
		start, stop = range_.split('-')
		start, stop = int(start, 16), int(stop, 16)

		self.range = range(start, stop)
		self.size = stop - start

		self.start = start
		self.stop = stop

		self.read = rights[0] != '-'
		self.write = rights[1] != '-'
		self.execute = rights[2] != '-'

		self.rights = rights

		self.path = path

	def __repr__(self):
		return f'Map({self.rights}, {hex(self.start)[2:]}-{hex(self.stop)[2:]}, {self.size} bytes, {self.path})'


class MEM:
	def __init__(self, pid: int):
		self.pid = pid

		self.memfd = None
		self.mapfd = None

		self.maps: List[Map] = []
		self.loadMaps()

	@classmethod
	def fromName(cls, name: str):
		for proc in process_iter():
			if proc.name() == name:
				return cls(proc.pid)

		raise ProcessNotFound(f"Couldn't find process {name}")

	def loadFiles(self):
		if self.memfd and self.mapfd:
			self.memfd.close()
			self.mapfd.close()

		self.memfd = open(f"/proc/{self.pid}/mem", "r+b")
		self.mapfd = open(f"/proc/{self.pid}/maps", "r")

	def loadMaps(self):
		self.loadFiles()

		for match in EXPRESSION.findall(self.mapfd.read()):
			self.maps.append(Map(*match))

	def read(self, type: Type, address, size: int = None):
		self.loadFiles()
		self.memfd.seek(address)

		if type == Bytes:
			return self.memfd.read(size)

		if type == String:
			return self.read(Bytes, address, size).decode(errors="ignore")

		return unpack(type.fmt, self.read(Bytes, address, type.size))

	def write(self, type: Type, address, value):
		self.loadFiles()
		self.memfd.seek(address)

		if type == Bytes:
			return self.memfd.write(value)

		if type == String:
			return self.write(Bytes, address, value.encode())

		return self.write(Bytes, pack(type.fmt, value))
