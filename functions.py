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
    print('-------------')
    print('[', instr, ']')


big = max('Hello World')
format_input(big)

small = min('Hello World')
format_input(small)


# Print hello
def greet(lang):
    if lang == 'es':
        format_input('Hola')
    elif lang == 'fr':
        format_input('Bonjour')
    else:
        format_input('Hello')


greet('en')
greet('es')
greet('fr')
