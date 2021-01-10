import re

# Python Regular Expression Quick Guide
#
# ^        Matches the beginning of a line
# $        Matches the end of the line

# .        Matches any character

# \s       Matches whitespace
# \S       Matches any non-whitespace character

# *        Repeats a character zero or more times
# *?       Repeats a character zero or more times (non-greedy)

# +        Repeats a character one or more times
# +?       Repeats a character one or more times (non-greedy)

# [aeiou]  Matches a single character in the listed set
# [^XYZ]   Matches a single character not in the listed set
# [a-z0-9] The set of characters can include a range

# (        Indicates where string extraction is to start
# )        Indicates where string extraction is to end

handle = open('mbox-short.txt')
lines = list()
for line in handle:
    line = line.rstrip()
    if re.search('^X-\S+:', line):
        print(line)
        lines.append(line)
print(len(lines))

print('-----------------------------')
domains = dict()
handle = open('mbox-short.txt')
for line in handle:
    domain = re.findall('^From .*@([\S]*)[^>]', line)
    if len(domain) > 0:
        domains[domain[0]] = domains.get(domain[0], 0) + 1
print(domains)