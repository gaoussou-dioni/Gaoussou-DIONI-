""" Écrire un programme qui demande le nom et l’âge d’un étudiant à l’université et afficher 
‘’Bonjour …, tu as … ans et bienvenue à l’université’’ en remplaçant les … par respectivement le nom et l’âge de l’étudiant."""

student_name = input("Hey, Student what's your name :) : ")
student_age = int(input("And your age: "))
print ("Bonjour {0}, tu as {1} ans et bienvenue à l’université".format(student_name, student_age))
