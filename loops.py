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

print()
print('>>> Find largest number in a list: ')

largest = -1
numbers = [9, 41, 12, 3, 74, 15]
for number in numbers:
    if number > largest:
        largest = number
    print('current max = ', largest)
print('------')
print('max = ', largest)
print()

count = 0
for number in numbers:
    count = count + 1
    print('current count = ', count)
print('------')
print('total count = ', count)
print()

sum = 0
for number in numbers:
    sum = sum + number
    print('running sum = ', sum)
print('------')
print('final sum = ', sum)

count = 0
sum = 0
avg = 0
for number in numbers:
    sum = sum + number
    count = count + 1
    print('current count = ', count)
    print('running sum = ', sum)
print('------')
print('avg = ', sum / count)
