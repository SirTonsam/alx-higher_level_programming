def text_indentation(text):
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    punctuation_marks = [".", "?", ":"]
    result = ""
    for char in text:
        result += char
        if char in punctuation_marks:
            result += "\n\n"
    print(result.strip())
