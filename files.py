print()
print('>>> count lines in a file: ')

fhandle = open('mbox.txt')
line_count = 0
for line in fhandle:
    line_count = line_count + 1
print('number(lines) = ', line_count)

print()
print('>>> file size: ')
fhandle = open('mbox.txt')
file_content = fhandle.read()
print('file(size) = ', len(file_content))
print(file_content[:20])

print()
print('>>> line starts with From: ')
fhandle = open('mbox.txt')
for line in fhandle:
    if line.startswith('From:'):
        print(line.rstrip())

print()
print('>>> ask for file name: ')
fname = input('provide file name:')
try:
    fhandle = open(fname)
except:
    print('not a valid file')
    quit()

for line in fhandle:
    if line.startswith('Subject:'):
        print(line)
