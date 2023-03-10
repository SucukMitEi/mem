from re import compile

MAPS = '([0-9a-f]+-[0-9a-f]+) ([r-][w-][x-])[ps] [0-9a-f]+ [0-9]+:[0-9]+ [0-9]+(?: +(.*))?'

EXPRESSION = compile(MAPS)
