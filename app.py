import streamlit as st
from etapa1 import EstoqueManager

st.set_page_config(page_title="Gestão de Estoque", layout="wide")

st.title("Sistema de Gerenciamento de Estoque")

estoque = st.session_state.get('estoque')
if not estoque:
    estoque = EstoqueManager()
    st.session_state['estoque'] = estoque

ABA_CADASTRO = "Cadastro de Produtos"
ABA_ESTOQUE = "Gestão de Estoque"
ABA_LISTA = "Lista de Produtos"

aba = st.sidebar.radio("Menu", [ABA_CADASTRO, ABA_ESTOQUE, ABA_LISTA])

if aba == ABA_CADASTRO:
    st.header("Cadastro de Produto")
    with st.form("form_cadastro"):
        codigo = st.text_input("Código do Produto")
        nome = st.text_input("Nome do Produto")
        categoria = st.text_input("Categoria")
        quantidade = st.number_input("Quantidade em Estoque", min_value=0, step=1)
        preco = st.number_input("Preço", min_value=0.0, step=0.01, format="%.2f")
        fornecedor = st.text_input("Fornecedor")
        descricao = st.text_area("Descrição", max_chars=200)
        submitted = st.form_submit_button("Cadastrar")
        if submitted:
            estoque.cadastrar_produto(codigo, nome, categoria, quantidade, preco, fornecedor, descricao)
            st.success(f"Produto '{nome}' cadastrado!")

elif aba == ABA_ESTOQUE:
    st.header("Gestão de Estoque")
    codigos = list(estoque.produtos.keys())
    if not codigos:
        st.info("Nenhum produto cadastrado.")
    else:
        codigo = st.selectbox("Selecione o produto", codigos)
        col1, col2, col3 = st.columns(3)
        with col1:
            qtd_add = st.number_input("Adicionar ao estoque", min_value=0, step=1, key="add")
            if st.button("Adicionar"):
                estoque.adicionar_ao_estoque(codigo, qtd_add)
                st.success("Quantidade adicionada!")
        with col2:
            qtd_rem = st.number_input("Remover do estoque", min_value=0, step=1, key="rem")
            if st.button("Remover"):
                estoque.remover_do_estoque(codigo, qtd_rem)
                st.success("Quantidade removida!")
        with col3:
            qtd_ajuste = st.number_input("Ajustar estoque manualmente", min_value=0, step=1, key="ajuste")
            if st.button("Ajustar"):
                if codigo in estoque.produtos:
                    estoque.produtos[codigo][2] = qtd_ajuste
                    st.success("Estoque ajustado!")

elif aba == ABA_LISTA:
    st.header("Lista de Produtos")
    if not estoque.produtos:
        st.info("Nenhum produto cadastrado.")
    else:
        min_estoque = st.number_input("Defina o nível mínimo para alerta de estoque baixo", min_value=0, value=5, step=1)
        data = []
        for codigo, info in estoque.produtos.items():
            alerta = info[2] <= min_estoque
            data.append({
                "Código": codigo,
                "Nome": info[0],
                "Categoria": info[1],
                "Quantidade": info[2],
                "Preço": f"R${info[3]:.2f}",
                "Fornecedor": info[4],
                "Descrição": info[5][:50] + ("..." if len(info[5]) > 50 else ""),
                "Alerta": "⚠️" if alerta else ""
            })
        st.dataframe(data, use_container_width=True)
        st.caption("Produtos com ⚠️ estão com estoque baixo.")
