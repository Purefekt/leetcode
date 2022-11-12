import collections

check = ['R33715',
'R33716',
'R33714',
'R33372',
'R33328',
'R32993',
'R32619',
'R32328',
'R33169',
'R33168',
'R32202',
'R32332',
'R32331',
'R32005',
'R32917',
'R32329',
'R32585',
'R32872',
'R32872',
'R32581',
'R32493',
'R32583']

print(len(check))
hashmap = collections.Counter(check)

for k,v in hashmap.items():
    print(k,v)