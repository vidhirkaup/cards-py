print()
print('>>> Prints hello world: ')


def hello():
    print('------')
    print('hello')
    print('world')
    print('------')


hello()
print('zip')
hello()

print()
print('>>> Prints input within parenthesis: ')


def format_input(instr):
    print('-------------')
    print('[', instr, ']')


big = max('Hello World')
format_input(big)

small = min('Hello World')
format_input(small)

print()
print('>>> Greet in different languages: ')


def greet(lang):
    greeting = ''
    if lang == 'es':
        greeting = 'Hola'
    elif lang == 'fr':
        greeting = 'Bonjour'
    else:
        greeting = 'Hello'
    return greeting


format_input(greet('en') + " USA")
format_input(greet('es') + " MEXICO")
format_input(greet('fr') + " FRANCE")
