import string
import random
string.ascii_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


class Robot:
    '''Attributs de classe'''
    directions = ('NORD', 'EST', 'SUD', 'OUEST')
    statuts = {1 : "En service", 2 : "Hors Service", 3 : "En réparation"}
    nb_robot = 0

    @classmethod
    def getNbRobots(cls):
        return cls.nb_robot

    def __init__(self, robot_type = "Générique"):
        self.__robot_type = robot_type
        self.__numero_serie="template"
        self.__orientation="NORD"
        self.__statut=1
        self.__lst = []
        Robot.nb_robot += 1

    def __len__(self):
        return len(self.__lst)


    @property
    def __robot_type(self):
        '''un seul underscore dans le getter ?'''
        return self._robot_type

    '''setter type'''
    @__robot_type.setter
    def __robot_type(self,value):
        if len(value) >= 2:
            '''un seul underscore dans le setter ?'''
            self._robot_type = value
        else:
            print("Erreur : le type de robot doit faire + de 2 caractères")
            '''un seul underscore dans le setter ?'''
            self._robot_type = "Générique"

    '''numero série'''
    @property
    def __numero_serie(self):
        '''deux underscores'''
        return self.__numero_serie

    @__numero_serie.setter
    def __numero_serie(self,value):
        '''Deux lettres aléatoires'''
        temp=random.choice(string.ascii_letters)+random.choice(string.ascii_letters)
        '''Ajoute un nombre aléatoire'''
        temp=temp+str(random.randrange(100000000))
        '''un seul underscore sinon ça ne marche pas'''
        self._numero_serie = temp

    @property
    def __orientation(self):
        return self.__orientation

    @__orientation.setter
    def __orientation(self,value):
        if value in self.directions:
            self._orientation = value
        else:
            print("Direction erronnée")

    @property
    def __statut(self):
        return self.statuts[self._statut]

    @__statut.setter
    def __statut(self,value):
        value=int(value)
        if value in (1,2,3):
            print("valeur de statut OK")
            self._statut = value
        else:
            print("valeur :",value)
            print("Mauvais statut")


    def tourner(self, entier):
        print("Le robot tourne")
        index=self.directions.index(self._orientation)
        if entier ==-1 or entier ==1:
            index=index+entier
            self.__orientation = self.directions[index]
        else:
            print("Mauvais ordre : entier n'est pas -1 ou 1 :",entier)

    def __str__(self):
        return (f"Robot {self._numero_serie} \n"
                f"Type : {self._robot_type} \n"
                f"Statut : {self.__statut}\n"
                f"Orientation : {self._orientation}\n")
