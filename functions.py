# Prints hello world
def hello():
    print('------')
    print('hello')
    print('world')
    print('------')


hello()
print('zip')
hello()


# Prints input within parenthesis
def format_input(instr):
    print('[', instr, ']')


big = max('Hello World')
format_input(big)

small = min('Hello World')
format_input(small)
