#Vinicius Perrud
# Update notes:
# Now can travel and buy things
#and see how people see you
import random
c = ''
d = ''
v = ''
#chooseclass
def chooseclass ():
    global c
    c = input("'mage' or 'warrior'? ")
    global d
    global v
    if c == 'mage':
        d = 10
        v = 15
    elif c== 'warrior':
        d = 5
        v = 20
    else:
        print('Writte in lowercase equal on example pls')
        chooseclass()
#forwhostartnow
def cadastre():
    global name
    name = input("Name: ")
    global g
    g = 20
    print (g)
    chooseclass()
cadastre()
#declaring status
def status():
    global name
    global c
    global v
    global d
    global g
    print ("""{}, the great {}
    Has {} HP
    {} damage
    and {} soulscoins
    """.format(name,c,v,d,g))
    commands()
#declaring shop, bill gates is happy
def shop():
    global g
    global v
    global d
    print("You can exchange soulscoins in power and life here. ")
    print("What you want? life or power? (or exit)")
    cc = input("? ")
    if cc == "power":
        num1 = int(input("How many soulscoins you gonna give?"))
        if g > num1-1:
            g = g - num1
            d = d + num1
            print ('Done! ')
            shop()
        else:
            print("You dont have souls for that! ")
            shop()
    elif cc == 'life':
        num1 = int(input("How many soulscoins you gonna give?"))
        if g > num1-1:
            g = g - num1
            v = v + num1
            print ('Done! ')
            shop()
        else:
            print ('You dont have souls for that! ')
            shop()
    elif cc == 'exit':
        commands()
    else:
        print ("Write corecttly pleese")
        shop()
#declaring commands
def commands():
    cc = input("Choose the destination: shop, church, dungeons (Secret command: status and reboot) ")
    if cc == "shop":
        shop()
    elif cc == "SHOP":
        shop()
    elif cc == "Shop":
        shop()
    elif cc == "status":
        status()
    elif cc == "Status":
        status()
    elif cc == "STATUS":
        status()


commands()