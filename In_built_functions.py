# abs() - absolute.
x = abs(-88.96745354)
print(x)

# print if it is true. all()
inp = [12, "Sameer", True]
x = all(inp)
print(x)

# any() - print if any of the values is true.
inp1 = [0, 0, 0]
x = any(inp1)
print(x)

# bin() - returns the binary value of the given input.
x = bin(56)
print(x)

# bool() - returns if it is true or else false.
x = bool(0)
print(x)

# bytearray() - returns a byte with using of an array.
x = bytearray(3)
print(x)

# bytes() - returns a bytes of a value without an array.
x = bytes(4)
print(x)

# chr() - returns a chr of giving an input of unicode.
x = chr(87)
print(x)

# compile() & exec() - compile and execute the given input.
x = compile("print(55)", "test", "eval")
exec(x)

# format() - formats the specified value using this method.
x = format(0.5, "%")
print(x)

# id() - returns the id of a given input.
x = ("apple", "banana", "cherry")
y = id(x)
print(y)

# hex() - converts a number as an hexdecimal value.
x = hex(14)
print(x)

# iter() - create an iterator and prints the items.
# next() - retruns the next items as an iterable.
x = iter({"Sameer", "Dhanush", "Pradeep"})
print(next(x))
print(next(x))
print(next(x))
# print(iter(x))

