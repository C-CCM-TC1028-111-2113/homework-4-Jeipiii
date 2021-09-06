
def main():
    #escribe tu código abajo de esta línea
    x = 0
    y = 1
    z = 0
    while True:
        l =int(input("Inserta un numero mayor a cero"))
        if l >= 0 :
        break
    print("0", end ="")
    for k in range (1, l):
        z = x+y
        print(f"{z}", end = "")
        x = y
        y = z
    print("")   
    pass

if __name__=='__main__':
    main()
