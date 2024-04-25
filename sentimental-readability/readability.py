from cs50 import get_string

txtinpt = get_string("Please enter your text for evaluation: ")

nr_letters = 0
nr_words = 1
nr_sentences = 0

# nr_letters
for char in txtinpt:
    if char.isalpha():
        nr_letters += 1

# nr_words
for char in txtinpt:
    if char == " ":
        nr_words += 1

# nr_sentences
for char in txtinpt:
    if char in (".", "?", "!"):
        nr_sentences += 1

L = nr_letters * 100 / nr_words
S = nr_sentences * 100 / nr_words

index = int(round(0.0588 * L - 0.296 * S - 15.8, 0))

if index < 1:
    print("Before Grade 1")
elif index > 16:
    print("Grade 16+")
else:
    print(f"Grade {index}")
