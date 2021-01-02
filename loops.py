print()
print('>>> While loop: ')

x = 5
while x > 0:
    print(x)
    x = x - 1

print('Blast Off')
print(x)

print()
print('>>> While loop with break and continue: ')

while True:
    line = input('> ')
    if line == 'done':
        break
    if line == '#':
        continue
    print(line)
print('DONE')
