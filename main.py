import utility_functions as uf
import italian_wordle as iw
import english_wordle as ew


# Prints the main menu.
def menu():
    uf.print_msg_box("WORDLE!")
    text = "MENU:\n(1) Italian Wordle\n(2) English Wordle\n(3) Exit"
    print(text)


def main():
    choice = ''
    while choice != 3:
        menu()
        choice = int(input("\n\U0000270F Select a game: "))
        print()
        if choice == 1:
            print("*** ITALIAN WORDLE ***")
            iw.italian_wordle()
        elif choice == 2:
            print("*** ENGLISH WORDLE ***")
            ew.english_wordle()


main()
