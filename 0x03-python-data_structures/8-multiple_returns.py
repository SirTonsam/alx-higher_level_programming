def multiple_returns(sentence):
    length = len(sentence)  # Get the length of the sentence
    
    if length == 0:
        first = None  # Set first to None if the sentence is empty
    else:
        first = sentence[0]  # Get the first character of the sentence
    
    return length, first  # Return the length and first character as a tuple

