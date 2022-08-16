#Big - O  Notation. 
#Determinado para el calculo y complejidad algorítmica 


#Ley de la suma 

def f(n):
    for i in range(n):
        print(i)
    for i in range(n):
        print(i)

    # O(n) + O(n) = O (n + n) = O (2n) = O (n). (En Big O nos interesa solo el término mas grande sin
    # ningun tipo de coheficiente previo.)
         #CRECIMIENTO LINEAL: si N crece en 10. se tardará 10 veces mas tiempo.

def f(n):
    for i in range(n):
        print(i)
    
    for i in range(n*n):
        print(i)

    #O(n) + O(n*n) = O(n + n2) = O (n2)


#Ley de multiplicacion:
def f(n):
    for i in range(n):
        for j in range(n):
            print(i,j)
    
    #O(n) * O(n) = O ( n * n ) = O (n2) ////// Crecimiento Cuadratico ( loop adentro de otro)

# Recursividad Multiple
def fibonacci(n):
    if n == 0 or n==1:
        return 1
    return fibonacci(n-1) + fibonacci(n-2)

# 0 (2**n)  /// Crecimiento exponencial
