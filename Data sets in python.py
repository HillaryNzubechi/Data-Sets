"""
Data structures are a way of organizing and storing data so that they can be accessed and worked with efficiently
Data sets in python can be referred to as data containers
They define the relationship between the data, and the operations that can be performed on the data
They serve as the primary form of data storage but also as a common container for results returned by algorithms
In programming, data types are important concepts
Variables can store data of different types and different types can do different things
Python has the following data types built-in by default, in these categories:
Text Type:	str
Numeric Types:	int, float, complex
Sequence Types:	list, tuple, range
Mapping Type:	dict
Set Types:	set, frozenset
Boolean Type:	bool
Binary Types:	bytes, bytearray, memoryview
None Type:	NoneType
You can get the data type of any object by using the type() function
Examples are expressed below
"""
print("Below are classes of data types and the last four are known as primitive data types")
x=b"Hello"
print(type(x)) #bytes
x=bytearray(5)
print(type(x)) #bytearray
x=memoryview(bytes(5))
print(type(x)) #memoryview
x=None
print(type(x)) #Nonetype
x=1j
print(type(x)) #complex
x = ["apple", "banana", "cherry"]
print(type(x)) #list
x = ("apple", "banana", "cherry")
print(type(x)) #tuple
x=range(6)
print(type(x)) #range
x = {"name" : "John", "age" : 36}
print(type(x)) #dictionary
x = {"apple", "banana", "cherry"}
print(type(x)) #set
x = frozenset({"apple", "banana", "cherry"})
print(type(x)) #frozenset
x=5
print(type(x)) #int
x=20.5
print(type(x)) #float
x="Hello world"
print(type(x)) #str
x=True
print(type(x)) #bool

"""
Python has four primitive variable:
Intergers:You can use an integer to represent numeric data and, more specifically, whole numbers from negative infinity to infinity
Float:Float stands for floating point number You can use it for rational numbers, usually ending with a decimal figure
Strings:Strings are collections of alphabets, words or other characters In Python you can create strings by enclosing a sequence of characters within a pair of single or double quotes
Bools:This data type can take up the values: True and False, which often makes them interchangeable with the integers 1 and 0.They are useful in conditional and comparison expressions
"""

