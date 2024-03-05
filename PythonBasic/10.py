filename = 'input.txt'

with open(filename) as f:
    content = f.read()

print(content)

with open(filename) as f:
    for line in f:
        print(line.rstrip())
    
with open(filename) as f:
    lines = f.readlines()

for line in lines:
    print(line.rstrip())

filenameWrite = 'output.txt'

with open(filenameWrite, 'w') as f:
    f.write("I love programming!\n")









