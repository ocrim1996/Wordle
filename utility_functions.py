import random


# Prints a message into a box.
def print_msg_box(msg, indent=1, width=None, title=None):
    """Print message-box with optional title."""
    lines = msg.split('\n')
    space = " " * indent
    if not width:
        width = max(map(len, lines))
        box = f'╔{"═" * (width + indent * 2)}╗\n'  # upper_border
        if title:
            box += f'║{space}{title:<{width}}{space}║\n'  # title
            box += f'║{space}{"-" * len(title):<{width}}{space}║\n'  # underscore
        box += ''.join([f'║{space}{line:<{width}}{space}║\n' for line in lines])
        box += f'╚{"═" * (width + indent * 2)}╝'  # lower_border
        print(box)


# Returns a random word from a txt file and returns all words list of this txt file.
def get_random_word_and_words_list(file_path):
    words_list = []
    with open(file_path, "r") as read_file:
        for line in read_file:
            word = line.strip()
            words_list.append(word)
    random_word = words_list[random.randint(0, len(words_list))]
    return random_word, words_list


# Checks if the word is not five letters.
def check_not_5_letters(word):
    if len(word) != 5:
        return True
    else:
        return False


# Checks if word is not in the words list (of txt file).
def check_not_in_list(word, words_list):
    if word not in words_list:
        return True
    else:
        return False


# Returns the frequency of the letters of a word.
def get_freq(word):
    freq = {}
    for i in word:
        if i in freq:
            freq[i] += 1
        else:
            freq[i] = 1
    freq = dict(sorted(freq.items()))
    return freq


# Main method of the Wordle game.
def wordle(w, word):
    right_positions = []
    wrong_positions = []
    letters_not_present = []
    w_freq = get_freq(w)
    word_freq = get_freq(word)
    current = ""
    new_w = w
    for i in range(len(w)):
        if word[i] == w[i]:
            right_positions.append(word[i])
            current = current + " " + word[i]
            new_w = new_w.replace(w[i], "")
            if word[i] not in new_w and word[i] in wrong_positions and w_freq[word[i]] != word_freq[word[i]]:
                wrong_positions.remove(word[i])
                letters_not_present.append(word[i])
        elif word[i] in w and word[i] in new_w and w_freq[word[i]] == word_freq[word[i]]:
            wrong_positions.append(word[i])
            current = current + " _ "
        elif word[i] in w and word[i] in new_w and w_freq[word[i]] != word_freq[word[i]]:
            wrong_positions.append(word[i])
            current = current + " _ "
            wrong_positions_freq = get_freq(wrong_positions)
            if wrong_positions_freq[word[i]] != w_freq[word[i]]:
                wrong_positions.remove(word[i])
                letters_not_present.append(word[i])
        else:
            letters_not_present.append(word[i])
            current = current + " _ "
    letters_not_present = list(dict.fromkeys(letters_not_present))
    return current, right_positions, wrong_positions, letters_not_present
