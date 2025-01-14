 

if __name__ == "__main__":

    def fibonacci(n):

        #Sequencia começa no numero 0 
        sequencia_fib = [0, 1]

        #aqui fazemos um iteração sobre um range um seja sobre uma "distancia" onde esta o 2 para frente

        for i in range(2, n):

            #essa prox_valor vai receber a soma dos numeros anteriores de sequencia_fib

            prox_valor = sequencia_fib[-1] + sequencia_fib[-2]

            #essa função append, acresenta um novo valor a variavel
            
            sequencia_fib.append(prox_valor)

        return sequencia_fib
        
        pass

    print(fibonacci(20))
    pass