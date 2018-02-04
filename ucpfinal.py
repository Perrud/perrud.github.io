# Vincius Perrud ;P
func = ('add,sub,mut,div,exp,root,"ave"(media),"per"(%)')
def op ():
    print (func)
    opp = input("Escolha a função desejada: ")
    if opp == "add":
        x = int(input('Num1'))
        y = int(input('Num2'))
        add(x,y)
    elif opp == 'sub':
        x = int(input('Num1'))
        y = int(input('Num2'))
        sub(x,y)
    elif opp == 'mut':
        x = int(input('Num1'))
        y = int(input('Num2'))
        mut(x,y)
    elif opp == 'div':
        x = int(input('Num1'))
        y = int(input('Num2'))
        div(x,y)
    elif opp == 'exp':
        x = int(input('Num1'))
        y = int(input('Num2'))
        exp(x,y)
    elif opp == 'root':
        x = int(input('Num1'))
        y = int(input('Num2'))
        root(x,y)
    elif opp == 'ave':
        ave ()
    elif opp == 'per':
        per()
    else:
        print("""
        
        Digite corretamente
        
        """)
        op()

def add(x,y):
    r = x + y
    print ('{} + {} = {} '.format(x,y,r))
    op()
def sub(x,y):
    r = x - y
    print ('{} - {} = {} '.format(x,y,r))
    op()
def mut(x,y):
    r = x * y
    print('{} x {} = {}'.format(x,y,r))
    op()
def div(x,y):
    r = x / y
    print('{} / {} = {}'.format(x,y,r))
    op()
def exp(x,y):
    r = x**y
    print('{}^{} = {}'.format(x,y,r))
    op()
def root(x,y):
    r = x**(1/y)
    print('{}√{} = {}'.format(x,y,r))
    op()
def per():
    opp = input('Calcular desconto/aumento (pc) ou calcular a porcentagem por conta propia(i): ')
    if opp == 'pc':
        ppo = input('Desconto (dis) ou aumento (inc) ?: ')
        if ppo == 'dis':
            on = float(input('Qual o numero original?: '))
            disc = float(input('Qual o valor do desconto? ("digite apenas o valor ex: 15): '))
            dis = disc / 100
            r = on - (on * dis)
            print('{}$ valor original, que com de {}% de desconto vai para {}$'.format(on,disc,r))
        elif ppo == 'inc':
            on = float(input('Qual o numero original?: '))
            disc = float(input('Qual o valor do aumento? ("digite apenas o valor ex: 15): '))
            dis = disc / 100
            r = on + (on * dis)
            print('{}$ valor original, que com de {}% de aumento vai para {}$'.format(on,disc,r))
        else:
            print("""

                    Digite corretamente

                    """)
            per()
    elif opp == 'i':
        x = float(input('Qual o numero original: '))
        y = float(input('Porcentagem, SO NUMEROS (ex:15, 120) : '))
        r = x * (y/100)
        print('Numero original: {} \n Porcentagem: {}% \n Total: {} '.format(x,y,r))
        op()
    else:
        print("""

                Digite corretamente

                """)
        op()
exd = 0
def EXD (x):
    global exd
    exd = exd + x

def ave():
    q = input('Coloca os numeros que serao usados para tirar a media entre espacos (ex: 0 1.2 -15)')
    n = q.split(' ')
    n = [int(i) for i in n]
    print(n)
    qq = len(n)
    for w in range(0,qq):
        EXD (n[w])
    global exd
    exd = (exd / qq)
    print(exd)
    op()
op()