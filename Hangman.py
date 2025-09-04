from random import choice

words = ['counselor', 'dinosaur', 'heliport', 'breakfast', 'entrepreneur']
correct_letters = []
incorrect_letters = []
tries = 6
right_answers = 0
game_over = False

def choose_word(list_of_words):
    chosen_word = choice(list_of_words)
    different_letters = len(set(chosen_word)) #set makes sure duplicate letters are not counted.

    return chosen_word, different_letters

def ask_letter():
    chosen_letter = ''
    is_valid = False
    alphabet = 'abcdefghijklmnopqrstuvwxyz'

    while not is_valid: #is valid is true.....
        chosen_letter = input('Please enter a letter: ')

        if chosen_letter in alphabet and len(chosen_letter) == 1:
            is_valid = True
        else:
            print("Please enter a valid letter.")#if number or something else is entered this is printed.


    return chosen_letter

def show_new_board(chosen_word):
    hidden_list = []

    for l in chosen_word:
        if l in correct_letters:
            hidden_list.append(l)
        else:
            hidden_list.append('-')

    print(' '.join(hidden_list))

def check_letter(chosen_letter, hidden_word, tries, matches):
    end = False

    if chosen_letter in hidden_word:
        correct_letters.append(chosen_letter)
        matches += 1

    else:
        incorrect_letters.append(chosen_letter)
        tries -= 1

    if tries == 0:
        end = lose()
    elif matches == unique_letters:
        end = win(hidden_word)

    return tries,end,matches

def lose ():
    print("You don't have any tries.")
    print("The hidden word was " + word)

    return True

def win(revealed_word):
    show_new_board(revealed_word)
    print("Congratulations, you guessed the word!")

    return True

word, unique_letters = choose_word(words)

while not game_over:
    print('\n' + '*' * 20 + '\n')
    show_new_board(word)
    print('\n')
    print('Incorrect letters:' + '-'.join(incorrect_letters))
    print(f'Tries left: {tries}')
    print('\n' + '*' * 20 + '\n')
    letter = ask_letter()
    tries, over, right_answers = check_letter(letter, word, tries, right_answers)
    game_over = over







