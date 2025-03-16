from adapter import CarregadorProdutosArquivo, CLIInterfaceUsuario

def main():
    # Configurar sistema através de portas
    carregador = CarregadorProdutosArquivo()
    catalogo = carregador.carregar_produtos()
    interface = CLIInterfaceUsuario(catalogo)
    
    # Loop principal
    while True:
        print("\n=== Supermercado Hexagonal ===")
        print("1 - Nova Venda")
        print("2 - Sair")
        
        opcao = input("Opção: ")
        
        if opcao == "1":
            interface.iniciar_venda()
            while True:
                print("\n1 - Adicionar Item")
                print("2 - Finalizar Venda")
                sub_opcao = input("Opção: ")
                
                if sub_opcao == "1":
                    try:
                        codigo = int(input("Código do produto: "))
                        quantidade = int(input("Quantidade: "))
                        interface.adicionar_item(codigo, quantidade)
                    except ValueError:
                        print("Entrada inválida!")
                elif sub_opcao == "2":
                    try:
                        valor = float(input("Valor recebido: R$"))
                        interface.finalizar_venda(valor)
                        break
                    except ValueError:
                        print("Valor inválido!")
                else:
                    print("Opção inválida!")
        elif opcao == "2":
            print("Saindo do sistema...")
            break
        else:
            print("Opção inválida!")

if __name__ == "__main__":
    main()