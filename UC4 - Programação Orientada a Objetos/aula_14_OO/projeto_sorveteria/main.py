from services.sorveteria import Sorveteria
import os
from datetime import datetime

if __name__ == "__main__":
    total_geral=0
    quantidade_geral=0
    historico_compras=[]
    contador_clientes=0

    # Criar a pasta onde as notas fiscais serão salvas, se não existir
    pasta_notas="Notas_fiscais"
    os.makedirs(pasta_notas, exist_ok=True)

    while True:
        contador_clientes+=1
        sorveteria= Sorveteria()
        # Inicia a etapa de compras
        sorveteria.iniciar_compras()
        # Processa pagamento
        pagamento= sorveteria.processar_pagamento()
        # Finaliza a compra mostrando a mensagem de agradecimento
        sorveteria.finalizar_compra()
        # Obtém os totais da compra do cliente atual
        total_compra= pagamento.total
        quantidade_compra= sorveteria.calcular_quantidade_total()
        # Atualiza os acumulados gerais do dia
        total_geral+=total_compra
        quantidade_geral+=quantidade_compra

        # Criar o nome do arquivo
        data_hora= datetime.now().strftime("%Y%m%d_%H%M%S")
        nome_arquivo= os.path.join(
            pasta_notas,
            f"nota_cliente_{contador_clientes}_{data_hora}.txt"
        )
        # Abrir o arquivo da nota fiscal em modo de escrita
        with open(nome_arquivo,"w",encoding="utf-8") as nota:
            # cabeçalho da nota
            nota.write("== Nota Fiscal ==")
            # Lista de todos os pedidos do cliente
            for pedido in sorveteria.pedidos:
                nota.write(
                    f"{pedido.quantidade}x {pedido.picole.nome} - "
                    f"R$ {pedido.calcular_subtotal():.2f}\n"
                )
                nota.write("===========================================\n")
                nota.write(f"Total R$ {total_compra}")
                nota.write("===========================================\n")

            print(f"Nota fiscal salva em: {nome_arquivo}")

            # Adicionar os dados da compra ao hstórico de todas as vendas
            historico_compras.append({
                "Cliente": contador_clientes,
                "Quantidade": quantidade_compra,
                "Total": total_compra
            })
            # Perguntar ao usuario se deseja atender outro cliente
            nova= input("Deseja atender um novo cliente (S/N): ").lower()
            
            # Caso o ususario não queira atender mais clientes
            if nova != "s":
                print("--- Relatório Final ---")
                print(f"Quantidade total de picolés vendidos: {quantidade_geral}")
                print(f"Valor total vendido: {total_geral:.2f}")
                print("\n","-"*30,"\n")

                # Ger um nome unico para o arquivo de historico de vendas
                nome_historico=f"Historico vendas_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
                with open(nome_historico, "w", encoding="utf-8") as hist:
                    hist.write("--- Histórico de Vendas ---")
                    # Escreve cada compra feita no dia
                    for compra in historico_compras:
                        hist.write(
                            f"Cliente {compra['Cliente']}: "
                            f"{compra['Quantidade']} picolés - "
                            f"R$ {compra['Total']:.2f}\n"
                        )
                    hist.write("-"*30)

                    hist.write(f"Total geral de picolés vendidos: {quantidade_geral}")
                    hist.write(f"Valor total vendido R$ {total_geral:.2f}")

                print(f"Histórico de vendas salvo em: {nome_historico}")
                break