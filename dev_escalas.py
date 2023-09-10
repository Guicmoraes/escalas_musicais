def menu():
    print("MODOS:\n[1]-Escala maior\n[2]-Escala menor\n[3]-Dório\n[4]-Frígio\n[5]-Lídio\n[6]-Mixolídio\n[7]-Lócrio\n[8]-Encerrar programa")
notas=['C','C#','D','D#','E','F','F#','G','G#','A','A#','B']*2
campo_harmonico=[]
def escalamaior():
    i=0
    while i<len(notas):
        if notas[i]==nota_digitada:
            i+=2
            campo_harmonico.append(notas[i])
            i+=2
            campo_harmonico.append(notas[i])
            i+=1
            campo_harmonico.append(notas[i])
            i+=2
            campo_harmonico.append(notas[i])
            i+=2
            campo_harmonico.append(notas[i])
            i+=2
            campo_harmonico.append(notas[i])
            break
        else:
            i+=1
    print('Campo Harmônico: ',campo_harmonico)
def escalamenor():
    i=0
    while i<len(notas):
        if notas[i]==nota_digitada:
            i+=2
            campo_harmonico.append(notas[i])
            i+=1
            campo_harmonico.append(notas[i])
            i+=2
            campo_harmonico.append(notas[i])
            i+=2
            campo_harmonico.append(notas[i])
            i+=1
            campo_harmonico.append(notas[i])
            i+=2
            campo_harmonico.append(notas[i])
            break
        else:
            i+=1
    print('Campo Harmônico: ',campo_harmonico)
def dório():
    i=0
    while i<len(notas):
        if notas[i]==nota_digitada:
            i+=2
            campo_harmonico.append(notas[i])
            i+=1
            campo_harmonico.append(notas[i])
            i+=2
            campo_harmonico.append(notas[i])
            i+=2
            campo_harmonico.append(notas[i])
            i+=2
            campo_harmonico.append(notas[i])
            i+=1
            campo_harmonico.append(notas[i])
            break
        else:
            i+=1
    print('Campo Harmônico: ',campo_harmonico)
def frígio():
    i=0
    while i<len(notas):
        if notas[i]==nota_digitada:
            i+=2
            campo_harmonico.append(notas[i])
            i+=2
            campo_harmonico.append(notas[i])
            i+=1
            campo_harmonico.append(notas[i])
            i+=2
            campo_harmonico.append(notas[i])
            i+=2
            campo_harmonico.append(notas[i])
            i+=2
            campo_harmonico.append(notas[i])
            break
        else:
            i+=1
    print('Campo Harmônico: ',campo_harmonico)
def lídio():
    i=0
    while i<len(notas):
        if notas[i]==nota_digitada:
            i+=2
            campo_harmonico.append(notas[i])
            i+=2
            campo_harmonico.append(notas[i])
            i+=2
            campo_harmonico.append(notas[i])
            i+=1
            campo_harmonico.append(notas[i])
            i+=2
            campo_harmonico.append(notas[i])
            i+=2
            campo_harmonico.append(notas[i])
            break
        else:
            i+=1
    print('Campo Harmônico: ',campo_harmonico)
def mixolídio():
    i=0
    while i<len(notas):
        if notas[i]==nota_digitada:
            i+=2
            campo_harmonico.append(notas[i])
            i+=2
            campo_harmonico.append(notas[i])
            i+=1
            campo_harmonico.append(notas[i])
            i+=2
            campo_harmonico.append(notas[i])
            i+=2
            campo_harmonico.append(notas[i])
            i+=1
            campo_harmonico.append(notas[i])
            break
        else:
            i+=1
    print('Campo Harmônico: ',campo_harmonico)
def lócrio():
    i=0
    while i<len(notas):
        if notas[i]==nota_digitada:
            i+=1
            campo_harmonico.append(notas[i])
            i+=2
            campo_harmonico.append(notas[i])
            i+=2
            campo_harmonico.append(notas[i])
            i+=1
            campo_harmonico.append(notas[i])
            i+=2
            campo_harmonico.append(notas[i])
            i+=2
            campo_harmonico.append(notas[i])
            break
        else:
            i+=1
    print('Campo Harmônico: ',campo_harmonico)
count=0
while count==0:
    nota_digitada=input('informe a nota base de sua música: ')
    if nota_digitada in notas:
        count+=1
    else:
        count==0
menu()
escala=int(input('informe a escala desejada: '))
while escala!=8:
    if escala==1:
        escalamaior()
        
    elif escala==2:
        escalamenor()
        
    elif escala==3:
        dório()
        
    elif escala==4:
        frígio()
        
    elif escala==5:
        lídio()
        
    elif escala==6:
        mixolídio()
       
    elif escala==7:
        lócrio()
        
    else:
        print('opção inválida')
    campo_harmonico.clear()
    escala=int(input('informe a escala desejada: '))
else:
    print('[programa encerrado]')