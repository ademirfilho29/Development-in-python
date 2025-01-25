 

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

    def pertenci_fibo(numero):

        sequencia_fib = [0, 1]

        while sequencia_fib[-1] < numero:

            prox_valor = sequencia_fib[-1] + sequencia_fib[-2]
            sequencia_fib.append(prox_valor )
            
        #VERIFICA SE O NUMERO SECOLHIDO PERTENCE OU NÃO A SEQUENCIA FIBONACCI

        if numero in sequencia_fib:
            return f"O número {numero} pertence à sequência de Fibonacci."
        
        else:
            return f"O número {numero} não pertence à sequência de Fibonacci."
            pass
    pass

    print(fibonacci(20))

    numero_para_verificar = int(input("Digite um número que você gostaria de testar: "))
    print(pertenci_fibo(numero_para_verificar))

    pass