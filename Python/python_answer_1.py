def highest_frequency_count_length(input_sen):
    """
    This function takes the input sentence as a parameter and returns 
    the length of maximum frequency word in the sentence.

    input : input_sen
    output : length maximum repeated frequency word
    """
    words = input_sen.split(" ") # split the sentence into words
    freq_count ={} 
    # counting frequency of each word
    for word in words:
        if word in freq_count:
            freq_count[word]+=1 
        else:
            freq_count[word]=1 
    
    max_frequency = max(freq_count.values()) # max frequency value
    
    max_frequency_words = [word for word,freq in freq_count.items() if freq==max_frequency] # maximum repeated frequency words
    
    return max(len(word) for word in max_frequency_words) # return maximum length of max frequency words
    
length_highest_freq_word=highest_frequency_count_length(input("Enter the sentence : ")) # input
print(length_highest_freq_word)