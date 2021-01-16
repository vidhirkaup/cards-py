import urllib.request, urllib.parse, urllib.error

fhandle = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
count = dict()
for line in fhandle:
    print(line.decode().strip())
    words = line.decode().split()
    for word in words:
        count[word] = count.get(word, 0) + 1
print(count)

print()

fhandle = urllib.request.urlopen('http://www.dr-chuck.com/page1.htm')
for line in fhandle:
    print(line.decode().strip())
