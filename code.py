#Hangman game
import random
Friut_list=['apple','banana','orange','mango','strawberry','watermelon','kiwi','peach','pear','papaya','grapes','pineapple','guava','blueberry','blackberry','raspberry','apricot']
choice='Y'
while choice=='Y':
    friut=random.choice(Friut_list)
    lives=5; temp=[];word=[]
    for i in fruit:
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
    print("The word was ",fruit.upper())
    choice=input("Play Again?(y/n) ").upper()
    
    
