a = "book"
b = "book"
c = "book"

print(id(a))
print(id(b))
print(id(c))
print("-" * 50)
d = ["book_test"]
e = ["book_test"]

print(id(d))
print(id(e))

print("-" * 50)

print(type(a), (type(b)), (type(c)))

print("-" * 50)

a = list()
b = list()
c = list()

print(id(a))
print(id(b))
print(id(c))

print(type(a), (type(b)), (type(c)))

d = str()
e = str()

print(id(d))
print(id(e))

print(type(d), (type(e)))
