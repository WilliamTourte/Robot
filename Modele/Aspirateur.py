from Modele.RobotMobile import RobotMobile


class Aspirateur:
    def __init__(self, marque, puissance : int):

        self._marque = marque
        self._puissance = puissance


    @property
    def marque(self):
        return self._marque

    @marque.setter
    def marque(self, marque):
        self._marque = marque

    @property
    def puissance(self):
        return self._puissance
    @puissance.setter
    def puissance(self, puissance):
        self._puissance = puissance

    def __str__(self):
        return "Aspirateur : "+self._marque+" Puissance : "+str(self._puissance)

class AspirateurRobot(Aspirateur, RobotMobile):
    def __init__(self, abs=0, ord=0, marque="Bosch'", puissance=4):
        RobotMobile.__init__(self, robot_type="Aspirateur Robot", abs=0, ord=0)
        Aspirateur.__init__(self, marque, puissance)
        self._distance_max = 1000
        self._robot_type = "Aspirateur Robot"

    @property
    def distance_max(self):
        return self._distance_max
    @distance_max.setter
    def distance_max(self, value):
        if value > 0:
            self._distance_max = value

    def __str__(self):
        return (RobotMobile.__str__(self)+"\n"+
               "Marque : "+str(self._marque)+"\n"+
                "Puissance : "+str(self._puissance))

    def parcours(self,largeur,longueur):
        ''''''

# Création de pièce de [largeur x longueur] cases
def crea_plateau(largeur, longueur):
    plateau = dict()

    for i in range(0, longueur):
        plateau[i] = dict()
        for j in range(0, largeur):
            plateau[i][j] = "-"
    return plateau

# Affichage plateau
def afficher(plateau):
    for i in sorted(plateau.keys()): #La boucle for i in sorted(plateau.keys()) parcourt les clés du dictionnaire plateau dans l'ordre croissant.
        ligne = [] #Pour chaque clé i, une liste ligne est construite en ajoutant chaque valeur de plateau[i][j].
        for j in sorted(plateau[i].keys()):
            ligne.append(plateau[i][j])
        print(" ".join(ligne)) #La ligne est affichée en utilisant " ".join(ligne), ce qui permet de séparer chaque élément par un espace.

plateau=crea_plateau(10,15)
afficher(plateau)

'''plateau[ord][abs]'''
plateau[0][1]="X"
print()
afficher(plateau)