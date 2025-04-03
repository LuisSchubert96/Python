# Cód 1 #
points = 7600                   # Define o valor da variavel em 7600
points_needed = 8000            # Define o valor da variavel em 8000
if points >= points_needed:     # Verifica se o valor de points é maior ou igual ao points_needed
    print ("You're Level 2")
else:                            # Como o valor é menor ele vai para o else, onde ele irá imprimir ( You need 400 more poins to reach Level 2)
    print(f"You need {points_needed-points} more points to reach Level 2")



# Cód 2 # 

chosen_number = 7            # Define o valor da variavel em 7

if chosen_number == 12:      # Verifica se o valor escolhido é igual
    print ("You guessed right!")
else:                         # Como o valor é diferente != ele irá imprimir a frase ( Have another go )
    print("Have another go")        