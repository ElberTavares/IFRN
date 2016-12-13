import os
#opções para votos / seus valores = 0
php, js, py, vb = 0, 0, 0, 0

def vot():
    global php, js, py, vb
    print("\n[*] Sistema de votação [*]")
    print("\n1 - Python\n2 - PHP\n3 - JavaScript\n4 - Visual Basic")
    resp = int(input(">>> "))
    if resp > 4 or resp < 0:
        print("Número invalido.")
    elif resp == 1:
        py += 1
        print('\n[+] Você votou em Python [+]')
    elif resp == 2:
        php += 1
        print('\n[+] Você votou em PHP [+]')
    elif resp == 3:
        js += 1
        print('\n[+] Você votou em JavaScript [+]')
    else:
        vb += 1
        print('\n[+] Você votou em Visual Basic [+]')


for i in range(0, 10):
    vot()

os.system("cls")
#resultado final Linguagem + pontos
print("\nResultado:\nPHP: "+str(php) + "\nPython: "+str(py) + "\nJavaScript: "+str(js)+"\nvb: "+str(vb)) 
