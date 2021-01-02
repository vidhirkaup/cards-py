print()
print('>>> Basic While loop: ')

x = 5
while x > 0:
    print(x)
    x = x - 1

print('Blast Off')
print(x)

print()
print('>>> While loop with break and continue: ')

# while True:
#     line = input('> ')
#     if line == 'done':
#         break
#     if line == '#':
#         continue
#     print(line)
# print('DONE')

print()
print('>>> Basic For loop: ')

for i in [5, 4, 3, 2, 1]:
    print(i)
print('Blast Off')
print()

friends = ['Adam', 'Bob', 'Charles']
for friend in friends:
    print('Hello ', friend)
print('Done')
