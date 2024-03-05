f_names = ['1.txt', '2.txt', '3.txt', '4.txt', '5.txt']

for name in f_names:
    try:
        with open(name, 'r') as f:
            lines = f.readlines()
    except FileNotFoundError:
        pass
    else:
        num_lines = len(lines)
        msg = "{0} has {1} lines.".format(name, num_lines)
        print(msg)

















