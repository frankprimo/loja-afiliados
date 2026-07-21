import csv


entrada = "shopee.csv"
saida = "shopee_corrigido.csv"


with open(entrada, "r", encoding="latin1") as origem:
    linhas = origem.readlines()


with open(saida, "w", encoding="latin1", newline="") as destino:

    escritor = csv.writer(destino)

    buffer = ""

    for linha in linhas:

        if linha.startswith("http"):

            if buffer:
                escritor.writerow([buffer])

            buffer = linha.strip()

        else:
            buffer += " " + linha.strip()


    if buffer:
        escritor.writerow([buffer])


print("CSV corrigido criado:", saida)