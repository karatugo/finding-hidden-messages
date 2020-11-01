import sys
from collections import Counter

def get_all_k_mer(string, k):
   length = len(string)
   return [string[i: i+ k] for i in range(length-k+1)]

s = str(sys.argv[1])
k = int(sys.argv[2])
print(Counter(get_all_k_mer(s, k)))