import utility_functions as uf


# English Wordle.
def english_wordle():
    rw, wl = uf.get_random_word_and_words_list("./dictionaries/english5.txt")
    attempt = 0
    letters_not_present_tot = []
    while attempt < 6:
        uf.print_msg_box("ATTEMPT N° " + str(attempt + 1) + " of 6")
        input_word = input("\U0000270F Enter a word of 5 letters: ").lower()
        while uf.check_not_5_letters(input_word) or uf.check_not_in_list(input_word, wl):
            print("\U000026A0 Word not 5 letters or not existing!!!")
            input_word = input("\U0000270F Enter a word of 5 letters: ").lower()
        current, cw, wp, np = uf.wordle(rw, input_word)
        wrong_letters_pos = []
        wrong_letters_pos.extend(wp)
        wrong_letters_pos = sorted(wrong_letters_pos)
        letters_not_present_tot.extend(np)
        letters_not_present_tot = sorted(list(dict.fromkeys(letters_not_present_tot)))
        print("\U000027A1 Current word: ", current)
        print("• Right letters in the correct position: ", cw)
        print("• Right letters in the wrong position: ", wrong_letters_pos)
        print("• Letters not present in the word: ", letters_not_present_tot)
        print()
        if input_word == rw:
            print("\U00002705 GOOD, you found the correct word \U0001F603")
            print("*" * 50 + "\n")
            break
        attempt = attempt + 1
    if input_word != rw:
        print("\U0000274E Sorry, retry you will be luckier \U0000274E")
        print("\n\U000027A1 The correct word was: " + rw)
        print("*" * 50)