from datetime import date

def gerar_contrato(nome_contratante, nome_contratado, servico, valor):
    with open("contrato_modelo.txt", "r", encoding="utf-8") as modelo:
        texto = modelo.read()
        contrato = texto.format(
            nome_contratante=nome_contratante,
            nome_contratado=nome_contratado,
            servico=servico,
            valor=valor,
            data=date.today().strftime("%d/%m/%Y")
        )
    with open("contrato_gerado.txt", "w", encoding="utf-8") as arquivo:
        arquivo.write(contrato)
    print("Contrato gerado com sucesso!")

# Exemplo de uso
gerar_contrato("João Silva", "Genailma Oliveira", "Consultoria Jurídica", "500")
