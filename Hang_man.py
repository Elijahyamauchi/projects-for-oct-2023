#goal: make a hangman sim
#have the user iput a string
#allow the user a set number of guesses to pick the correct letters
#print the guessed letters 
#print the correct letters ex: hamburger h _ m _ _ r g e r
# does not catch instances or the same letter twice
#strech goal: print the hanged man in acordance with the score


#checks to see if ansswer contains more then one character
def len_check (list):  
    return len(list)==1
#checks to see if answer contains a number  
#blockes out if only numbers, passes if mix of numbers and leters
def num_check(list):
    for i in list:
        if i.isdigit():
            return False
        return True

#for finding the position of the guess in the answer
def find_pos (word_list,guess_lower):
    for j in range(len(word_list)):
        if guess_lower==word_list[j]:
            return j
    return -1
def play_again():
    ugh=True
    while (ugh==True):
        choice =input("play again? 'y','n'")
        if choice.lower()=='y':
            return True
        elif choice.lower()=='n':
            return False
        else:
            ugh=True
            print("Invalid entry.")


#univeral variables
word=''
word_list=[]
word_lower= ''
guess=''
guess_lower=''
guess_list=[]   
answer_list=[]
guesses=[]
game_on=True
while game_on==True:
    #for getting the password
    on=True
    chances = 5
    while on==True:
        word=input("Enter the password to save their life.\n")
        word_lower=word.lower() #sets the given word to lower case to make it easier to process
        word_list = [char for char in word_lower]
        if (num_check(word_list)==False):
            print("No numbers alowed.")
        elif (len(word_list)<=0):
            print("The password is too short.")
        else:
            print("The password has been saved.\nPlease pass the computer to the other player.\n\n")
            on=False
    # creates the (_,_,_)
    for i in range(len(word_list)):
        answer_list.append('_')

    #loop for getting the guesses
    on=True
    alive=True
    print ("Welcom player.\nIf you want to save the prisoners life you have to guess the password.")
    while alive==True:
        print(f"you have {chances} chances left.")
        on=True
        while on == True:
            on = True
            print("guesses so far:",guesses)
            print ("Password:",answer_list)
            #add a print (answer list) #done
            guess=input("Plese enter your letter\n")
            guess_lower=guess.lower()
            guess_list=[char for char in guess_lower]
            if (num_check(guess_list)==False):
                print("No numbers alowed.")
            elif (not len_check(guess_list)):
                print("The guess can only be one letter.")           
            else:
                print("your guess is saved")
                on=False
                guesses.append(guess_lower)
            #works, causes an infinite loop #fixed
        if guess_lower in word_list:
            #yes
            print("you got one!\n")
            on=False
            pos=find_pos(word_list,guess_lower)
            #add the alterations to answer_list here
            answer_list[pos]=guess_lower
            if answer_list==word_list:
                print("Congrats! The prisoner was freed!")
                alive=False
                game_on=play_again()

        else:
            #no
            print("Oh no, that wasn't in it.\n")
            chances=chances-1
            #add in a lose condition when chance hits 0 #done
            on=False
            if chances<=0:
                print("\nThe prisoner has died.\n")
                alive=False
                game_on=play_again()
                
