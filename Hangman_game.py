MAX_TRIES = 7

HANGMAN_ASCII_ART = (
	   """ _   _\
        \n| | | |\
        \n| |_| | __ _ _ __   __ _ _ __ __    __ _ _ __\
        \n|  _  |/ _' | '_ \ / _' | '_ ' _ \ / _' | '_  \
\       \n| | | | (_| | | | | (_| | | | | | | (_| | | | |\
        \n|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|\
        \n                    __/ |\
        \n                   |___/\n\n""")

HANGMAN_PHOTOS = {1 : """\nx-------x""", 
				  2 : """\nx-------x\
						 \n|\
						 \n|\
						 \n|\
						 \n|\
						 \n|""",
				  3 : """\nx-------x\
						 \n|       |\
						 \n|       0\
						 \n|\
						 \n|\
						 \n|""",
				  4 : """\nx-------x\
						 \n|       |\
						 \n|       0\
						 \n|       |\
						 \n|\
						 \n|""",
				  5 : """\nx-------x\
						 \n|       |\
						 \n|       0\
						 \n|      /|\\\
			             \n|\
						 \n|""",
				  6 : """\nx-------x\
						 \n|       |\
						 \n|       0\
						 \n|      /|\\\
			             \n|      /\
						 \n|""",
				  7 : """\nx-------x\
						 \n|       |\
						 \n|       0\
						 \n|      /|\\\
			             \n|      / \\\
			             \n|"""
						 }

def print_open_screen(tries):
	print(HANGMAN_ASCII_ART + str(MAX_TRIES - tries))
	
def print_hangman(num_of_tries):
	print(HANGMAN_PHOTOS[num_of_tries])

def choose_word(file_path, index):
	word_list = list()
	found_list = list()
	count = 0
	with open(file_path, "r") as w_file:
		details = w_file.read().split(" ")
	if(index > len(details)):
		while index > len(details):
			index = index - len(details)
	for item in details:
		if(item not in found_list):
			found_list.append(item)
	word_list.append(len(found_list))
	word_list.append(details[index -1])
	return tuple(word_list)
	
def is_valid_input(letter_guessed):
	return len(letter_guessed) == 1 and letter_guessed.isalpha()

def check_valid_input(letter_guessed, old_letters_guessed):
	return is_valid_input(letter_guessed) and not letter_guessed.lower() in old_letters_guessed

def try_update_letter_guessed(letter_guessed, old_letters_guessed):
	if(check_valid_input(letter_guessed, old_letters_guessed)):
		old_letters_guessed.append(letter_guessed.lower())
		return True
	print("X\n" + " -> ".join(old_letters_guessed))
	return False
	
def show_hidden_word(secret_word, old_letters_guessed):
	find_str = ""
	flag = False
	for letter in secret_word:
		flag = False
		if(letter in old_letters_guessed):
			find_str += letter
			flag = True
		if(flag == False):
			find_str += '_'
	return (" ").join(find_str)

def check_win(secret_word, old_letters_guessed):
	return not '_' in show_hidden_word(secret_word, old_letters_guessed)

def main():
	import os
	import os.path
	os.system('cls')
	old_letters_guessed = list()
	letter_guessed = ""
	num_of_tries = 1
	print_open_screen(num_of_tries)	
	while True:
		path_file = input("Insert The path of words file: ")
		if(os.path.exists(path_file)):
			break
	while True:
		index = int(input("Insert the index of the word you want to discover: "))
		if(index > 0):
			break
	print("Let's Start")
	print_hangman(num_of_tries)
	secret_word = choose_word(path_file, index)[1]
	print(show_hidden_word(secret_word, old_letters_guessed))
	while num_of_tries < MAX_TRIES and not check_win(secret_word, old_letters_guessed):
		letter = input("Guess a letter: ")
		if not is_valid_input(letter) or letter in old_letters_guessed:
			print("X\n" + " -> ".join(old_letters_guessed))
		else:
			letter = letter.lower()
			if try_update_letter_guessed(letter, old_letters_guessed) and letter in secret_word:
				print(show_hidden_word(secret_word, old_letters_guessed))
			else:
				num_of_tries += 1
				print(":(")
				print_hangman(num_of_tries)
				print("\n" + show_hidden_word(secret_word, old_letters_guessed))
	if check_win(secret_word, old_letters_guessed):
		print("WIN")
	else:
		print("LOSE")
	input("Press any key for exit")

if __name__ == "__main__":
    main()



	
	
	
	
	
	
	
	
	
	
	
	

	
	
	
