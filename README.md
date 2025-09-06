# Sistema Gerenciador de Loja de Varejo - FIAP

Este projeto foi desenvolvido durante as aulas de Python da FIAP e consiste em um sistema gerenciador de loja de varejo, com foco na gestão de estoque de produtos, utilizando o framework **Streamlit** para criação de interfaces web interativas.

## Funcionalidades

- Cadastro, edição e remoção de produtos
- Controle de estoque
- Visualização de relatórios simples

## Pré-requisitos

- Python 3.8 ou superior instalado

## Instalação

1. **Clone o repositório:**
  ```bash
  git clone https://github.com/seu-usuario/seu-repositorio.git
  cd seu-repositorio
  ```

2. **Crie um ambiente virtual (opcional, mas recomendado):**
  ```bash
  python -m venv venv
  ```
  ```bash
  source venv/bin/activate  # Linux/Mac
  ```
  Antes de ativar:
  ```bash
  venv\Scripts\activate     # Windows
  ```
  Use:
  ```bash
  Get-ExecutionPolicy
  ```
  Caso voce veja no seu Terminal:
  > Restricted
  
  Execute:
  ```bash
  Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned
  ```
  Isso permite que os scripts sejam executados localmente.
  
  Depois disso poderar executar o seginte codigo sem problema
  ```bash
  venv\Scripts\activate     # Windows
  ```

3. **Instale as dependências:**
  ```bash
  pip install -r requirements.txt
  ```
  > O arquivo `requirements.txt` deve conter pelo menos:
  > ```
  > streamlit
  > ```


## Como executar o sistema

1. Certifique-se de que as dependências estão instaladas (veja seção Instalação).
2. No terminal, dentro da pasta do projeto, execute:
  ```bash
  streamlit run app.py
  ```
3. O navegador abrirá automaticamente a interface do sistema.

---

### Integrantes

Adicione aqui o link do GitHub da equipe e os nomes/RMs de todos os integrantes.

## Dicas para quem nunca usou Streamlit

- O Streamlit transforma scripts Python em aplicações web de forma simples.
- Sempre que fizer alterações no código, salve o arquivo e a página será atualizada automaticamente.
- Para interromper a aplicação, pressione `Ctrl+C` no terminal.

## Referências

- [Documentação oficial do Streamlit](https://docs.streamlit.io/)
- [FIAP - Cursos de Python](https://www.fiap.com.br/)

---
Colabore com melhorias e sugestões!