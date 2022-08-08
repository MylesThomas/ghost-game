import random
import string

min_word_size = 3

wordlist_filename = "C:/Users/MT23510/OneDrive - Baker Tilly US/Documents/wordlist.txt"

def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    
    return: list
    """
    return [word.rstrip().lower() for word in open(wordlist_filename, 'r') if len(word.rstrip()) >= min_word_size]

# Load the dictionary of words and point to it with 
# the wordlist variable so that it can be accessed from anywhere
# in the program.
wordlist = load_words()

def is_word(s, wordlist):
    if s in wordlist:
        return True
    else:
        return False
        
def is_fragment(s, wordlist):
    for word in wordlist:
        if s in word:
            return False
    return True

def whose_turn(turn):
    if turn%2 == 1:
        return 'Player 1'
    else:
        return 'Player 2'

def valid_move(s):
    if len(s) == 1 and s in string.ascii_letters:
        return True
    else:
        return False
        
def play_again():
    print("Play again? y/n")
    choice = input()
    if choice == 'y':
        ghost()
    elif choice == 'n':
        print("Thanks for playing!")
        exit(0)
    else:
        print("Invalid command!")
        play_again()
        
def add_strike(player, dict_strikes):
    """
    Takes in the player name and the current state of players' strikes. Returns an updated dict if the game is still going. (3 strikes and you're out.)
    
    parameters
    ----------
    player: int
    dict_strikes: dict
    
    return: dict
    """
    print("Invalid move!")
    dict_strikes[player] += 1
    if dict_strikes[player] > 2:
        print(f"{player} loses because they have picked up their 3rd strike. As the saying goes, 3 strikes and you're out!")
        play_again()
    else:
        print(f"{player} now has {dict_strikes[player]} strike(s), and also it is still their turn.")
        print(f"Also, that letter is not added to the word.")
        return dict_strikes

             
def ghost():
    turn_options = [1, 2]
    turn = random.choice(turn_options)
    char = ''
    word = ''
    dict_strikes = {'Player 1': 0, 'Player 2': 0}
    print("Welcome to Ghost!")
 
    while True:
        print(f"It is {whose_turn(turn)}'s turn.")
        
        string_message = f"Current word fragment: {word}" if word != '' else f"Current word fragment: The word is currently blank."
        print(string_message)
        
        char = input()
        char = char.lower().strip()
        
        while valid_move(char) == False:
            print(f"""'{char}' is an invalid entry.
{whose_turn(turn)} does not receive a strike, but must go again.
Please make sure that your input follows these conditions: 
#1: string with length = 1 
#2: letters only""")
            char = input()
            char = char.lower().strip()
        word += char
        
        if len(word) > min_word_size and valid_move(char):
            if is_word(word, wordlist):
                print(f"{word} is a word. {whose_turn(turn)} loses!")
                play_again()
                
            elif is_fragment(word, wordlist):
                print(f"No word begins with {word}.")
                dict_strikes = add_strike(whose_turn(turn), dict_strikes)
                turn -= 1
                word = word[:len(word)-1]
                
        elif len(word) <= min_word_size and valid_move(char):
            if is_fragment(word, wordlist):
                print(f"No word begins with {word}. {whose_turn(turn)} loses!")
                play_again()    
            
        turn += 1

# Run it! 
ghost()
