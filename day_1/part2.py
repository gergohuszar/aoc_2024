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
        
result=[]

nums_a.sort()
nums_b.sort()

for a in nums_a:
    res=nums_b.count(a)
    result.append(res*a)


print(sum(result))
    
