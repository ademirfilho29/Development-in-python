if __name__ == "__main__":

    def inverter_string (texto):

        #VAI RECEBER A STRING INVERTIDA

        texto_invertido = ""

        #ITERA SOBRE UM "DISTANCIA" QUE TEM TAMANHO DO TEXTO E FAZ UM LOOP QUE COMEÇA NO ULTIMO INDICE
        
        for i in range(len(texto) -1, -1, -1):

            texto_invertido += texto[i]

            pass

        return texto_invertido
    
    entrada = input("Digite um texto para ser invertido: ")

    resultado = inverter_string(entrada)

    print(f"A string invertida ficou assim: {resultado}")

    pass
    

        
