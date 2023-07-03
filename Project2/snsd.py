import random
import numpy as np
from copy import deepcopy

n = int(input("학생 수 : "))
k = int(input("조별 학생 수 : "))
arr = []
for i in range(n):
    name, feat = input("이름, 값: ").split()
    arr.append([name, int(feat)])

minstd = 1000
minstdarr = []
for i in range(10000):
    stdarr = []
    random.shuffle(arr)
    for j in range(0, n, k):
        stdarr.append(sum(list(map(lambda x: x[1],arr[j:j+k]))))
    std = np.std(stdarr)
    if minstd > std:
        minstdarr = deepcopy(arr)
        minstd = std

for j in range(0, n, k):
    print(minstdarr[j:j + k])

