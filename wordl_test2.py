import random

#def sorting():
#    letter = ["e","t","a","i","n","o","s","h","r","d","l","u","c","m","f","w","y","g","p","b","v","k","q","j","x","z"]
#    guess.find("e")
def game():

    possible_words = []
    
    with open("wordle_library.txt", "r") as file:
        data = file.read()
        words = data.split()
      
    # Generating a random number for word position
        word_pos = random.randint(0, len(words)-1)
        hidden_word = words[word_pos];
        print("Word at position:", words[word_pos])
    
  
        attempt = 6
        while attempt > 0:
            guess = str(input("Guess the word: "))
            if guess == hidden_word:
                print("The word has been guessed properly")
                break
            else:
                attempt = attempt - 1
                print(f"{attempt} attempt(s) remaining ,, \n ")
                
            for char, word in zip(hidden_word, guess):
                if word in hidden_word and word in char:
                    print(word + " ✔ ")
                    char_index_right = guess.index(word)
                    print("the index is",  char_index_right)

                    for i in range(len(words)):
                        #print (i, end = " ")
                        #print (words[i])
                        choice_word = words[i]
                        char_choice_word = choice_word[char_index_right]
                        if char_choice_word == char:
                            possible_words.append(words[char_index_right])
                            print(possible_words)

                elif word in hidden_word:
                        print(word + " ➕ ")
                        char_index_miss = guess.index(word)
                        #print("the index is",  char_index_miss)
                else:
                        print(" ❌ ")
            if attempt == 0:
                print(" No attempts remain.")


game()



    
