"""Écrire un programme qui demande à l’utilisateur de donner un nombre entier n et de lui afficher la table de multiplication de ce nombre."""

user_input = int(input("Enter a number: "))

number_list = [i for i in range(11)]

for i in number_list:
    print("{}x{} = {}".format(user_input, i, user_input*i))
