'''
n = int(input('Digite n :'))
primo = 0
for c in range (1,n+1):
    if n%c==0:
        primo+=1            
    print(primo)
if primo==2:
    print('Primo')
else :
    print('nao primo')
    '''

n = int(input('quantidade primos :'))
cont = 0
c = 2
while cont < n:
    primo = 0
    for co in range (1,c+1):
        if c%co==0:
            primo+=1       
    if primo==2:
        print(c)
        cont+=1
    c+=1
    
        
    
    

    
