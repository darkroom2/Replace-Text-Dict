import random

# split whole file into lines
dictionary = open("dict.txt").read().split('\n')

# TODO: avoid adding empty string to the replacement_list in the tuple. Or filter them out afterwards.
# split lines into pairs: (letter, replacement_list)
dictionary = [(line[0].lower(), line[2:].split(',')) for line in dictionary]

# make dictionary as {letter : random_replacement_from_list}
secure_random = random.SystemRandom()
dictionary = {key: secure_random.choice(value) for (key, value) in dictionary}

# TODO: fix adding spaces when replacing the chars in lines. I don't know why .replace() adds
with open("in.txt", 'r') as infile, open("out.txt", 'a') as outfile:
    for line in infile:
        for src, target in dictionary.items():
            line = line.replace(src, target)
        outfile.write('\n' + line)
