#TODO: Calcular o preço final do pedido (total dos hambúrgueres + total das bebidas).


#TODO: Calcular o troco do pedido, considerando o preço final e o valor pago pelo usuário.


#TODO: Imprimir a saída no formato especificado neste desafio.

hambúrguer = 10.50
hambúrguer_1 = 11.50

bebida = 2.50
bebida_2 = 3.50


print('''Bem Vindo
      Digite 1 para fazer um pedido
      Digite 2 para sair ''')

lang = input()
match lang:
    case "1":
         print('''Esse e nosso cardapio
               hambúrguer = 10.50
               hambúrguer_1 = 11.50

               bebida = 2.50
               bebida_2 = 3.50''')
         
         while True:
            resposta = input("Digite 'acabou' para encerrar o loop: ")
                
            if resposta.lower() == 'acabou':
                print("Loop encerrado.")
                break
            else:
                 print("Digite 'acabou' para encerrar o loop.")

         
    
       

            
          
            

        

    case "2":
            exit()
           

          

    case _:
        print("ERRO")