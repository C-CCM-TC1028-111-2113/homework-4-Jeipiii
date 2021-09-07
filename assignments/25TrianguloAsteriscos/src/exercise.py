
def main():
    #Escribe tu código debajo de esta línea
   altura = int(input("Ingresa la altura para el triangulo"))
    def triangulo_asterisco(altura):
        line = str("")
        for j in range(0, altura-1):
            line = str("*" + line)
            print(line)
   triangulo_asterisco(altura)
    
    pass


if __name__=='__main__':
    main()
