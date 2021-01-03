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

