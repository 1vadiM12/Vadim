a = "book"
b = "book"
c = "book"

print(id(a))
print(id(b))
print(id(c))
print("-" * 50)
a = ["book_test"]
b = ["book_test"]

print(id(a))
print(id(b))

print("-" * 50)

print(type(a), (type(b)), (type(c)))

print("-" * 50)

a = ["book"]
b = ["book"]
c = ["book"]

print(id(a))
print(id(b))
print(id(c))

print(type(a), (type(b)), (type(c)))

a = "book_test"
b = "book_test"

print(id(a))
print(id(b))

print(type(a), (type(b)))
