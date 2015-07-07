import sys


def make_chains(corpus):
    """Takes input text as string; returns dictionary of markov chains.""" 
    text_file = open(corpus)
    list_of_words = []

    for line in text_file:
        line = line.rstrip()
        word = line.split(" ")
        for lst in word: 
            list_of_words.append(lst)

    bi_grams = {}

    for i in range(len(list_of_words) - 1): 
        bi_grams[(list_of_words[i], list_of_words[(i + 1)])] = []

    for word in bi_grams: 
        bi_grams[word] += 


    # for element in list_of_words:   
        # if list_of_words.index(element) == len(list_of_words) - 1: 
        #     break
        # else: 
        #     element = (element, list_of_words[list_of_words.index(element) + 1])
        #     print element


print make_chains('green-eggs.txt')

def make_text(chains):
    """Takes dictionary of markov chains; returns random text."""

    return "Here's some random text."


# Change this to read input_text from a file, deciding which file should
# be used by examining the `sys.argv` arguments (if neccessary, see the
# Python docs for sys.argv)
'''
input_text = "Some text"

# Get a Markov chain
chain_dict = make_chains(input_text)

# Produce random text
random_text = make_text(chain_dict)

print random_text
'''
