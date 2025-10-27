"""
Task 3 – Function with Combined Logic
------------------------------------
Write a function `analyze_sentence(text)` that returns:
1. total character count (len)
2. word count (split)
3. whether it contains the word "Python" (case-insensitive)
Return results as a tuple and print summary in main.
"""

def analyze_sentence(text):
    """Return length, word count, and whether 'Python' appears in text."""
    char_count = len(text) #implement function logic
    word_count = len(text.split())
    contains_python = "python" in text.lower()
    return char_count, word_count, contains_python

if __name__ == "__main__":
    sentence = input ("Enter a sentence: ") #read sentence from input, call function, and print results
    chars, words, has_python = analyze_sentence(sentence)

    print(f"Character amount: {chars}")
    print(f"Word amount: {words}")
    print(f"Contains 'Python': {has_python}")
