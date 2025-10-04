import random
words=['impossible','imaginary' , 'programming' , 'developer' , 'soniyaisswag' , 'something' , 'backpack']
word= random.choice(words)

word_letters =set(word)

guessed_letters =set()       #to track the values user has entered

tries=7

print('WELCOME TO HANGMAN GAME 🕹🎮🏁 BY SONIYA 🗣 ‼')
print("YOU HAVE TO GUESS🤔💭 ONE LETTER AT A TIME")

while tries > 0 and len(word_letters) > 0 :
#laptop     -->word
#l a p t o ---->> word_letters
#p   ---> guess-letter
# _ _ p _ _ p
      print(f"YOU HAVE {tries} TRIES")
      display_ =' '
      for i in word:
            if i in word_letters:
                    display_ +=' _ '

            elif i in guessed_letters:
                    display_ +=i         

      print('GUESS THE WORD : ',display_)              

      guess =input('ENTER A LETTER-->').lower()

      if len(guess) > 1  :
             print('INVALID LETTER')
             continue
      
      guessed_letters.add( guess)

      if guess in word_letters:
             word_letters.remove(guess)
             print('YAY ! RIGHT GUESS')
             print(' ')
      else :
             tries-=1
             print('OOPS ! WRONG GUESS')
             print(' ')

if len(word_letters) == 0:
       print('HELL YEAHHH! YOU WON🏆🌟👑🏅') 
       print('THE WORD WAS--> ',word)       

else :
       print('OOPS ! YOW LOST🫵🏻🤣LOSER')
       print('THE WORD WAS--> ',word)                  
