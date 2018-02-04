c = ''
def chooseclass ():
    global c
    c = input("'mage' or 'warrior'?")
def cadastre():
    global name
    name = input("Name: ")
    chooseclass ()
cadastre()
