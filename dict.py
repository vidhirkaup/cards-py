bag = dict()
bag['money'] = 12
bag['candy'] = 3
bag['tissues'] = 80
print(bag)
print('bag[candy] = ', bag['candy'])

bag['candy'] = bag['candy'] + 15
print(bag)

colors_hist = dict()
colors = ['red', 'blue', 'green', 'yellow', 'red', 'blue', 'green', 'yellow', 'red', 'blue', 'green', 'yellow', 'red',
          'blue', 'green', 'yellow', 'red', 'blue', 'green', 'yellow', 'red', 'blue', 'green', 'yellow', 'violet',
          'gold', 'red', 'blue', 'green', 'yellow', 'purple']
for color in colors:
    if color not in colors_hist:
        colors_hist[color] = 1
    else:
        colors_hist[color] = colors_hist[color] + 1
print(colors_hist)

colors_hist = dict()
for color in colors:
    colors_hist[color] = colors_hist.get(color, 0) + 1
print(colors_hist)

fname = input('Enter file name:')
if len(fname) == 0:
    fname = 'clown.txt'
fhandle = open(fname)
word_counter = dict()
words = list()
for line in fhandle:
    words = line.split()
    if len(words) == 0:
        continue
    # print(words)
    for word in words:
        word_counter[word] = word_counter.get(word, 0) + 1
print(word_counter)
print()

# for key in word_counter:
#     print(key, word_counter[key])

print()
count = -1
word = None
for k, v in word_counter.items():
    # print(k, v)
    if v > count:
        count = v
        word = k
print('max(word) = ', word, count)

print()
print(word_counter.items())

sorted_word_counter = sorted(word_counter.items())
print(sorted_word_counter)

print()
print('print in sorted order of keys')
# for k, v in sorted(word_counter.items()):
#     print(k, v)

print()
print('print in sorted order of values')
word_list = list()
for k, v in word_counter.items():
    word_list.append((v, k))
print(word_list[:5])

word_list = sorted(word_list, reverse=True)
print(word_list[:5])

print()
print('>>> print top 10 most common words in a file')
fhandle = open('romeo.txt')
words = list()
words_dict = dict()
for line in fhandle:
    # print(line)
    words = line.split()
    for word in words:
        words_dict[word] = words_dict.get(word, 0) + 1
print(words_dict)

words_list = list()
for k,v in words_dict.items():
    words_list.append((v, k))
print(words_list[:5])

words_list = sorted(words_list, reverse=True)
for v, k in words_list[:10]:
    print(k, v)

# print(sorted([(v, k) for k, v in words_dict.items()], reverse=True)[:10])
