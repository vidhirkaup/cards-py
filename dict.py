bag = dict()
bag['money'] = 12
bag['candy'] = 3
bag['tissues'] = 80
print(bag)
print('bag[candy] = ', bag['candy'])

bag['candy'] = bag['candy'] + 15
print(bag)


colors_hist = dict()
colors = ['red', 'blue', 'green', 'yellow', 'red', 'blue', 'green', 'yellow', 'red', 'blue', 'green', 'yellow', 'red', 'blue', 'green', 'yellow', 'red', 'blue', 'green', 'yellow', 'red', 'blue', 'green', 'yellow', 'violet', 'gold', 'red', 'blue', 'green', 'yellow', 'purple']
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

word_counter = dict()
words = list()
fhandle = open('random-lines.txt')
for line in fhandle:
    words = line.split()
    if len(words) == 0:
        continue
    # print(words)
    for word in words:
        word_counter[word] = word_counter.get(word, 0) + 1
print(word_counter)
print()

for key in word_counter:
    print(key, word_counter[key])

print()
for k, v in word_counter.items():
    print(k, v)


