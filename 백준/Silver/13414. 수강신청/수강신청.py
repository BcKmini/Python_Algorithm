import sys
from collections import OrderedDict
input=sys.stdin.readline
K,L=map(int,input().split())
od=OrderedDict()

for _ in range(L):
    s=input().strip()
    if s in od:
        del od[s]
    od[s]=1
cnt=0

for key in od.keys():
    if cnt==K:
        break
    sys.stdout.write(key+"\n")
    cnt+=1
