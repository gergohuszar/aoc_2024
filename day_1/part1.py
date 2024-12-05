import re


regex = re.compile(r'(\d+)   (\d+)')


with open('input.txt') as f:
    lines = f.readlines()


nums_a = []
nums_b = []

for line in lines:
    match = regex.match(line)
    if match:
        a, b = map(int, match.groups())
        nums_a.append(a)
        nums_b.append(b)
        
diffs=[]

nums_a.sort()
nums_b.sort()

for a, b in zip(nums_a, nums_b):
    diffs.append(abs(b-a))


print(sum(diffs))
    
