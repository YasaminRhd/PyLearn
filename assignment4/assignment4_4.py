def howManyWords(string):
    splited_string = string.split(" ")
    print(len(splited_string))

string = input("enter a sentences to see how many words it has: ")
howManyWords(string)