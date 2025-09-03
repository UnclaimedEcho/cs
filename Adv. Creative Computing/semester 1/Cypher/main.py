# turns a text file into a list of lists
# input: file(text file name)
# output: list of lists [[l1w2, l1w2], [l2w1, l2w2]]

def file2list(file):
    output = []

    with open(file) as f:
        lines = f.read()

    lines = lines.splitlines()

    for line in lines:
        line = line.split()
        output.append(line)

    return output

# solves cypher 1
# input: cypher(cypher in list of lists), words(words to decode in lists of lists)
# output: answer in a list

def cypher_1(cypher, words):
    output = []
    for list in cypher:
        line = int(list[0])
        word = int(list[1])
        output.append(words[line][word])
    return output

# solves cypher 1
# input: cypher(cypher in list of lists), words(words to decode in lists of lists)
# output: answer in a list

def cypher_2(cypher, words):
    output = []
    for list in cypher:
        line = int(list[0])
        word = int(list[1])
        letter = int(list[2])
        word = words[line][word]
        output.append(word[letter:])
    return output

# read the files into lists of lists

words = file2list("talk.txt")
cypher1 = file2list("cypher 1.txt")
cypher2 = file2list("cypher 2.txt")


# print the final output as a sentence

print()

for word in cypher_2(cypher2, words):
    print(word, end="")
    print(" ", end = "")
for word in cypher_1(cypher1, words):
    print(word, end="")
    print(" ", end = "")

print(); print()