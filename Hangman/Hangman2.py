import random
from playsound import playsound
from colored import fg,bg,attr

def getword():
    word_list=['Cricket','Football','Volleyball','Tennis']
    word=random.choice(word_list)
    word=word.upper()
    return word

def getword1(word):
    word_list=['Cricket','Football','Volleyball','Tennis']
    listhint=["Hint : The highest number of runs scored in an over is not more than 36.",
               "Hint : During every game, players run an average of 9.65 km.",
               "Hint : This  were first introduced as Olympic sports in 1964. , Most  players jump about 300 times a match. ",
               "Hint : hold!, receive! or take!, an interjection used as a call from the server to his opponent to indicate that he is about to serve."]
    ind=[i for i,values in enumerate(word_list) if values==word.capitalize()]
    for i in ind:
         hint=listhint[i]
    return hint 
def display(tries):

    Man=[ '''
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

    return Man[tries]

def playhangman(word,hint):
    guessed=False
    letters=[]
    wordsguessed=[]
    count=0
    completed="_"*len(word)
    tries=7
    print("Let's Play Hangman !!")
    print(display(tries))
    print(hint)
    print(completed)
    print("\n")   
    while not guessed and tries>0:
        guess=input("%sEnter The Letter or Word\t\t"%(fg('orchid'))).upper()
        if len(guess)==1 and guess.isalpha():
            if guess in letters:
               print("%s%sYou Have Already guessed that letter !!%s"%(fg(1),bg('yellow'),attr('reset')))
               #playsound('C:\\Users\\Yash D Upadhyay\\OneDrive\\Documents\\Hangman\\Sample2.mp3')
               playsound('Sounds/Sample2.mp3')
            elif guess not in word:
                tries=tries-1
                #playsound('C:\\Users\\Yash D Upadhyay\\OneDrive\\Documents\\Hangman\\Sample.mp3')
                playsound('Sounds/Sample.mp3')
                if tries==0:
                    break
                print("%sSorry,Try Again",tries,"%stries left !!\n\n"%(fg('yellow')))
                letters.append(guess)
            else:
                print("Guess Is Correct !!")
                listword=list(completed)
                indices=[i for i,letter in enumerate(word) if letter==guess]
                for index in indices:
                   listword[index]=guess
                completed="".join(listword)
                count=count+1
                if "_" not in completed:
                    print("Great Job You have Correctly guessed The Word !!")
                    #playsound('C:\\Users\\Yash D Upadhyay\\OneDrive\\Documents\\Hangman\\Sample3.mp3')
                    playsound('Sounds/Sample3.mp3')
                    guessed=True
        elif  len(guess)==len(word) and guess.isalpha():
            guess.upper()
            print(word)
            if guess in wordsguessed:
                print("%s%sYou Have Already guessed that letter !!%s"%(fg(1),bg('yellow'),attr('reset')))
                playsound('Sounds/Sample2.mp3')
            elif guess!=word:
                wordsguessed.append(guess)
                tries=tries-1
                playsound('Sounds/Sample.mp3')
                if tries==0:
                    print("OOPS !! ,You Ran Out Of Tries\n\n")
                    break
                print("Sorry,Try Again",tries,"%stries left !!\n\n"%(fg('yellow')))
            else:
                completed=word
                print("Great Job You have Correctly Guessed The Word !!\n\n")
                playsound('Sounds/Sample3.mp3')
                guessed=True
        else:
            print("Invalid Guess !!")
        print(display(tries))
        print(hint)
        print(completed)
        print("\n")
    
    print(display(tries))
    print(hint)
    print(completed)
    print("Want To Play Again? Enter 'Y' to Continue ")




word=getword()
hint=getword1(word)
playhangman(word,hint)
a=input("Enter 'Y' to Play Again !!\t\t").upper()
while a=='Y':
    word=getword()
    hint=getword1(word)
    playhangman(word,hint)
if a!='Y':
    print("Good Luck !!")
