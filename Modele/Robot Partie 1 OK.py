import string
import random
string.ascii_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

class Robot:
    '''Attributs de classe'''
    directions = ('NORD', 'EST', 'SUD', 'OUEST')
    statuts = {1: "En service", 2: "Hors Service", 3: "En réparation"}
    nb_robot = 0

    @classmethod
    def getNbRobots(cls):
        return cls.nb_robot

    def __init__(self, robot_type="Générique"):
        self._robot_type = robot_type
        self.numero_serie = "t"  # Utilisation du setter pour générer le numéro de série : pas d'underscore !
        self._orientation = "NORD"
        self.statut = 1
        self._lst = []
        Robot.nb_robot += 1

    def __len__(self):
        return len(self._lst)

    @property
    def robot_type(self):
        return self._robot_type

    @robot_type.setter
    def robot_type(self, value):
        if value is None:
            self._robot_type = "Générique"
        if len(value) >= 2:
            self._robot_type = value
        else:
            print("Erreur : le type de robot doit faire + de 2 caractères")
            self._robot_type = "Générique"

    @property
    def numero_serie(self):
        return self._numero_serie

    @numero_serie.setter
    def numero_serie(self, value):
        temp = random.choice(string.ascii_letters) + random.choice(string.ascii_letters)
        temp = temp + str(random.randrange(100000000))
        self._numero_serie = temp

    @property
    def orientation(self):
        return self._orientation

    @orientation.setter
    def orientation(self, value):
        if value in self.directions:
            self._orientation = value
        else:
            print("Direction erronnée")

    @property
    def statut(self):
        return self.statuts[self._statut]

    @statut.setter
    def statut(self, value):
        value = int(value)
        if value in (1, 2, 3):
            print("valeur de statut OK")
            self._statut = value
        else:
            print("valeur :", value)
            print("Mauvais statut")

    def tourner(self, entier):
        print("Le robot tourne")
        index = self.directions.index(self._orientation)
        if entier == -1 or entier == 1:
            index = index + entier
            self._orientation = self.directions[index]
        else:
            print("Mauvais ordre : entier n'est pas -1 ou 1 :", entier)

    def __str__(self):
        return (f"Robot {self._numero_serie} \n"
                f"Type : {self._robot_type} \n"
                f"Statut : {self.statut}\n"
                f"Orientation : {self._orientation}\n")
