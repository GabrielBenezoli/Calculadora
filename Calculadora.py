# Questionamento para o usuário escolher os dois valores inicias que serão utilizados na questão.
a = int(input('Digite o valor do primeiro item da questão:'))
b = int(input('Digite o valor do segundo item da questão:'))

# Def para repetição, caso o usuário escolha uma opção inadequada.
def again():
 
 # Questionamento para o usuário escolher a operação que será utilizada.
 equacao = int(input('Escolha a operação que deseja realizar:'
               '\n 1 - SOMA'
               '\n 2 - SUBTRAÇÃO'
               '\n 3 - DIVISÃO'
               '\n 4 - MULTIPLICAÇÃO'))
 
 # If e else para diferenciar a escolha do usuário e again() para retormar a pergunta caso sua escolha seja fora do pedido.
 if equacao < 1 or equacao > 4:
    print('Opção invalida, tente novamente')
    again()

 else:
  
  # Opção match para realizar qualquer operação de acordo com a escolha do usuário. 
  # Variável string "ex" para compor a respota final, de acordo com a operação escolhida.
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

  print('O resultado da equação de [',a,']',ex,'[',b,'] resulta em: [',c,'].')

  # Opção para jogar novamente.
  nova_questao = int(input('Deseja realizar uma nova questão?'
                 '\n 1 - SIM'
                 '\n 2 - NÃO'))
  
  # Alternativa para uma opção de encerramento da questão.
  if nova_questao == 2:
     print('Fim da questão.')

  # Opção IF e while para continuamento e loping da questão para caso de repetição da questão.
  if nova_questao == 1:
    while nova_questao == 1:
     
     # Opção de anulamento da questão anterior (antiga resposta "c" será 0).
     zero = int(input('Deseja zerar a questão?'
                      '\n 1 - SIM'
                      '\n 2 - NÃO'))
     
     # Opção de anulação da questão anterior.
     if zero == 1:
        c = 0

     d = int(input('Digite o valor do novo denominador:'))    
     
     nova_equaçao= int(input('Escolha a nova equação que deseja realizar'
                     '\n 1 - ADIÇÃO'
                     '\n 2 - SUBTRAÇÃO'
                     '\n 3 - DIVISÃO'
                     '\n 4 - MULTIPLICAÇÃO.')) 
     
     # If para caso a resposta estiver fora do padrão e While para estar em looping até a resposta estiver no padrão.
     if nova_equaçao < 1 or nova_equaçao > 4: 
      while nova_equaçao < 1 or nova_equaçao > 4:
       
       print('Opção invalida, tente novamente')
       nova_equaçao= int(input('Escolha a nova equação que deseja realizar'
                     '\n 1 - ADIÇÃO'
                     '\n 2 - SUBTRAÇÃO'
                     '\n 3 - DIVISÃO'
                     '\n 4 - MULTIPLICAÇÃO.')) 
        
     # Opção match para realizar qualquer operação de acordo com a escolha do usuário.    
     match nova_equaçao:
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
                           
     print('O resultado da equação de [',c,']',ex,'[',d,'] resulta em: [',e,'].')

     # Mudança de valor da resposta anterior para seguir de acordo com o funcionamento da questão.
     c = e

     nova_questao = int(input('Deseja realizar uma nova equação?'
                    '\n 1 - SIM'
                    '\n 2 - NÃO'))
     
     # Finalização da questão.
     if nova_questao == 2:
        print('Fim da equação.')
     
again()
