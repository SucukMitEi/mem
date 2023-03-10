list = [
	# name, fmt, size
	["Int32", "i", 4],
	["UInt32", "I", 4],
	["Int64", "q", 8],
	["UInt64", "Q", 8],
	["String"],
	["Bytes"]
]

names = iter(x[0] for x in list)

attrs = dict()
for col in list[:-2]:
	attrs[col[0]] = {}
	attrs[col[0]]["fmt"] = col[1]
	attrs[col[0]]["size"] = col[2]

Int32 = type('Int32', (object,), attrs.get(next(names), {}))
UInt32 = type('UInt32', (object,), attrs.get(next(names), {}))
Int64 = type('Int64', (object,), attrs.get(next(names), {}))
UInt64 = type('UInt64', (object,), attrs.get(next(names), {}))
String = type('String', (object,), attrs.get(next(names), {}))
Bytes = type('Bytes', (object,), attrs.get(next(names), {}))

Type = Int32 | UInt32 | Int64 | UInt64 | String | Bytes

__all__ = [
	*[i[0] for i in list],
	"Type"
]
