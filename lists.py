a = [1, 2, 3]
b = [4, 5, 6]
c = a + b
print(a)
print(b)
print(c)

t = [91, 82, 83, 64, 55, 46, 37, 28, 19]
print(t[2:5])

stuff = list()
print(stuff)
stuff.append('book')
stuff.append(23)
print(stuff)
stuff.append('again')
print(stuff)

print(9 in t)
print(28 in t)
print(20 not in t)

friends = list()
friends.append('Dave')
friends.append('MaK')
friends.append('Adam')
friends.append('Raj')
friends.append('Nathan')
print(friends)
print(friends[0])
friends.sort()
print(friends)
print(friends[0])

print(t)
print(len(t))
print(max(t))
print(min(t))
print(sum(t))
print(sum(t)/len(t))

line_with_space = 'With three words'
print(line_with_space)
words = line_with_space.split()
print(words)
print(len(words))
print(words[0])
for word in words:
    print(word)

line_with_colon = "one:two:three"
print(line_with_colon)
words = line_with_colon.split(':')
print(words)

fhandle=open('mbox.txt')
domains = list()
for line in fhandle:
    if line.startswith('From '):
        # print(line)
        from_words = line.split()
        # print(from_words[1])
        email = from_words[1].split('@')
        # print(email[1])
        domains.append(email[1])
print(domains)
domains.sort()
print(domains)
print(len(domains))

domains = list(dict.fromkeys(domains))
print(domains)
print(len(domains))
