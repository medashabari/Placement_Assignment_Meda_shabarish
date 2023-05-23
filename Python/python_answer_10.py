import nltk
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
from nltk import pos_tag
from nltk.tokenize import word_tokenize 

def count_pos(sentence)->dict:
    """
    This function counts the number of nouns,pronouns,verbs,adjectives
    input: sentence
    output: returns count of each Parts of speech
    """

    words = word_tokenize(sentence) # breaks sentence into words

    pos_tag_words = pos_tag(words) # performs parts of speech operation

    pos_tags_dict = {
        'verbs':0,
        'pronouns':0,
        'nouns':0,
        'adjectives':0
    }

    for word,tag in pos_tag_words:
        if tag.startswith('VB'):
            pos_tags_dict['verbs']+=1
        elif tag.startswith('NN'):
            pos_tags_dict['nouns']+=1
        elif tag.startswith('PRP'):
            pos_tags_dict['pronouns']+=1
        elif tag.startswith('JJ'):
            pos_tags_dict['adjectives']+=1

    return pos_tags_dict


input_sentence = input("Enter a sentence : ")

print(count_pos(input_sentence))