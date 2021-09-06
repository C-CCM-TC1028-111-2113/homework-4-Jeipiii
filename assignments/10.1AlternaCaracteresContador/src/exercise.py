def main():
    #escribe tu código abajo de esta línea
    l=int(input("Pon la cantidad de numeros a repetir"))
    for k in range(l):
        if k%2 == 0:
            print('#')

        else:
            print('%')
    pass

if __name__=='__main__':   
    main()
