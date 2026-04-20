import requests

def buscar_taxas():
        # Fazemos a requisição dentro da função para garantir que os dados em estejam em tempo real
        link = "https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,GBP-BRL"
        requisicao = requests.get(link)
        
        # Verificamos se o site respondeu (Status 200 é OK)
        if requisicao.status_code == 200:
            dados = requisicao.json()
            
            # Extraímos os valores convertendo para float
            dolar = float(dados['USDBRL']['bid'])
            euro = float(dados['EURBRL']['bid'])
            libra = float(dados['GBPBRL']['bid'])
            
            return dolar, euro, libra
        else:
            raise Exception("Site da API fora do ar")

def main():
    taxa_dolar, taxa_euro, taxa_libra = buscar_taxas()

    while True:
        # Caso a pessoa não digite um número
        try: 
            menu = int(input("""
                            
            Para qual moeda você quer fazer a conversão?

            [1] Dólar Americano
            [2] Euro
            [3] Libra (Inglaterra)
            [0] Sair                                 

            => """))
        
        except ValueError:
            print("Você não digitou um número.")
            continue   
        
        # Para encerrar o código
        if menu == 0:
            print("Encerrando...")
            break
        
        # Caso a pessoa digite um número que não está no comando
        if menu not in [1, 2, 3]:
            print("Comando não reconhecido.")
            continue

        # Quantia em real
        try:
            real = float(input("Digite a quantia em R$ ")) 
        except ValueError:
           print("Você não digitou um número.")
           continue
           
        if menu == 1:
            conversao = real / taxa_dolar
            # .2f serve para mostrar apenas duas casas decimais
            print(f"R${real:.2f} valem US${conversao:.2f} (Cotação: {taxa_dolar})")

        elif menu == 2:
            conversao = real / taxa_euro
            # .2f serve para mostrar apenas duas casas decimais
            print(f"R${real:.2f} valem €{conversao:.2f} (Cotação: {taxa_euro})")

        elif menu == 3:
            conversao = real / taxa_libra
            # .2f serve para mostrar apenas duas casas decimais
            print(f"R${real:.2f} valem £{conversao:.2f} (Cotação: {taxa_libra})")
                 
main()
