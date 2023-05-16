def frequency_counter(word):
    """
    This function takes the input word as a parameter and returns 
    the frequency of each letter.

    input : word
    return : frequency of each letter
    """
    freq_count = {}
    # counting frequency of each letter
    for letter in word:
        if letter in freq_count:
            freq_count[letter] += 1
        else:
            freq_count[letter] = 1
    return freq_count


def is_valid_string(input_str):
    """
    This function checks if all characters are in same frequency or accepts
    one variation then returns Yes  else No
    input : word
    return : Yes or No
    """
    freq_counts = frequency_counter(input_str)  # count frequency
    freq_counts = sorted(freq_counts.values())  # sort the values

    # if only one unique frequency the returns yes
    if len(set(freq_counts)) == 1:
        return "Yes"
    # If there are exactly two different frequencies and the first frequency is 1
    elif freq_counts[0] == 1 and len(set(freq_counts[1:])) == 1:
        return "Yes"
    # Substract 1 from the highest frequency and check for the validity
    freq_counts[-1] -= 1
    if len(set(freq_counts)) == 1:
        return "Yes"
    else:
        return "No"  # if None of the above conditions met return "No"


print(is_valid_string(input("Enter the input String : ")))
