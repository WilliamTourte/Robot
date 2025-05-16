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
        self._numero_serie = self.genNumeroSerie()  # Utilisation du setter pour générer le numéro de série : pas d'underscore !
        self._orientation = "NORD"
        self._statut = 1
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
            return

        if len(value) >= 2:
            self._robot_type = value
        else:
            print("Erreur : le type de robot doit faire + de 2 caractères")
            self._robot_type = "Générique"

    @property
    def numero_serie(self):
        return self._numero_serie


    def genNumeroSerie(self):
        temp = random.choice(string.ascii_letters) + random.choice(string.ascii_letters)
        temp = temp + str(random.randrange(100000000))
        return temp

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

            self._statut = value
        else:
            print("Mauvais statut car valeur =", value)

    def tourner(self, entier):

        index = self.directions.index(self._orientation)
        if entier == -1 or entier == 1:
            index = index + entier
            self._orientation = self.directions[index]
            print("Le robot tourne")
        else:
            print("Mauvais ordre : entier n'est pas -1 ou 1 :", entier)

    def __str__(self):
        return (f"Robot {self._numero_serie} \n"
                f"Type : {self.robot_type} \n"
                f"Statut : {self.statut}\n"
                f"Orientation : {self._orientation}\n")