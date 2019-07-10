#Hangman game
import random
F=['apple','banana','orange','mango','strawberry','watermelon','kiwi','peach','pear','papaya','grapes','pineapple','guava','blueberry','blackberry','raspberry','apricot']
choice='Y'
while choice=='Y':
    f=random.choice(F)
    lives=5; temp=[];word=[]
    for i in f:
        word.append(i)
        temp.append('_')
    while '_' in temp and lives!=0:
        for i in temp:
            print(i,end=' ')
        print("\t Lives:",lives)
        l=input("Guess a letter: ").lower()
        if l in word:
            for i in range(0,len(word)):
                if word[i]==l:
                    temp[i]=l
        else:
            lives-=1
    if lives==0:
        print("GAME OVER!")
    else:
        print("YOU WIN!!!")
    print("The word was ",f.upper())
    choice=input("Play Again?(y/n) ").upper()
    
    
