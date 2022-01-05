def show_menu():
    print('''
    1- Add new word
    2- English to persian translator
    3- Persian to english translator
    4- Save and exit
        ''')
 
def load():
    try:
        database = open('assignment7/translate.txt', 'r').read()
    except FileNotFoundError:
        print("File does not exist!")
    
    data = database.strip().split('\n')  
    for i in range(0, len(data), 2):
       dicKeys = {'english':data[i], 'persian':data[i+1]} 
       dictionary.append(dicKeys)
 
        
def addNewWord():
    english = input('enter your word in english: ')
    persian = input('enter meaning of the word: ')

    dickeys = {'english':english, 'persian':persian}
    dictionary.append(dickeys)


def englishToPersian():
    sentence = input('enter your text in english: ').strip().split('.')
    words = []
    for item in sentence:
        word = item.split()
        for i in word: 
            words.append(i)
          
    finalOutput = ''
    for word in words:
        item = search(word)
        if item:
            finalOutput += item['persian'] + ' '
        else:
            finalOutput +=  word + ' '            
    print(finalOutput)        
        

def persianToEnglish():
    sentence = input('enter your text in persian: ').strip().split('.')
    words = []
    for item in sentence:
        word = item.split()
        for i in word: 
            words.append(i)
          
    finalOutput = ''
    for word in words:
        item = search(word)
        if item:
            finalOutput += item['english'] + ' '
        else:
            finalOutput +=  word + ' '            
    print(finalOutput)      



def search(argument):
    for item in dictionary:
        if item['english'] == argument or item['persian'] == argument:
            return item
    return False    

def saveInFile():
    database = open('assignment7/translate.txt', 'w')
    for item in dictionary:
        database.write(item['english'] + '\n' + item['persian'] + '\n')

        
    
dictionary = []
load()
   
while True:
    show_menu()    
    choice = input('Please choose a number: ')
    match choice:
        case "1":
            addNewWord()
        case "2":
            englishToPersian()
        case "3":
            persianToEnglish()
        case "4":
            saveInFile()
            exit()
 
