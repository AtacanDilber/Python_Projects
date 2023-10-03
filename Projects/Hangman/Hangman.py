secret_word="metallica"
lives=10
guess_string=[]
name=input("Name: ")
print(f"Hello {name} time to play hangman!")
for x in range(1,10):
    print("-")
while lives>0:    
    letter=input("Guess a word: ")
    while letter.isalpha()==False or len(letter)>1:
        print("Invalid input!")
        letter=input("Guess a word: ")
        letter=letter.lower()
    guess_string.append(letter.lower())          
    if letter.lower() not in secret_word:
        lives-=1
        if lives==0:
            print("Wrong!")
            print(f"You have {lives} left")
            print("You died!")
            break
        else:
            print("Wrong!")
            print(f"You have {lives} left")
            for elem in secret_word:
                if elem in guess_string:
                    print(elem)
                else:
                    print("-")                       
    else:
        character_left=0        
        for elem in secret_word:    
            if elem in guess_string:        
                print(elem)        
            else:
                print("-")
                character_left+=1
        if character_left==0:
            print("You won!")
            break
                    
                 
            
                

