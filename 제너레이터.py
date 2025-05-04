def mygen():
    yield 'a'
    yield 'b'
    yield 'c'
    yield 'd'

g = mygen()

print(f"type(g) = {type(g)}")

print(f"next(g) = {next(g)}")
print(f"next(g) = {next(g)}")
print(f"next(g) = {next(g)}")
print(f"next(g) = {next(g)}")


