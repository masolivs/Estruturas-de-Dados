testes= int(input())
n= 0
while testes>n:
    a= 0
    planoestudo={}
    estudo= input()
    for i in estudo:
            if i in planoestudo:
                planoestudo[i]+=1
            else:
                planoestudo[i]=1
    morri= False
    while a<3:
        string= input()
        for i in string:
            if i in planoestudo:
                planoestudo[i]-=1
            else:
                morri= True

      
        a+=1
    
    n+=1
    ralar=''
    ralart= False
    for i in planoestudo:
        if planoestudo[i]>0:
            ralar+= i
            ralart= True
        if planoestudo[i]<0:
            morri= True
    ralara= sorted(ralar)
    ralar= ''.join(ralara)
    if morri:
        print('You died!')
    if not morri and ralar:
        print(f'Bora ralar: {ralar}')
    if not morri and not ralar:
        print("It's in the box!")