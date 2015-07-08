import sys 
import random


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


    for i in range(len(list_of_words) - 2):
        key = (list_of_words[i], list_of_words[(i + 1)])
        value = list_of_words[i+2]
        if key not in bi_grams: 
            bi_grams[key] = []
    
        bi_grams[key].append(value)

   # print bi_grams
    return bi_grams




def make_text(chains):
    """Takes dictionary of markov chains; returns random text."""
    
    
    #next_element = (current_element[1],  next_word)

   # our_sentence = str(current_element) + next_word
    sentence = ''
    current_element = random.choice(chains.keys())

    while len(sentence) < 100:
        
        next_word = random.choice(chains[current_element])
        #sentence += current_element[0] + ' ' + current_element[1] + ' '
         
        actual_current_element = str((current_element[1],  next_word))
        sentence += current_element[0] + ' ' + actual_current_element



    print sentence
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
input_file = sys.argv[1]
chains_dict = make_chains(input_file)

print make_text(chains_dict)