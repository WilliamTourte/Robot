from Modele.Robot import Robot

r1 = Robot()
r2 = Robot("Mécanique")
r3 = Robot("Electrique")

print("------------------------------------")
print("------- TP : PREMIERE PARTIE -------")
print("------------------------------------")

print("-------- CREATION DE ROBOTS --------")
print(r1)
print('_'*36)
print(r2)
print('_'*36)
print(r3)
print('_'*36)
print("Nombre de robots créés au total : ", Robot.nb_robot)
print("------------------------------------")

print("--------- TEST SETTER TYPE ---------")
r4 = Robot("T")  # Doit afficher un message d'erreur
print(r4)  # Doit afficher un type Générique
print('_'*36)
r2.robot_type = "K"  # Doit afficher un message d'erreur
print(r2)  # Le type ne doit pas avoir été modifié
print("------------------------------------")

print("--------- TEST STATUT ---------")
r2.statut = 2
print(r2)
print('_'*36)
r2.statut = 5  # Doit afficher un message d'erreur
print(r2)  # Le statut ne doit pas avoir été modifié
print("------------------------------------")

print("--------- TEST TOURNER ---------")
r3.tourner(1)
print(r3)
print('_'*36)
r3.tourner(-1)
print(r3)
print('_'*36)
r3.tourner(12)  # Doit afficher un message d'erreur
print(r3)  # Le robot ne doit pas avoir tourné
print("------------------------------------")