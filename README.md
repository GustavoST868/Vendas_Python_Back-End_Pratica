# POO_Vendas
Estrutura para simular um ambiente de vendas de produtos com Orientação a  Objetos e modelagem de vendas.

**Descrição Geral:**

O código representa um sistema de interface gráfica em Tkinter, conectado a bancos de dados SQLite para gerenciar usuários, endereços e produtos. O sistema possui diversas interfaces, como registro de usuários, entrada de usuário, registro de endereço, registro de produtos e visualização de produtos.

**Classe `Address`:**

- **Método `__init__`:**
  - Inicializa a conexão com o banco de dados `addresses.db` e cria a tabela `addresses` se não existir.
  
- **Método `insert_address`:**
  - Insere um novo endereço no banco de dados.

- **Método `close_connection`:**
  - Fecha a conexão com o banco de dados.

**Classe `InterfaceProduct`:**

- **Método `on_image_click`:**
  - Exibe uma mensagem quando uma imagem é clicada.

- **Método `Window`:**
  - Define a interface gráfica para visualização de produtos.
  - Inclui botões para registrar um novo produto e voltar para a tela inicial.

**Classe `EnterInterface`:**

- **Método `Window`:**
  - Define a interface gráfica para a entrada de usuários.
  - Verifica se o usuário existe no banco de dados.

**Classe `GetAddress`:**

- **Método `Window`:**
  - Define a interface gráfica para obter informações de endereço.
  - Insere o endereço no banco de dados ao clicar no botão "Próximo".

**Classe `IntialInterface`:**

- **Método `Window`:**
  - Define a interface gráfica inicial com opções para entrar ou registrar um usuário.

**Classe `RegisterInterface`:**

- **Método `Window`:**
  - Define a interface gráfica para registrar usuários.

**Classe `InteraceRegisterProduct`:**

- **Método `Window`:**
  - Define a interface gráfica para registrar produtos.

**Classe `Product`:**

- **Método `__init__`:**
  - Inicializa a conexão com o banco de dados `products.db` e cria a tabela `products` se não existir.

- **Método `insert_product`:**
  - Insere um novo produto no banco de dados.

- **Método `get_all_products`:**
  - Retorna todos os produtos do banco de dados.

- **Método `check_product_exists`:**
  - Verifica se um produto existe no banco de dados.

**Classe `User`:**

- **Método `__init__`:**
  - Inicializa a conexão com o banco de dados `users.db` e cria a tabela `users` se não existir.

- **Método `insert_user`:**
  - Insere um novo usuário no banco de dados.

- **Método `user_exists`:**
  - Verifica se um usuário existe no banco de dados.

- **Método `close_connection`:**
  - Fecha a conexão com o banco de dados.
