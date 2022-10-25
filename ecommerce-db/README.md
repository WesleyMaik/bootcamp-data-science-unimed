## Modelagem de dados para Ecommerce 
### Desafio da Digital Innovation One Inc.
---
### Objetivo
Criar um esquema conceitual para uma loja virtual.

### Narrativa
- Sistema de venda de produtos por uma loja virtual.
- O sistema deve contar com usuários, produtos, fornecedores, vendedores, estoques, pedidos, pagamento e entrega.
- O usuário deve ter suas informações pessoais, endereço e CPF ou CNPJ.
- O produto deve conter seu nome, categoria, preço e estoque.
- Fornecedores e vendedores devem ter CNPJ e Razão Social.
- O Estoque deve ter local.
- Os pedidos devem ter endereço, descrição, se foram cancelados ou não, produtos, pagamento e entrega.
- No pagamentos consta o valor total do pedido, desconto e se há Cartão de Crédito, Boleto ou Pix.
- O Cartão de Crédito deve ter o número do cartão, o nome do portador do cartão, validade e token.
- O Boleto deve ter o código de registro e token.
- O Pix deve ter a chave pix e o token.
- A entrega deve ter data de entrega, código de rastreio, endereço de entrega, status, data do pedido, e valor do frete.


### Relacionamentos
- Um Usuário pode ter N Pedidos.
- Um Pedido pode ter N Produtos, uma forma de pagamento e uma opção de delivery.
- Um Produto pode ter uma Categoria, quantidade em Estoque, N Fornecedores e N Vendedores.
- Um Fornecedor pode fornecer N Produtos.
- Um Vendedor pode vender N Produtos com quantidade.
- O Pagamento pode ter um Cartão de Crédito, Boleto e/ou Pix.
---
## Modelo:
![DB Model](ecommercedb-model.png)