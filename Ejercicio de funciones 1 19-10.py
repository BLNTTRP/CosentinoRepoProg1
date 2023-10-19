# El siguiente programa debería imprimir el número 2 si se le ingresan como valores x=5,
# y=1 pero en su lugar imprime 5. ¿Qué hay que corregir?

# DEFINICIÓN DE FUNCIONES

def most(a,b):
    if(x>y):        # En vez de (x>y), (a>b)
        return x    # return a
    else:
        return y    # return b
    
def least(a,b):
    if(x<y):        # En vez de (x<y), (a<b)
        return x    # return a
    else:
        return y    # return b
    
# PROGRAMA PRINCIPAL

x = int(input('Un numero: '))
y = int(input('Otro numero: '))

print(most(x-3, least(x+2, y-5)))

# SOLUCIÓN: En ambas funciones (most y least) las variables que se pasan en el código principal
# (x e y) se declaran como 'a' y 'b' respectivamente, y las funciones devuelven 'x' o 'y', que son los valores
# que el usuario ingresó, sin modificar. Para solucionar el problema, hay que cambiar dentro del bloque
# de código de cada función, 'x' por 'a' e 'y' por 'b', y que retornen 'a' o 'b'.