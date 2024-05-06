"""

Napisz program generujący ciąg n początkowych liczb Fibonacciego..

"""

def fibonacci( n ):

    if n == 0:
        # print("Wynki: 0")    
        return 0
    
    if n == 1:
        # print("Wynki: 1")    
        return 1
    
    if n > 1:
        return fibonacci( n - 1 ) + fibonacci ( n - 2 )

if __name__ == "__main__":
    
    for n in range(0, 30):
        print(fibonacci(n))