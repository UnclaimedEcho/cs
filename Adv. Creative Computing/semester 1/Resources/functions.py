# file2list
# input: text file name
# output: list of lists [[l1w2, l1w2], [l2w1, l2w2]]

def file2list(file):

    with open(file) as f:
        lines = f.read()

    lines = lines.splitlines()

    list = []

    for line in lines:
        line = line.split()
        list.append(line)

    return list