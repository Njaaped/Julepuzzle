import random
from nltk.corpus import words

# Load a Norwegian word list (you can use an external list if necessary)
norwegian_word_list = set()  # Replace this with a proper set of Norwegian words
# Example: norwegian_word_list = {"jul", "nisse", "det", "og", "er", ...}

def generate_norwegian_letters_with_word(word="JULENISSEN", n=1000):
    norwegian_alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    remaining_length = n - len(word)
    random_letters = []

    # Generate random letters while avoiding forming real words
    for _ in range(remaining_length):
        while True:
            char = random.choice(norwegian_alphabet)
            potential_sequence = ''.join(random_letters[-2:] + [char])
            # Ensure the potential sequence does not form real words
            if potential_sequence not in norwegian_word_list:
                random_letters.append(char)
                break

    # Insert the word into a random position in the sequence
    position = random.randint(0, remaining_length)
    sequence = ''.join(random_letters[:position]) + word + ''.join(random_letters[position:])
    return sequence

# Generate a string where "JULENISSEN" is the only word
random_sequence = generate_norwegian_letters_with_word()
print(random_sequence)
