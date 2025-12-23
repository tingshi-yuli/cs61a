import re
import sys

line = sys.stdin.readline().strip()
words = re.split(r'[\s,\.!?]+', line)
words = [w.lower() for w in words if w]
print(len(set(words)))