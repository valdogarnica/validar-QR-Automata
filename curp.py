import random
import string

def automata(cadena):
    estado = 'q1'
    i = 0
    while i < len(cadena):
        char = cadena[i]
        
        if estado == 'q1':
            if char in 'ABCDEFGHIJKLMNÑOPKRSTUVWXYZ':
                estado = 'q2'
                print("el estado es ", estado)
            else:
                return False
        elif estado == 'q2':
            if char in 'ABCDEFGHIJKLMNÑOPKRSTUVWXYZ':
                estado = 'q3'
                print("el estado es ", estado)
            else:
                return False
        elif estado == 'q3':
            if char in 'ABCDEFGHIJKLMNÑOPKRSTUVWXYZ':
                estado = 'q4'
                print("el estado es ", estado)
            #elif char == '0': #oreja que elimine xd
                #estado = 'q2'
            else:
                return False
        elif estado == 'q4':
            if char in 'ABCDEFGHIJKLMNÑOPKRSTUVWXYZ':
                estado = 'q5'
                print("el estado es ", estado)
            else:
                return False
        elif estado == 'q5':
            if char in '0123456789':
                estado = 'q6'
            else:
                return False
        elif estado == 'q6':
            if char in '0123456789':
                estado = 'q7'
            else:
                return False
        elif estado == 'q7':
            if char in '0123456789':
                estado = 'q8'
            else:
                return False
        elif estado == 'q8':
            if char in '0123456789':
                estado = 'q9'
            else:
                return False
        elif estado == 'q9':
            if char in '0123456789':
                estado = 'q10'
            else:
                return False
        elif estado == 'q10':
            if char in '0123456789':
                estado = 'q11'
            else:
                return False
        elif estado == 'q11':
            if char in 'ABCDEFGHIJKLMNÑOPKRSTUVWXYZ':
                estado = 'q12'
            else:
                return False
            #############################################################################################
        elif estado == 'q12':
            if char in 'ABCDEFGHIJKLMNÑOPKRSTUVWXYZ':
                estado = 'q13'
            else:
                return False
            
        elif estado == 'q13':
            if char in 'ABCDEFGHIJKLMNÑOPKRSTUVWXYZ':
                estado = 'q14'
            else:
                return False
            
        elif estado == 'q14':
            if char in 'ABCDEFGHIJKLMNÑOPKRSTUVWXYZ':
                estado = 'q15'
            else:
                return False
        
        elif estado == 'q15':
            if char in 'ABCDEFGHIJKLMNÑOPKRSTUVWXYZ':
                estado = 'q16'
            else:
                return False
        elif estado == 'q16':
            if char in 'ABCDEFGHIJKLMNÑOPKRSTUVWXYZ':
                estado = 'q17'
            else:
                return False
            
        elif estado == 'q17':
            if char in 'ABCDEFGHIJKLMNÑOPKRSTUVWXYZ':
                estado = 'q18'
            else:
                return False
            
        elif estado == 'q18':
            if char in '0123456789':
                estado = 'q19'
            else:
                return False
        i += 1
    
    
    return estado in {'q19'}


     


'''
def curpRandom():
    # Generar tres letras mayúsculas
    part1 = ''.join(random.choices(string.ascii_uppercase, k=4))
    year = ''.join(random.choices(string.digits, k=2))
    month = ''.join(random.choices([f'{i:02}' for i in range(1, 13)]))
    # Generar dos dígitos para el día (01 a 31)
    day = ''.join(random.choices([f'{i:02}' for i in range(1, 32)]))
    # Generar dos letras mayúsculas
    part3 = ''.join(random.choices(string.ascii_uppercase, k=7))
    # Generar un dígito
    digit = ''.join(random.choices(string.digits, k=1))
    print(digit)

    c = part1 +  year + month + day + part3 + digit
    
    return c


curp = curpRandom()

#curp = 'GAGV030214HMCRRLA2'
print(f"La cadena '{curp}' es {'válida' if automata(curp) else 'inválida'}")
'''