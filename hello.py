print('hello world from file')

print('========================')
print('start')
x = 5
if x < 10:
    print('----> small')
if x > 20:
    print('----> big')

print('finish')

print('========================')

y = 5
while y > 0 :
    print(y)
    y = y - 1
print('blast-off')

print('========================')

# name = input('Enter file:')
# handle = open(name, 'r')

# counts = dict()
# for line in handle:
#     words = line.split()
#     for word in words:
#         counts[word] = counts.get(word, 0) + 1

# bigCount = None
# bigWord = None
# for word, count in counts.items():
#     if bigCount is None or count > bigCount:
#         bigWord = word
#         bigCount = count

# print(bigWord, bigCount)

print('========================')

# euroFloor = input('Enter Euro Floor: ')
# usFloor = int(euroFloor)0 + 1
# print('US Floor: ', usFloor)

print('========================')

x = 1
if x > 2 :
    print('big')
else : 
    print('small')

print('========================')

x = 42
if x < 10 :
    print('S')
elif x < 20 :
    print('M')
elif x < 30 :
    print('L')
elif x < 40 :
    print('XL')
else :
    print('XXL')

print('========================')

aStr = 'hello bob'
try:
    ival = int(aStr)
except :
    ival = -1
print(ival)

bStr = '123'
try:
    ival = int(bStr)
except :
    ival = -1
print(ival)

print('========================')

rawstr = input('Enter a number: ')
try : 
    ival = int(rawstr)
except :
    ival = -1

if ival > 0 :
    print('Nice work')
else : 
    print('Not a number')