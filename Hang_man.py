#goal: make a hangman sim
#have the user iput a string
#allow the user a set number of guesses to pick the correct letters
#print the guessed letters 
#print the correct letters ex: hamburger h _ m _ _ r g e r
#strech goal: print the hanged man in acordance with the score


#checks to see if ansswer contains more then one character
def len_check (list):  
    return len(list)==1
#checks to see if answer contains a number  // note to self, turn these into functions
#blockes out if only numbers, passes if mix of numbers and leters
def num_check(list):
    for i in list:
        if i.isdigit():
            return False
        return True
#univeral variables
word=''
word_list=[]
word_lower= ''
guess=''
guess_lower=''
guess_list=[]   

on=True
chances = 5
while on==True:
    word=input("Enter the password to save their life.\n")
    word_lower=word.lower() #sets the given word to lower case to make it easier to process
    word_list = [char for char in word_lower]
    #make sure to add in the number check thats in the guess code
    if (num_check(word_list)==False):
        print("No numbers alowed.")
    elif (len(word_list)<=0):
        print("The password is too short.")
    else:
        print("The password has been saved.\nPlease pass the computer to the other player.\n\n")
        on=False

on=True
alive=True
print ("Welcom player.\nIf you want to save the prisoners life you have to guess the password.")
while alive==True:
    print(f"you have {chances} chances left.")
    while on == True:
        guess=input("Plese enter your letter")
        guess_lower=guess.lower()
        guess_list=[char for char in guess_lower]
        if (num_check(guess_list)==False):
            print("No numbers alowed.")
        elif (len(guess_list)<=0):
            print("The guess is too short.")
        else:
            print("your guess is saved")
            on=False
    #works, causes an infinite loop
    if guess_lower in word_list:
        print ("yes")
    else:
        print("no")




