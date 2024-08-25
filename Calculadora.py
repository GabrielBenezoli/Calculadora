# Questionamento para o usuário escolher o valor inicial "a" que será utilizado na questão.
a = float(input('Digite o valor do primeiro produto da questão:'))

# Def para repetição, caso o usuário escolha uma opção inadequada.
def again():
 
 # Questionamento para o usuário escolher a operação que será utilizada.
 equacao = int(input('Escolha a operação que deseja realizar:'
               '\n 1 - SOMA'
               '\n 2 - SUBTRAÇÃO'
               '\n 3 - DIVISÃO'
               '\n 4 - MULTIPLICAÇÃO'
               '\n 5 - RAIZ.'
               '\n 6 - POTENCIAÇÃO.'))
 
 # Variável If para caso a resposta da questão anterior estiver fora do padrão pedido (1 até 6), caso a resposta for menor ou maior que esse pedido, estará incorreta e permanecera dentro desse looping até a resposta ser uma das alternativas pedidas anteriormente.
 if equacao < 1 or equacao > 6:
    print('Opção invalida, tente novamente')

    # Função "again" para repetir a questão caso a variável If acima for verdadeira.
    again()

 # Variável if para dar continuidade para as seguintes respostas: (1,2,3,4,6), pois se a escolha da operação for a "5" não irá necessitar de um novo produto na questão.
 if equacao != 5:
  
  # Questionamento para o usuário escolher o valor do segundo produto "b" que será utilizado na questão.
  b = float(input('Digite o valor do segundo produto da questão:'))

 # Variável If para caso a resposta da questão anterior estiver dentro do padrão pedido (1 até 6).
 # Variável match para dar continuidade da questão e calcular os respectivos valores dos itens de acordo com a operação escolhida anteriormente.
 # Variável string "ex" para compor a respota final, de acordo com a operação escolhida.
 if equacao >= 1 or equacao <= 6:

  # a = Valor do primeiro produto da questão.
  # b = Valor do segundo produto da questão.
  # c = Resultado da operação entre 'a' e 'b'
  # ex = Apenas uma string que irá ser adicionada na resposta verbal da questão.
  match equacao:
    case 1:
        c = a + b
        ex = 'mais'

    case 2:
        c = a - b
        ex = 'menos'

    case 3:
        c = a / b
        ex = 'dividido por'

    case 4:
        c = a * b
        ex = 'multiplicado por'

    case 5:
        c = a ** (1/2)
        print('O calculo da raiz de [',a,'] resulta em: [',c,'].')

    case 6:
      c = a ** b
      ex = 'potencializado por'

 # Variável if para dar a resposta "print" da questão para as seguintes respostas: (1,2,3,4,6), sendo que a resposta "print" da opção "5" está no case 5 e não necessitará de outra resposta a baixo.
 if equacao != 5:
  
  print('O resultado da equação de [',a,']',ex,'[',b,'] resulta em: [',c,'].')

 # Opção para realizar uma nova questão.
 nova_questao = int(input('Deseja realizar uma nova questão?'
                 '\n 1 - SIM'
                 '\n 2 - NÃO'))
 
 # Alternativa para uma opção de encerramento da questão. 
 if nova_questao == 2:
     print('Fim da questão.')

 # Opção IF e while para continuamento e loping da questão para caso de repetição da questão.
 if nova_questao == 1:
    while nova_questao == 1:
     
     # Opção de anulamento da questão anterior (resposta anterior "c" será 0).
     zero = int(input('Deseja zerar a questão?'
                      '\n 1 - SIM'
                      '\n 2 - NÃO'))
     
     if zero == 1:
        c = 0   
     
     # Questionamento para o usuário escolher a nova operação que será utilizada.
     nova_equacao= int(input('Escolha a nova equação que deseja realizar'
                     '\n 1 - ADIÇÃO'
                     '\n 2 - SUBTRAÇÃO'
                     '\n 3 - DIVISÃO'
                     '\n 4 - MULTIPLICAÇÃO.'
                     '\n 5 - RAIZ.'
                     '\n 6 - POTENCIAÇÃO.')) 
     
     # If para caso a resposta estiver fora do padrão e While para estar em looping até a resposta estiver no padrão (1 até 6).
     if nova_equacao < 1 or nova_equacao > 6: 
      while nova_equacao < 1 or nova_equacao > 6:
       
       print('Opção invalida, tente novamente')
       nova_equacao= int(input('Escolha a nova equação que deseja realizar'
                     '\n 1 - ADIÇÃO'
                     '\n 2 - SUBTRAÇÃO'
                     '\n 3 - DIVISÃO'
                     '\n 4 - MULTIPLICAÇÃO.'
                     '\n 5 - RAIZ.'
                     '\n 6 - POTENCIAÇÃO.')) 

     # Variável If para dar continuidade caso a escolha da operação ser a "5", juntamente com a opção de zerar a questão anterior for positiva "1".
     # Se ambas respostas forem de acordo com a variável, então a operação irá necessitar de um novo produto "c".
     if nova_equacao == 5 and zero == 1:
       c = float(input('Digite o valor do novo produto:')) 

     # Variável Elif para caso a escolha da operação ser a "6", juntamente com a opção de zerar a questão anterior "1" for positiva.
     #Se ambas as respotas forem de acordo com a variável, a nova operação "6" (potênciaçaõ), irá necessitar de um novo produto base "c" e um novo produto para ser seu expoente "d".
     elif nova_equacao == 6 and zero == 1:
       c = float(input('Digite o valor do produto base da equação:'))
       d = float(input('Digite o valor do expoente desse produto:'))
     
     # Variável Elif para caso a escolha de operação estiver dentro do padrão (1,2,3,4,6), pois todas essas alternativas irão necessitar de um novo produto e a alternativa "c" irá necessitar de um novo expoente, caso a opção zero for igual à: "2".
     elif nova_equacao != 5: 
       d = float(input('Digite o valor do novo denominador:'))

     # Opção match igual à anterior, mudando apenas suas variáveis "c" e "d", juntamente com a nova resposta da questão "e".  
     # d = Valor do terceiro produto da questão.
     # e = Resultado da operação entre 'c' e 'd'
     match nova_equacao:
        case 1:
           e = c + d
           ex = 'mais'
          
        case 2:
           e = c - d
           ex = 'menos'
                   
        case 3:
           e = c / d
           ex = 'dividido por'
                    
        case 4:
           e = c * d
           ex = 'multiplicado por'

        case 5:
         e = c ** (1/2)
         print('O calculo da raiz quadrada de: [',c,'] resulta em: [',e,'].')

        case 6:
         e = c ** d
         ex = 'potencializado por'
            
     if nova_equacao != 5:                     
      print('O resultado da equação de [',c,']',ex,'[',d,'] resulta em: [',e,'].')

     # Mudança de valor da resposta anterior para seguir de acordo com o funcionamento da questão.
     c = e

     # Opção para realizar uma nova questão.
     nova_questao = int(input('Deseja realizar uma nova equação?'
                    '\n 1 - SIM'
                    '\n 2 - NÃO'))
     
     # Finalização da questão.
     if nova_questao == 2:
        print('Fim da equação.')

# Função "again" para realizar a questão.     
again()
