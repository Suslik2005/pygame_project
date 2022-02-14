# map = [[0, 0, 0, 0, 0, 0, 0, 0],
#        [0, 0, 0, 0, 0, 0, 0, 0],
#        [0, 0, 0, 0, 0, 0, 0, 0],
#        [0, 0, 0, 0, 0, 0, 0, 0],
#        [0, 0, 0, 0, 0, 0, 0, 0],
#        [0, 0, 0, 0, 0, 0, 0, 0],
#        [0, 0, 0, 0, 0, 0, 0, 0],
import random
m = []
for i in range(32):
    m.append(i)
    m.append(i)

random.shuffle(m)
map = {}
for i in range(len(m)):
    map[m[i]] = 0
print(map)
