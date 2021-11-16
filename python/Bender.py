import sys
import math

prio = ['O', 'N', 'E', 'S']
full_map = list()
m = list()
teleporteurs = list()
casseur = 0
direction = 'S'
pos = (0, 0)
saved = list()

def reverse_prio():
    prio = prio[::-1]

def find_at(l, c):
    for i in range(l):
        for j in range(c):
            if m[i][j] == '@':
                print(f"Find @ at {i}, {j}", file=sys.stderr, flush=True)
                return (i, j)   

def print_m():
    for l in m:
        print(l)

def print_full_m():
    for l in full_map:
        print(l) 


l, c = [int(i) for i in input().split()]

for i in range(l):
    row = input()
    full_map.append([c for c in row])
    m.append([c for c in row[1:-1]])

m.pop(0)
m.pop()

l -= 2
c -= 2

pos = find_at(l, c)
