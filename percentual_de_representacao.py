if __name__ == "__main__":

    sp = "7.836,43"
    rj = "36.678,66"
    mg = "29.229,88"
    es = "27.165,48"
    outros = "19.849,53"

    def converter_para_float(valor_str):

        return float(valor_str.replace(".", "").replace(",", "."))

        pass
    sp = converter_para_float(sp)
    rj = converter_para_float(rj)
    mg = converter_para_float(mg)
    es = converter_para_float(es)
    outros = converter_para_float(outros)

    soma_total  = sp + rj + mg + es + outros

    print(f"Essa foi a soma total: {soma_total}")

    percentual_sp = (sp / soma_total) * 100
    percentual_rj = (rj / soma_total) * 100
    percentual_mg = (mg /soma_total) * 100
    percentual_es = (es / soma_total) *100
    percentual_outros = (outros / soma_total) *100

    print(f"Percentual de SP: {percentual_sp: .2f}%")
    print(f"Percentual de RJ: {percentual_rj: .2f}%")
    print(f"Percentual de MG: {percentual_mg: .2f}%")
    print(f"Percentual de ES: {percentual_es: .2f}%")
    print(f"Percentual de OUTROS: {percentual_outros: .2f}%")
    
    pass
