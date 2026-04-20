# Conversor de Moedas
Este projeto é um conversor de moedas interativo desenvolvido em Python. Ele se conecta a uma API financeira para buscar as cotações mais recentes do Dólar, Euro e Libra, permitindo conversões precisas a partir do Real (BRL).

## Como funciona?
O programa é dividido em duas partes principais:

- buscar_taxas(): Uma função que utiliza a biblioteca requests para acessar a AwesomeAPI, capturar os dados em formato JSON e retornar as cotações atuais.
- main(): O loop principal que gerencia o menu, valida as entradas do usuário usando try/except e exibe o resultado formatado.

## Tecnologias e Conceitos Utilizados
- **Python 3**
- **Biblioteca requests:** Para comunicação via HTTP com a API.
- **API:** AwesomeAPI
- **Tratamento de Erros (try/except):** Utilizado para evitar que o programa feche caso o usuário digite letras ou caracteres inválidos. 
- **Estruturas de Controle:** Uso de while True, if/elif/else, break e continue para um menu fluido.

## Pré-requisitos
- Para rodar este script, você precisa instalar a biblioteca 'request'.
 
## Como usar
1. Execute o arquivo .py.
2. O programa buscará automaticamente as taxas de câmbio na internet. 
3. Escolha a moeda de destino (1, 2 ou 3). 
4. Digite o valor que você possui em Reais (R$). 
5. O programa exibirá o valor convertido e a cotação utilizada no momento. 
6. Para sair, digite 0.
