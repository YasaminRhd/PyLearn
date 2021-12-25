from pyfiglet import Figlet 
import qrcode

def show_list():
    for i in range(len(products)):
        print(products[i])
        
def show_menu():
    print('1- Add Product')
    print('2- Edit Product')
    print('3- Delete Product')
    print('4- Search')
    print('5- Show list')
    print('6- Buy')
    print('7- make QrCode')
    print('8- Exit')
    
def load():
    myfile = open('assignment6/database.txt' , 'r')
    data = myfile.read()
    product_list = data.strip().split('\n')
    
    for i in range(len(product_list)):
        product_info = product_list[i].split(",")
        mydict = {}
        mydict['id']  = int(product_info[0])
        mydict['name']  = product_info[1]
        mydict['price']  = int(product_info[2])
        mydict['count']  = int(product_info[3])
        products.append(mydict)
        
def add_product():
    with open('assignment6/database.txt', "a") as addToFile:
        addToFile.write( '\n' )
        addToFile.write(input("add id of the new product: "))
        addToFile.write( ',' )        
        addToFile.write(input("add name of the new product: "))
        addToFile.write( ',' )        
        addToFile.write(input("add price of the new product: "))
        addToFile.write( ',' )        
        addToFile.write(input("add count of the new product: "))
    load()
        
        
def edit():
    
    index = search()    

    if index:
        file = open("assignment6/database.txt", "r")
        list_of_lines = file.readlines()
        list_of_lines[index] = input("enter id , name , price , number of product: ") + '\n'
        list_of_lines[index] = list_of_lines[index].replace(" ", ",")
        a_file = open("assignment6/database.txt", "w")
        a_file.writelines(list_of_lines)
        a_file.close()
    else:
        print('item not found!')
         
def delete():
    
    index = search()
        
    if index:
        file = open("assignment6/database.txt", "r")
        list_of_lines = file.readlines()
        del list_of_lines[index]
        a_file = open("assignment6/database.txt", "w")
        a_file.writelines(list_of_lines)
        a_file.close()
    else:
        print('item not found!')
    

def search():
    name = input('enter the name of the product: ')
    #  you can use Python’s enumerate() to get a counter and the value from the iterable at the same time!
    for index, item in enumerate(products): 
        if item['name'] == name:
            print(item)
            return index
    print("item not found!")
    return False 

def make_qrcode():
    id = int(input('enter id of the product: '))
    for item in products: 
        if item['id'] == id:
            img = qrcode.make(item)
            img.save('assignment6/product.png')

def buy():
    string = ''
    total = 0
    flag = False
    while True:
        id = int(input('enter id of the product: '))
        for index, item in enumerate(products): 
            if item['id'] == id:
                flag = True
                number = int(input('how many item do you want?'))
                if number > item['count'] :
                    print('insufficient inventory!')
                if number <= item['count'] :
                    string += f"{number} of { item['name'] }  * { item['price'] } = { number * item['price']} \n "
                    item['count'] -= number
                    # edit the number of product 
                    file = open("assignment6/database.txt", "r")
                    list_of_lines = file.readlines()
                    list_of_lines[index] = list_of_lines[index].split(',')
                    list_of_lines[index][3] = item['count']
                    list_of_lines[index] = str(list_of_lines[index][0] +','+ list_of_lines[index][1] +','+ list_of_lines[index][2] +','+ str(list_of_lines[index][3])) + '\n'
                    a_file = open("assignment6/database.txt", "w")
                    a_file.writelines(list_of_lines)
                    a_file.close()
                    total +=  number * item['price']
                print(string)
                break 
                             
        if not flag:
            print("item not found!")
        if input("do you want to continue? ") == 'no':
            break         
    print("total price: ", total)
    
products = []
load()
f = Figlet(font="standard")
print(f.renderText("Yasamin Store"))



while True:
    show_menu()
    choice = input('Please choose a number: ')
    match choice:
        case "1":
            add_product()
        case "2":
            edit()
        case "3":
            delete()
        case "4":
            search()
        case "5":
            show_list()
        case "6":
            buy()
        case "7":
            make_qrcode()
        case "8":
            exit()