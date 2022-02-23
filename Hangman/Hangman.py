import random
from playsound import playsound
from colored import fg,bg,attr

def get_word():
    word_list=['Cricket','Football','Volleyball','Tennis']
    word=random.choice(word_list)
    word=word.upper()
    return word
def display(tries):

    stages=[ '''
                 |_ _ _ _ _
                 |         |
                 |         O
                 |        /|\\
                 |         |
                 |        / \       
                ___                        
                                 '''
                                    
                
                ,
                '''
                    |_ _ _ _ _
                    |         |
                    |         O
                    |        /|
                    |         |
                    |        / \       
                    __                  '''
                 ,
                 '''
                     |_ _ _ _ _
                     |         |
                     |         O
                     |         |
                     |         |
                     |        / \       
                    __                  
                                        '''
                ,
                '''  
                    |_ _ _ _ _
                    |         |
                    |         O
                    |         |
                    |         |
                    |        /      
                    __             
                                       '''
                ,
                '''
                    |_ _ _ _ __
                    |         |
                    |         O
                    |         |
                    |         |
                    |               
                   __             
                                         '''
                ,
                ''' 
                    |_ _ _ _ _
                    |         |
                    |         O
                    |         |
                    |         
                    |               
                   __              
                                         '''
                            
                ,
                '''
                    |_ _ _ _ _
                    |         |
                    |         O
                    |         
                    |         
                    |               
                   __              
                                          '''
                ,
                '''
                    |_ _ _ _ _
                    |         |
                    |         
                    |         
                    |         
                    |               
                   __               
                                         '''
                 
                
                                         ]

    return stages[tries]

def play(word):
    guessed=False
    guessed_letters=[]
    guessed_word=[]
    count=0
    word_completion="_"*len(word)
    tries=7
    print("Let's Play Hangman !!")
    print(display(tries))
    print(word_completion)
    print("\n")   
    while not guessed and tries>0:
        guess=input("%sEnter The Letter or Word\t\t"%(fg('orchid'))).upper()
        if len(guess)==1 and guess.isalpha():
            if guess in guessed_letters:
               print("%s%sYou Have Already guessed that letter !!%s"%(fg(1),bg('yellow'),attr('reset')))
               playsound('C:\\Users\\Yash D Upadhyay\\OneDrive\\Documents\\Hangman\\Sample2.mp3')
            elif guess not in word:
                tries=tries-1
                playsound('C:\\Users\\Yash D Upadhyay\\OneDrive\\Documents\\Hangman\\Sample.mp3')
                if tries==0:
                    
                    break
                print("%sSorry,Try Again",tries,"%stries left !!\n\n"%(fg('yellow')))
                guessed_letters.append(guess)
            else:
                print("Guess Is Correct !!")
                word_list=list(word_completion)
                indices=[i for i,letter in enumerate(word) if letter==guess]
                for index in indices:
                   word_list[index]=guess
                word_completion="".join(word_list)
                count=count+1
                if "_" not in word_completion:
                    print("Great Job You have Correctly guessed The Word !!")
                    playsound('C:\\Users\\Yash D Upadhyay\\OneDrive\\Documents\\Hangman\\Sample3.mp3')
                    guessed=True
        elif  len(guess)==len(word) and guess.isalpha():
            if guess in guessed_word:
                print("You Have Already Guessed That Word !!\n\n")
            elif guess!=word:
                tries=tries-1
                if tries==0:
                    print("OOPS !! ,You Ran Out Of Tries\n\n")
                    break
                print("Sorry,Try Again ,You have",tries,"tries left !!\n\n")
            else:
                word_completion=word
                print("Great Job You have Correctly Guessed The Word !!\n\n")
                guessed=True
        else:
            print("Invalid Guess !!")
        print(display(tries))
        print(word_completion)
        print("\n")
    
    print(display(tries))
    print(word_completion)
    print("Want To Play Again? Enter 'Y' to Continue ")




word=get_word()
play(word)
a=input("Enter 'Y' to Play Again !!\t\t").upper()
while a=='Y':
    word=get_word()
    play(word)
if a!='Y':
    print("Good Luck !!")
