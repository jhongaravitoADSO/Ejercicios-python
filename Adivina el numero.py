import random
geneartedNumber= random.randrange(1,10)
userGuess=int(input('Adivina un numero entre 1-10:'))
if userGuess==geneartedNumber:
    print("lo escogiste!")
elif userGuess<geneartedNumber:
    print('tu suposicion es demasiado baja')
else:
    print('tu suposicion es demasiado alta')
    