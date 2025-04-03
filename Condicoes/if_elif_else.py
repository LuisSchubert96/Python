# CÓD 1 #

hour1= 9                        # Definindo o valor da variavel para 9
if hour1 < 12:                  # If irá verificar se a variavel é menor que 12
    print("Good morning")       # Se for menor que 12 irá imprimir ( Good morning )
else:                           
    print("Good afternoon")     # Se não for menor ele irá imprimir ( Good afternoon )

# CÓD 2 #

hour2 = 14                      # Definindo o valor da variavel para 14
if hour2 < 12:                  # If irá verificar se a variavel é menor que 12
    print("Good morning")      # Se for menor que 12 irá imprimir ( Good morning )
elif hour2 < 17:                # elif é a mesma coisa que o Else If e ele será usado quando possuirmos uma segunda condição para verificarmos
    print("Good afternoon")     # Se o valor estipulado não for menor que 12 ele irá passar para o elif, e se for menor que o valor estipulado ele irá imprimir ( Good Afternoon )
 
# CÓD 3 #

hour3 = 18                      # Definindo o valor da variavel para 14
if hour3 < 12:                  # If irá verificar se a variavel é menor que 12
    print("Good morning")       # Se for menor que 12 irá imprimir ( Good morning )
elif hour3 < 17:                # elif é a mesma coisa que o Else If e ele será usado quando possuirmos uma segunda condição para verificarmos
    print("Good afternoon")     # Se o valor estipulado não for menor que 12 ele irá passar para o elif, e se for menor que o valor estipulado ele irá imprimir ( Good Afternoon )
else:                           # Já aqui se o valor estipulado não for aceito em nenhumas das duas condições ele irá automáticamente cair no nosso else onde irá imprimir ( Good night )
    print("Good night")    

# CÓD 4 #    

hour4 = 18                      # Mas lembrando...desde que venham antes do else, podemos usar quantos elif acharmos necessarios.
if hour4 < 12:                  
    print("Good morning")       
elif hour4 < 17:                
    print("Good afternoon")
elif hour4 < 21:
    print("Good evening")         
else:                           
    print("Good night")   