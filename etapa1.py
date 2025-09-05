class EstoqueManager:
    def __init__(self):
        self.produtos = {}  # Dicionário: {codigo: [nome, categoria, quantidade, preco, fornecedor, descricao]}

    def adicionar_ao_estoque(self, codigo, quantidade):
        try:
            if codigo not in self.produtos:
                raise KeyError("Produto não cadastrado.")
            if quantidade < 0:
                raise ValueError("Quantidade não pode ser negativa.")
            self.produtos[codigo][2] += quantidade
        except (ValueError, KeyError) as e:
            print(f"Erro: {e}")
        else:
            print(f"Quantidade adicionada com sucesso. Novo estoque: {self.produtos[codigo][2]}")
        finally:
            print("Operação finalizada.")

    def remover_do_estoque(self, codigo, quantidade):
        try:
            if codigo not in self.produtos:
                raise KeyError("Produto não cadastrado.")
            if quantidade < 0:
                raise ValueError("Quantidade não pode ser negativa.")
            if self.produtos[codigo][2] < quantidade:
                raise ValueError("Estoque insuficiente.")
            self.produtos[codigo][2] -= quantidade
        except (ValueError, KeyError) as e:
            print(f"Erro: {e}")
        else:
            print(f"Quantidade removida com sucesso. Novo estoque: {self.produtos[codigo][2]}")
        finally:
            print("Operação finalizada.")

    def cadastrar_produto(self, codigo, nome, categoria, quantidade, preco, fornecedor, descricao):
        try:
            if codigo in self.produtos:
                raise ValueError("Produto já cadastrado.")
            if not nome.strip() or not categoria.strip():
                raise ValueError("Nome e categoria não podem ser vazios.")
            if quantidade < 0 or preco < 0:
                raise ValueError("Quantidade e preço não podem ser negativos.")
            if len(descricao) > 200:
                raise ValueError("Descrição não pode exceder 200 caracteres.")
            self.produtos[codigo] = [nome, categoria, quantidade, preco, fornecedor, descricao]
            print(f"Produto {nome} cadastrado com sucesso.")
        except ValueError as e:
            print(f"Erro: {e}")

    def listar_produtos(self):
        if not self.produtos:
            print("Nenhum produto cadastrado.")
            return
        print("\n=== Lista de Produtos ===")
        print("Código | Nome | Categoria | Quantidade | Preço | Fornecedor | Descrição")
        print("-" * 80)
        for codigo, info in self.produtos.items():
            descricao = info[5][:50] + "..." if len(info[5]) > 50 else info[5]
            print(f"{codigo} | {info[0]} | {info[1]} | {info[2]} | R${info[3]:.2f} | {info[4]} | {descricao}")

def obter_texto(mensagem, obrigatorio=True, max_len=None):
    while True:
        valor = input(mensagem).strip()
        if obrigatorio and not valor:
            print("Este campo não pode ser vazio.")
            continue
        if max_len and len(valor) > max_len:
            print(f"Entrada excede o limite de {max_len} caracteres.")
            continue
        return valor

def obter_numero(mensagem, tipo=float, minimo=None):
    while True:
        try:
            valor = tipo(input(mensagem))
            if minimo is not None and valor < minimo:
                print(f"Valor deve ser no mínimo {minimo}.")
                continue
            return valor
        except ValueError:
            print("Entrada inválida. Por favor, insira um número válido.")

def main():
    estoque = EstoqueManager()
    while True:
        print("\n=== Sistema de Gerenciamento de Estoque ===")
        print("1. Cadastrar produto")
        print("2. Adicionar ao estoque")
        print("3. Remover do estoque")
        print("4. Listar produtos")
        print("5. Sair")
        opcao = input("Escolha uma opção (1-5): ").strip()

        if opcao == "1":
            codigo = obter_texto("Digite o código do produto: ")
            nome = obter_texto("Digite o nome do produto: ")
            categoria = obter_texto("Digite a categoria do produto: ")
            quantidade = obter_numero("Digite a quantidade inicial: ", int, 0)
            preco = obter_numero("Digite o preço do produto: ", float, 0)
            fornecedor = obter_texto("Digite o nome do fornecedor: ", obrigatorio=False)
            descricao = obter_texto("Digite a descrição do produto (máx. 200 caracteres): ", obrigatorio=False, max_len=200)
            estoque.cadastrar_produto(codigo, nome, categoria, quantidade, preco, fornecedor, descricao)

        elif opcao == "2":
            codigo = obter_texto("Digite o código do produto: ")
            quantidade = obter_numero("Digite a quantidade a adicionar: ", int, 0)
            estoque.adicionar_ao_estoque(codigo, quantidade)

        elif opcao == "3":
            codigo = obter_texto("Digite o código do produto: ")
            quantidade = obter_numero("Digite a quantidade a remover: ", int, 0)
            estoque.remover_do_estoque(codigo, quantidade)

        elif opcao == "4":
            estoque.listar_produtos()

        elif opcao == "5":
            print("Saindo do sistema...")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()