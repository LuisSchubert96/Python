# CÓD 1 AND #

# O operador AND nos permite executar o código apenas se ambas as consições forem TRUE

age = 17                          # Definindo o valor para 17
has_permit = True                 # Definindo o valor para True   
if age > 16 and has_permit:       # Irá verificar se ambas as condições são verdadeiras, caso forem ele irá imprimir ( Can drive )
    print("Can drive")

# CÓD 2 AND #

# O operador AND pula o bloco de código se uma ou mais condições forem FALSE

age = 17                                  # Definindo o valor para 17
has_permit = True                         # Definindo o valor para True   
if age > 18 and has_permit == True:       # Irá verificar se ambas as condições são verdadeiras, caso forem ele irá imprimir ( Can drive )  
    print("Can drive")                    # Se não for ele irá ignorar o bloco do código IF como acontece nesse caso

# CÓD 3 AND #

# Podemos adcionar quantas condições quisermos no nosso bloco de código

subway_defect = True                               # Definindo o valor para True 
is_sunny = True                                    # Definindo o valor para True 
distance = 2                                       # Definindo o valor para 2
if subway_defect and is_sunny and distance <= 2:   #Irá verificar se ambas as condições são verdadeiras
    print ("Walk to work")

# CÓD 1 OR #

# O operador OR nos permite utilizar o código quando uma das condições forem TRUE

avarage_grade = "A"                                  # Definindo o valor para "A"
final_score = 1400                                   # Definindo o valor para 1400
if avarage_grade == "A" or final_score <= 1300:      #Irá verificar se 1 ou ambas as condições são verdadeiras e irá imprimir 
    print ("Certificate achieved")                   # Se uma ou ambas forem verdadeira irá imprimir ( Certificate achieved )  

# CÓD 2 OR #

# Mas se todas as condições forem FALSE ele irá ignorar o código

average_grade2 = "A"                                  # Definindo o valor para "A"
final_score2 = 1400                                   # Definindo o valor para 1400
if average_grade2 == "B" or final_score2 >= 1500:     # Irá verificar se 1 ou ambas as condições são verdadeiras e irá imprimir ( Certificate achieved )
    print ("Certificate achieved")                    # Mas se ambas forem FALSE ele irá ignorar o código

# CÓD 3 OR #

# Podemos usar quantas condições quiseremos no nosso bloco de código

highest_score = 100                            # Definindo o valor para "A"
score = 70                                     # Definindo o valor para "A"
level = 5                                      # Definindo o valor para "A"
if score > highest_score or level == 5:        # Irá verificar se 1 ou ambas as condições são verdadeiras e irá imprimir ( You won! )
    print("You won!")