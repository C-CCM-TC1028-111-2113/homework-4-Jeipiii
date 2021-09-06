def main():
    #escribe tu código abajo de esta línea+
    count=0
    add=0
    n=1

    while True:
        n =float(input('Inserte un número (inserta uno negativo para acabar el programa):'))
   
        if n < 0:
            break

         add+=n
         count+=1

         if count == 0:
            print('No digitó ningun número')
    
         else:
            promedio= add/count

     print("El promedio es : ",promedio)


    pass
if __name__=='__main__':
    main()
