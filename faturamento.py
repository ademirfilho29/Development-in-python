import json
if __name__ == "__main__":

    vetor = []

    menor_valor_do_faturamento = []

    maior_valor_do_faturamento = []

    valor_de_faturamento_maior_media_mensal = []

    def analisar_faturamento(dados):
          
          with open(dados, "r") as file:
            dados = json.load(file)

            faturamento = [item["valor"] for item in dados if "valor" in item]

            faturamento_valido = [valor for valor in faturamento if valor > 0]

            menor_faturamento = min(faturamento_valido)
            maior_faturamento = max(faturamento_valido)

            media_mensal = sum(faturamento_valido) / len(faturamento_valido)

            dias_acima_da_media =  sum(1 for valor in faturamento_valido if valor > media_mensal)

            return{
                "menor_faturamento": menor_faturamento,
                "maior_faturamento" : maior_faturamento,
                "dias_acima_da_media" : dias_acima_da_media

            }

            pass
          
    resultado = analisar_faturamento("dados.json")

    print("Menor faturamento:", resultado["menor_faturamento"])

    print("Maior faturamento:", resultado["maior_faturamento"])

    print("Dias acima da média:", resultado["dias_acima_da_media"])

    pass